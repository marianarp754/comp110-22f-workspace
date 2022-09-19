"""EX04 - `list` Utility Functions."""

__author__ = "730576205"


def all(list_num: (list[int]), single_num: int) -> bool:
    """Return a bool indicating whether or not all the ints in the list are the same as the given int."""
    i: int = 0
    if len(list_num) == 0:
        return False
    while i < len(list_num):
        if list_num[i] != single_num:
            return False
        i = i + 1
    return True


def max(input: list[int]) -> int:
    """Return the largest in the List."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    else:
        i: int = 0
        large_num: int = input[0]
        while i < len(input):
            if input[i] > large_num:
                large_num = input[i]
            i = i + 1
        return large_num


def is_equal(first_list: list[int], sec_list: list[int]) -> bool:
    """Given two lists of int values, return True if every element at every index is equal in both lists."""
    i: int = 0
    if len(first_list) != len(sec_list):
        return False
    while i < len(first_list):
        if first_list[i] != sec_list[i]:
            return False
        i = i + 1
    return True