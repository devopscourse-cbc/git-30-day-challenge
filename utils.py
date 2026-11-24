import datetime

def timestamp():
    return datetime.datetime.now().isoformat()

def format_name(first, last):
    return f"{first} {last}"
