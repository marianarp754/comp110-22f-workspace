"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi
from math import sqrt


__author__ = "730576205"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, other: Point) -> float:
        """Returns the distance between the Point object the method was called on and some other Point object passed in as a parameter."""
        the_distance: float = sqrt(((self.x - other.x)**2) + ((self.y - other.y)**2))
        return the_distance


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Uses the sickness attribute of a Cell to count the number of ticks it has been infected for."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def contract_disease(self) -> None:
        """A method of Cell that assigns the INFECTED constant defined above to the sickness attribute of the Cell object the method is called on."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """A method of a Cell that returns True when the cell's sickness attribute is equal to VULNERABLE and False otherwise."""
        if self.sickness == 0:
            return True
        else: 
            return False

    def is_infected(self) -> bool:
        """Define a method of a Cell that returns True when the cell's sickness attribute is equal to INFECTED and False otherwise."""
        if self.sickness >= constants.INFECTED:
            return True
        else: 
            return False

    def color(self) -> str:
        """The color of a Cell."""
        if self.is_infected():
            return "orange"
        if self.is_vulnerable():
            return "gray"
        if self.is_immune():
            return "pink"

    def contact_with(self, other_cell: Cell) -> None:
        """A method that will be called when two Cell objects do make contact."""
        if self.is_vulnerable() and other_cell.is_infected():
            self.contract_disease()
        if self.is_infected() and other_cell.is_vulnerable():
            other_cell.contract_disease()

    def immunize(self) -> None:
        """A method to Cell that assigns the constant IMMUNE to the sickness attribute of the Cell."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """A method to Cell that returns True when the Cell object's sickness attribute is equal to the IMMUNE constant."""
        if self.sickness == constants.IMMUNE:
            return True
        else: 
            return False
        

class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, num_of_infected: int, num_of_immune: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if num_of_infected >= cells:
            raise ValueError
        if num_of_infected <= 0:
            raise ValueError("Some number of the Cell objects must begin infected.")
        if num_of_immune > cells:
            raise ValueError
        if num_of_immune < 0:
            raise ValueError
        for _ in range(cells - num_of_infected - num_of_immune):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
        for _ in range(num_of_infected):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
            cell.contract_disease()
        for _ in range(num_of_immune):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            self.population.append(cell)
            cell.immunize()

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        result: list[bool] = []
        for cell in self.population:
            if cell.is_infected():
                result.append(False)
            else: 
                result.append(True)
        if False in result:
            return False
        else:
            return True

    def check_contacts(self) -> None:
        """Tests whether any two Cell values come in “contact” with one another."""
        i: int = 0
        while i < len(self.population):
            idx: int = i + 1
            while idx < len(self.population):
                if self.population[i].location.distance(self.population[idx].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[idx])
                idx = idx + 1
            i = i + 1