def full_name(first, last=None):
    if last is None:
        return first
    return first + " " + last
