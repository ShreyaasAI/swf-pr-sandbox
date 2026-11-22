from slugs import slugify


def test_single_word():
    assert slugify("word") == "word"


def test_spaces_and_case():
    assert slugify("Hello   World") == "hello-world"
