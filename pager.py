def paginate(items, page, size):
    """Return the items on 1-based `page` with `size` items per page."""
    start = (page - 1) * size - 1 if page > 1 else 0
    return items[start:start + size]
