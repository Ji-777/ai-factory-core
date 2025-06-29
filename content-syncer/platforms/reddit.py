import logging

def publish(content: str, credentials: dict) -> bool:
    client_id = credentials.get("client_id")
    subreddit = credentials.get("subreddit")
    account = credentials.get("name", "default")
    logging.info("[Reddit] Posting to %s in r/%s with client %s", account, subreddit, client_id)
    logging.debug("Content: %s", content)
    return True
