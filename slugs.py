def slugify(text):
    words = text.split()
    return '-'.join(word.capitalize().lower() for word in words)
