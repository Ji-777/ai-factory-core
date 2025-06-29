import json
import logging
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup
import markdown

def setup_logging(log_file: str = "log.txt") -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[logging.FileHandler(log_file, encoding="utf-8"), logging.StreamHandler()]
    )

def load_config(path: str = "config.json") -> dict:
    if not Path(path).is_file():
        raise FileNotFoundError(f"Config file {path} not found")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def read_content(path: str) -> str:
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"Content file {path} not found")
    text = p.read_text(encoding="utf-8")
    if p.suffix.lower() in {".md", ".markdown"}:
        html = markdown.markdown(text)
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()
    elif p.suffix.lower() in {".html", ".htm"}:
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()
    return text

def log_result(platform: str, success: bool) -> None:
    status = "SUCCESS" if success else "FAILURE"
    logging.info("%s: %s", platform, status)
