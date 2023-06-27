#!/usr/bin/python3
"""This module defines a class Square"""


class Square:
    """This class represents a square with private instance attribute: size"""

    def __init__(self, size=0):
        """Initializes the square with the given size"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
