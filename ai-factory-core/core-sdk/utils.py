# utils.py - Reusable helper functions

import datetime

def get_today_date():
    return datetime.datetime.today().strftime("%Y-%m-%d")

def is_valid_email(email: str) -> bool:
    return "@" in email and "." in email
