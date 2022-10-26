"""Dictionary related utility functions."""

__author__ = "730576205"


from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read an entire CSV of data into a list of rows, each row represented as dict[str, str]."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column whose name is the second parameter."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform_ a table represented as a list of rows (e.g. list[dict[str, str]]) into one represented as a dictionary of columns (e.g. dict[str, list[str]])."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(the_dict: dict[str, list[str]], the_int: int) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. dict[str, list[str]]) table with only the first N (a parameter) rows of data for each column."""
    result: dict[str, list[str]] = {}
    for column in the_dict:
        a_list: list[str] = []
        i: int = 0
        if len(the_dict[column]) <= the_int:
            return the_dict
        else:
            while i < the_int:
                a_list.append((the_dict[column])[i])
                i = i + 1
            result[column] = a_list
    return result


def select(a_dict: dict[str, list[str]], the_list: list[str]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. dict[str, list[str]]) table with only a specific subset of the original columns."""
    result: dict[str, list[str]] = {}
    for column in the_list:
        result[column] = a_dict[column]
    return result


def concat(one_dict: dict[str, list[str]], two_dict: dict[str, list[str]]) -> dict[str, list[str]]:
    """Produce a new column-based (e.g. dict[str, list[str]]) table with two column-based tables combined."""
    result: dict[str, list[str]] = {}
    for column in one_dict:
        result[column] = one_dict[column]
    for column in two_dict:
        if column in result:
            result[column] += two_dict[column]
        else:
            result[column] = two_dict[column]
    return result


def count(another_list: list[str]) -> dict[str, int]:
    """Given a list[str], this function will produce a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    result: dict[str, int] = {}
    for item in another_list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result