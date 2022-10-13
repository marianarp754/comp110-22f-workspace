"""EX07 - Dictionary Functions Unit Tests."""

__author__ = "730576205"

from dictionary import invert, favorite_color, count
import pytest


def test_invert_single_letter() -> None:
    """Tests when invert has keys that are only one charcter long."""
    assert invert({"a": "z", "b": "y", "c": "x"}) == {"z": "a", "y": "b", "x": "c"}


def test_invert_same_value() -> None:
    """Tests when invert has more than one key that has the same value."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_invert_words() -> None:
    """Tests when invert has keys that are more than one charcter long.."""
    assert invert({"apple": "cat"}) == {"cat": "apple"}


def test_favorite_color_same_and_diff() -> None:
    """Tests when favorite_color has more than one key that has the same value."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color_diff_color() -> None:
    """Tests when favorite_color has more than one key that has a different value each time."""
    assert favorite_color({"Marc": "yellow", "Ezri": "green", "Kris": "blue"}) == "yellow"


def test_favorite_color_same_color() -> None:
    """Tests when favorite_color has more than one key that has the same value each time."""
    assert favorite_color({"Marc": "blue", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_count_same_and_diff() -> None:
    """Tests when count has more than one key that has the same value."""
    a_list: list[str] = ["yellow", "blue", "blue"]
    assert count(a_list) == {"yellow": 1, "blue": 2}


def test_count_same() -> None:
    """Tests when count has more than one key that has the same value each time."""
    a_list: list[str] = ["blue", "blue", "blue"]
    assert count(a_list) == {"blue": 3}


def test_count_diff() -> None:
    """Tests when count has more than one key that has a different value each time."""
    a_list: list[str] = ["yellow", "green", "blue"]
    assert count(a_list) == {"yellow": 1, "green": 1, "blue": 1}