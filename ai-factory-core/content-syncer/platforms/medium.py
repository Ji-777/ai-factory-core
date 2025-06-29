import logging

def publish(content: str, credentials: dict) -> bool:
    token = credentials.get("token")
    account = credentials.get("name", "default")
    logging.info("[Medium] Posting to %s with token %s", account, token)
    logging.debug("Content: %s", content)
    return True
