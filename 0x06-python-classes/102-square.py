#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class represents a square with private instance attribute: size"""

    def __init__(self, size=0):
        """Initializes the square with the given size"""
        self.size = size

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def __eq__(self, other):
        """Comparison operator: ==
        Checks if the area of self is equal to the area of other"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Comparison operator: !=
        Checks if the area of self is not equal to the area of other"""
        return self.area() != other.area()

    def __gt__(self, other):
        """Comparison operator: >
        Checks if the area of self is greater than the area of other"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Comparison operator: >=
        Checks if area of self is greater than or equal to the area of other"""
        return self.area() >= other.area()

    def __lt__(self, other):
        """Comparison operator: <
        Checks if the area of self is less than the area of other"""
        return self.area() < other.area()

    def __le__(self, other):
        """Comparison operator: <=
        Checks if area of self is less than or equal to the area of other"""
        return self.area() <= other.area()
