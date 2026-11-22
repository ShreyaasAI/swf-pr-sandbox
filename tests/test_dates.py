from datetime import date

from dates import parse_iso


def test_same_day_and_month():
    assert parse_iso("2024-05-05") == date(2024, 5, 5)


def test_month_and_day_order():
    assert parse_iso("2024-03-07") == date(2024, 3, 7)
