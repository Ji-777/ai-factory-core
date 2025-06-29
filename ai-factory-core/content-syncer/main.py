from core_sdk.config import settings
from core_sdk.logger import get_logger
from core_sdk.utils import some_helper_function

logger = get_logger(__name__)

import argparse
import importlib
from typing import Dict

from utils import load_config, read_content, setup_logging, log_result

PLATFORM_MODULES: Dict[str, str] = {
    "twitter": "platforms.twitter",
    "linkedin": "platforms.linkedin",
    "medium": "platforms.medium",
    "telegram": "platforms.telegram",
    "reddit": "platforms.reddit",
}

def get_module(name: str):
    module_path = PLATFORM_MODULES.get(name)
    if not module_path:
        raise ValueError(f"Unsupported platform: {name}")
    return importlib.import_module(module_path)

def main():
    parser = argparse.ArgumentParser(description="Distribute content to multiple platforms")
    parser.add_argument("--file", help="Path to Markdown/HTML file")
    parser.add_argument("--link", help="Link to share")
    parser.add_argument("--platforms", nargs="+", required=True, help="Platforms to publish to")
    parser.add_argument("--config", default="config.json", help="Path to config.json")
    args = parser.parse_args()

    setup_logging()
    config = load_config(args.config)

    if args.file:
        content = read_content(args.file)
    elif args.link:
        content = args.link
    else:
        parser.error("Either --file or --link must be provided")

    for platform_name in args.platforms:
        try:
            module = get_module(platform_name.lower())
        except ValueError as exc:
            log_result(platform_name, False)
            print(exc)
            continue

        accounts = config.get(platform_name.lower(), [])
        if not accounts:
            log_result(platform_name, False)
            print(f"No configuration for {platform_name}")
            continue
        for account in accounts:
            template = account.get("template", "{content}")
            formatted = template.replace("{content}", content)
            success = module.publish(formatted, account)
            log_result(f"{platform_name}:{account.get('name', 'default')}", success)

if __name__ == "__main__":
    main()
