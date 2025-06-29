from core_sdk.config import settings
from core_sdk.logger import get_logger
from core_sdk.utils import some_helper_function

logger = get_logger(__name__)

import argparse
import logging
import os
from urllib.parse import urlparse, parse_qs

import pandas as pd
import requests
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

SHOPIFY_API_KEY = os.getenv("SHOPIFY_API_KEY")
SHOPIFY_PASSWORD = os.getenv("SHOPIFY_PASSWORD")
SHOPIFY_DOMAIN = os.getenv("SHOPIFY_DOMAIN")  # e.g. myshop.myshopify.com
SHOPIFY_API_VERSION = os.getenv("SHOPIFY_API_VERSION", "2023-07")
SHOPIFY_LOCATION_ID = os.getenv("SHOPIFY_LOCATION_ID")


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def read_inventory(source: str) -> pd.DataFrame:
    """Read inventory data from a local Excel file or Google Sheet."""
    if os.path.isfile(source):
        df = pd.read_excel(source)
    else:
        df = read_google_sheet(source)
    if "SKU" not in df.columns or "Quantity" not in df.columns:
        raise ValueError("Source must contain 'SKU' and 'Quantity' columns")
    return df[["SKU", "Quantity"]]


def read_google_sheet(url: str) -> pd.DataFrame:
    """Read a Google Sheet via its CSV export."""
    parsed = urlparse(url)
    if "docs.google.com" not in parsed.netloc:
        raise ValueError("Not a Google Sheets URL")
    parts = parsed.path.split("/")
    try:
        sheet_id = parts[3]
    except IndexError:
        raise ValueError("Invalid Google Sheets URL")
    gid = parse_qs(parsed.query).get("gid", ["0"])[0]
    csv_url = (
        f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"
    )
    return pd.read_csv(csv_url)


def shopify_session() -> requests.Session:
    """Create a configured requests session for Shopify API."""
    if not all([SHOPIFY_API_KEY, SHOPIFY_PASSWORD, SHOPIFY_DOMAIN, SHOPIFY_LOCATION_ID]):
        raise EnvironmentError("Missing Shopify credentials or location id")
    session = requests.Session()
    session.auth = (SHOPIFY_API_KEY, SHOPIFY_PASSWORD)
    session.headers.update({"Content-Type": "application/json"})
    return session


def base_url() -> str:
    return f"https://{SHOPIFY_DOMAIN}/admin/api/{SHOPIFY_API_VERSION}"


def get_inventory_item_id(session: requests.Session, sku: str, dry_run: bool = False) -> str | None:
    """Fetch the inventory item ID for a given SKU."""
    if dry_run:
        logging.info("[Dry Run] Simulated inventory_item_id fetch for SKU %s", sku)
        return "simulated_inventory_item_id"

    url = f"{base_url()}/variants.json"
    params = {"sku": sku}
    resp = session.get(url, params=params)
    if resp.status_code != 200:
        logging.error("Failed to fetch variant for SKU %s: %s", sku, resp.text)
        return None
    variants = resp.json().get("variants", [])
    if not variants:
        logging.error("No variant found for SKU %s", sku)
        return None
    return variants[0].get("inventory_item_id")


def update_inventory_level(
    session: requests.Session, inventory_item_id: str, quantity: int, dry_run: bool = False
) -> bool:
    if dry_run:
        logging.info("[Dry Run] Simulated update of inventory ID %s to quantity %d", inventory_item_id, quantity)
        return True

    url = f"{base_url()}/inventory_levels/set.json"
    payload = {
        "location_id": SHOPIFY_LOCATION_ID,
        "inventory_item_id": inventory_item_id,
        "available": quantity,
    }
    resp = session.post(url, json=payload)
    if resp.status_code == 200:
        return True
    logging.error("Inventory update failed: %s", resp.text)
    return False


def sync_inventory(source: str, dry_run: bool = False) -> None:
    data = read_inventory(source)
    session = shopify_session()
    for _, row in data.iterrows():
        sku = str(row["SKU"]).strip()
        qty = int(row["Quantity"])
        inventory_item_id = get_inventory_item_id(session, sku, dry_run=dry_run)
        if not inventory_item_id:
            logging.error("Skipping SKU %s", sku)
            continue
        if update_inventory_level(session, inventory_item_id, qty, dry_run=dry_run):
            logging.info("Updated %s to %s", sku, qty)
        else:
            logging.error("Failed to update %s", sku)


def main():
    parser = argparse.ArgumentParser(description="Sync inventory to Shopify")
    parser.add_argument("source", help="Path to Excel file or Google Sheet URL")
    parser.add_argument("--dry-run", action="store_true", help="Simulate API calls without executing them")
    args = parser.parse_args()
    try:
        sync_inventory(args.source, dry_run=args.dry_run)
    except Exception as exc:
        logging.exception("Error while syncing: %s", exc)


if __name__ == "__main__":
    main()
