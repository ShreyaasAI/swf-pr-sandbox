import re

_EMAIL = re.compile(r"^[A-Za-z0-9._-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)+$")


def is_valid_email(value):
    return bool(_EMAIL.match(value))
