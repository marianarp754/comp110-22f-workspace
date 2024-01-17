"""Tests for linked list utils."""

import pytest
from exercises.ex11.linked_list import Node, last, value_at, max, linkify, scale

__author__ = "730576205"


def test_last_empty() -> None:
    """Last of an empty Linked List should raise a ValueError."""
    with pytest.raises(ValueError):
        last(None)


def test_last_non_empty() -> None:
    """Last of a non-empty list should return its last data value."""
    linked_list = Node(1, Node(2, Node(3, None)))
    assert last(linked_list) == 3


def test_value_at_first() -> None:
    """Tests to see if the data of the first Node stored is stored at the index 0."""
    assert value_at(Node(10, Node(20, Node(30, None))), 0) == 10


def test_value_at_last() -> None:
    """Tests to see if the data of the last Node stored is stored at the index 2."""
    assert value_at(Node(10, Node(20, Node(30, None))), 2) == 30


def test_max_ascending() -> None:
    """Tests to see if the max function returns 30 when the data values of the Nodes are in ascending order."""
    assert max(Node(10, Node(20, Node(30, None)))) == 30


def test_max_descending() -> None:
    """Tests to see if the max function returns 30 when the data values of the Nodes are in descending order."""
    assert max(Node(30, Node(20, Node(10, None)))) == 30


def test_linkify_diff() -> None:
    """Tests to see of the linkify function returns a Linked List of Nodes when the input list has all different values."""
    assert str(linkify([1, 2, 3])) == "1 -> 2 -> 3 -> None"


def test_linkify_same() -> None:
    """Tests to see of the linkify function returns a Linked List of Nodes when the input list has all the same values."""
    assert str(linkify([2, 2, 2])) == "2 -> 2 -> 2 -> None"


def test_scale_long() -> None:
    """Tests to see if the scale function returns a new linked list of Nodes when the original list is long."""
    assert str(scale(linkify([1, 2, 3, 4, 5, 6]), 2)) == "2 -> 4 -> 6 -> 8 -> 10 -> 12 -> None"


def test_scale_short() -> None:
    """Tests to see if the scale function returns a new linked list of Nodes when the original list is short."""
    assert str(scale(linkify([1, 2, 3]), 2)) == "2 -> 4 -> 6 -> None"