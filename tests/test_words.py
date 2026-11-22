from words import word_count


def test_empty():
    assert word_count("") == {}


def test_counts_repeated_words():
    assert word_count("a b a") == {"a": 2, "b": 1}
