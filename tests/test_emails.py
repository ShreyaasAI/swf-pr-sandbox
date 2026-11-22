from emails import is_valid_email


def test_simple_valid():
    assert is_valid_email("ann@example.com")


def test_missing_domain_invalid():
    assert not is_valid_email("ann@")


def test_plus_address_valid():
    assert is_valid_email("ann+news@example.com")
