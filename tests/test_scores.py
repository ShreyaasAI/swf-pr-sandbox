from scores import top_scores


def test_n_zero():
    assert top_scores([3, 1, 2], 0) == []


def test_top_two():
    assert top_scores([3, 9, 1, 7], 2) == [9, 7]
