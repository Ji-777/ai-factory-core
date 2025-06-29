# config.py - Global configuration settings

import os

FIVERR_CSV_PATH = os.getenv("FIVERR_CSV_PATH", "data/fiverr_orders.csv")
SHOPIFY_TOKEN = os.getenv("SHOPIFY_TOKEN", "your_shopify_token")
CONTENT_SYNC_API_KEY = os.getenv("CONTENT_SYNC_API_KEY", "your_content_sync_api_key")
