from datetime import datetime


def parse_iso(value):
    return datetime.strptime(value, "%Y-%m-%d").date()
