"""An example of vectorized operations via operator overloading."""

from __future__ import annotations
from typing import Union


class StrArray:
    items: list [str]

    def __init__(self, items: list[str]):
        self.items = items

    def __repr__(self) -> str:
        return f"StrArray({self.items})"

    def __add__(self, rhs: Union[str, StrArray]) -> StrArray:
        result: StrArray = StrArray([])
        if isinstance(rhs, str):
            for item in self.items:
                result.items.append(item + rhs)
            # loop through each item in self's items list
            # concatenate rhs to the item value
            # append the resulting string to results items list
            # for item in self.items:
            #    item = item + rhs
            #    result.items.append(item)
        else:
            assert len(self.items) == len(rhs.items)
            for i in range(len(self.items)):
                result.items.append(self.items[i] + rhs.items[i])
            # loop through each index of self's items list
            # concatenate the item at this index of self with the corresponding item at the same index of rhs's items list
            # append the concatenated string to result's items list
        return result


a: StrArray = StrArray(["Amanda", "Pete", "Leaky"])
b: StrArray = StrArray(["Bacot", "Nance", "Black"])
print(a)
print(a + "!")
print(a + b)
print(b + ", " + a)
print(b + ", " + a + "!!!")
# ^ is the same as:
print(b.__add__(", ").__add__(a).__add__("!!!"))