"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730576205"


class Simpy:
    """A utility class that is helpful for working with sequences of numerical data, just like what you would expect to see in a column of a data table."""

    values: list[float]

    def __init__(self, values: list[float]):
        """Initialize the values attribute of the newly constructed SImpy object to the argument passed in."""
        self.values = values
    
    def __repr__(self) -> str:
        """Converts Simpy object to a str representation."""
        return f"Simpy({self.values})"

    def fill(self, float_value: float, int_value: int) -> None:
        """Fill's purpose is to fill a Simpy's values with a sepcific number of repeating values."""
        self.values = []
        i: int = 0
        while i < int_value:
            self.values.append(float_value)
            i = i + 1

    def arange(self, the_start: float, the_stop: float, the_step: float = 1.0) -> None:
        """Arange's purpose is to fill in the values attribute with range of values, like the range built-in function, but in terms of floats."""
        assert the_step != 0.0
        self.values = []
        while abs(the_start) < abs(the_stop):
            self.values.append(the_start)
            the_start = the_start + the_step

    def sum(self) -> float:
        """Sum's purpose is to compute and return the sum of all the items in the values attribute."""
        the_float: float = 0.0
        i: int = 0
        while i < len(self.values):
            the_float += self.values[i]
            i = i + 1
        return the_float

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """The ability to use the _addition operator_ (+) in conjunction with Simpy objects and floats."""
        result: Simpy = Simpy([])
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs)
                i = i + 1        
        else:
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                result.values.append(self.values[i] + rhs.values[i])
                i = i + 1
        return result

    def __pow__(self, lhs: Union[float, Simpy]) -> Simpy:
        """The ability to use the _power operator_ (**) in conjunction with Simpy objects and floats."""
        result: Simpy = Simpy([])
        if isinstance(lhs, float):
            i: int = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** lhs)
                i = i + 1        
        else:
            assert len(self.values) == len(lhs.values)
            i = 0
            while i < len(self.values):
                result.values.append(self.values[i] ** lhs.values[i])
                i = i + 1
        return result

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """The ability to produce a _mask_, or a list[bool], based on the equality of each item in the values attribute with some other Simpy object or a float value."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs:
                    result.append(True)
                else: 
                    result.append(False)
                i = i + 1        
        else:
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    result.append(True)
                else: 
                    result.append(False)
                i = i + 1
        return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """The ability to produce a _mask_, or a list[bool], based on the greater than relationship between each item in the values attribute with some other Simpy object or a float value."""
        result: list[bool] = []
        if isinstance(rhs, float):
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs:
                    result.append(True)
                else: 
                    result.append(False)
                i = i + 1        
        else:
            assert len(self.values) == len(rhs.values)
            i = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    result.append(True)
                else: 
                    result.append(False)
                i = i + 1
        return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """The ability to use the _subscription_ operator with Simpy objects."""
        result: Simpy = Simpy([])
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            assert len(self.values) == len(rhs)
            i = 0
            while i < len(rhs):
                if rhs[i]:
                    result.values.append(self.values[i])
                i = i + 1
            return result