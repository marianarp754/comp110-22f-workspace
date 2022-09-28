"""EX05 - `list` Utility Test Functions."""

__author__ = "730576205"

from utils import only_evens, concat, sub


def test_only_evens_one_even() -> None:
    """Tests for even numbers when there is only one even number in the list."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_no_even() -> None:
    """Tests for even numbers when there is no even numbers in the list."""
    assert only_evens([1, 5, 3]) == []


def test_only_evens_all_even() -> None:
    """Tests for even numbers when all the numbers in the list are even."""
    assert only_evens([4, 4, 4]) == [4, 4, 4]


def test_concat_same_length() -> None:
    """Tests for two lists of unique ints of the same length."""
    assert concat([1, 2, 3], [4, 5, 6]) == ([1, 2, 3, 4, 5, 6])


def test_concat_diff_length() -> None:
    """Tests for two lists of unique ints and differing lengths."""
    assert concat([1, 2, 3, 4], [5, 6]) == ([1, 2, 3, 4, 5, 6])


def test_concat_same_list() -> None:
    """Tests for two identical lists."""
    assert concat([1, 2, 3], [1, 2, 3]) == ([1, 2, 3, 1, 2, 3])


def test_sub_start_idx_0() -> None:
    """Tests for when the start index is zero."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 0, 3) == [10, 20, 30]


def test_sub_start_idx_neg() -> None:
    """Tests for when the start index is negative."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, -1, 3) == [10, 20, 30]


def test_sub_end_idx() -> None:
    """Tests for when end index is greater than the length of the list."""
    a_list = [10, 20, 30, 40]
    assert sub(a_list, 0, 5) == [10, 20, 30, 40]