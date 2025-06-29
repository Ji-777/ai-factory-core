import logging

def publish(content: str, credentials: dict) -> bool:
    token = credentials.get("token")
    chat_id = credentials.get("chat_id")
    account = credentials.get("name", "default")
    logging.info("[Telegram] Posting to %s chat %s with token %s", account, chat_id, token)
    logging.debug("Content: %s", content)
    return True
