from bounds import clamp


def test_inside_range():
    assert clamp(5, 0, 10) == 5


def test_below_range():
    assert clamp(-3, 0, 10) == 0


def test_above_range():
    assert clamp(15, 0, 10) == 10
