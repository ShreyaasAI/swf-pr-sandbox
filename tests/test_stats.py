import pytest

from stats import average


def test_whole_average():
    assert average([2, 4]) == 3


def test_empty_raises():
    with pytest.raises(ValueError):
        average([])


def test_fractional_average():
    assert average([1, 2]) == 1.5
