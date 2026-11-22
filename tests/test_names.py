from names import full_name


def test_both_names():
    assert full_name("Ada", "Lovelace") == "Ada Lovelace"


def test_first_name_only():
    assert full_name("Ada") == "Ada"
