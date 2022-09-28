"""EX05 - `list` Utility Functions."""

__author__ = "730576205"


def only_evens(list_num: (list[int])) -> (list[int]):
    """Return a new list containing only even integers."""
    i: int = 0
    even_list: list[int] = []
    while i < len(list_num):
        if list_num[i] % 2 == 0:
            even_list.append(list_num[i])
        i = i + 1
    return even_list


def concat(first_list: (list[int]), sec_list: (list[int])) -> (list[int]):
    """Return a new list that contains all of the elements of the first list followed by all of the elements of the second list."""
    i: int = 0
    big_list: list[int] = []
    while i < len(first_list):
        big_list.append(first_list[i])
        i = i + 1
    i = 0
    while i < len(sec_list):
        big_list.append(sec_list[i])
        i = i + 1
    return big_list


def sub(a_list: (list[int]), start_idx: int, end_idx: int) -> (list[int]):
    """Return a list that is a subset of the given list, between the specified start index and the end index (not including the end index)."""
    the_list: list[int] = []
    if len(a_list) == 0:
        return []
    if start_idx > len(a_list):
        return []
    if end_idx < 0:
        return []
    if start_idx < 0:
        start_idx = 0
    if end_idx > len(a_list):
        end_idx = len(a_list)
    while start_idx < end_idx:
        the_list.append(a_list[start_idx])
        start_idx = start_idx + 1
    return the_list