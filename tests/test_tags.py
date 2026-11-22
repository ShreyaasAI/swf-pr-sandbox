from tags import add_tag


def test_explicit_list():
    assert add_tag("a", ["x"]) == ["x", "a"]


def test_default_list_is_fresh():
    add_tag("a")
    assert add_tag("b") == ["b"]
