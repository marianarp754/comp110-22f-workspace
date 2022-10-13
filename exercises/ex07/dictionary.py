"""EX07 - Dictionary Functions."""

__author__ = "730576205"


def invert(a_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of [str, str], invert should return a dict[str, str] that inverts the keys and the values."""
    the_result: dict[str, str] = {}
    value_frequency: dict[str, int] = {}
    for key in a_dict:
        if a_dict[key] in value_frequency:
            value_frequency[a_dict[key]] += 1
        else: 
            value_frequency[a_dict[key]] = 1
    for x in value_frequency:
        if value_frequency[x] >= 2: 
            raise KeyError
    for y in a_dict:
        the_result[a_dict[y]] = y
    return the_result


def favorite_color(the_dict: dict[str, str]) -> str:
    """Given a dictionary of [sr, str], favorite_color should return a str which is the color that appears most frequently. If there is a tie for most popular color, favorite_color should return the color that appeared in the dictionary first."""
    max: int = 0
    fav_color: str = ""
    a_result: dict[str, int] = {}
    for key in the_dict:
        if the_dict[key] in a_result:
            a_result[the_dict[key]] += 1
        else: 
            a_result[the_dict[key]] = 1
    for color in a_result:
        if a_result[color] > max:
            max = a_result[color]
            fav_color = color
    return fav_color


def count(the_list: list[str]) -> dict[str, int]:
    """Given a list of [str], count should return a dict[str, int] where each key is a unique value in the given list and each value associated is the count of the number of times that value appeared in the input list."""
    this_result: dict[str, int] = {}
    for i in range(0, len(the_list)):
        if the_list[i] in this_result:
            this_result[the_list[i]] += 1
        else: 
            this_result[the_list[i]] = 1
    return this_result