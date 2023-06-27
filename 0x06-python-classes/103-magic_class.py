#!/usr/bin/python3
"""This module defines a class Square"""


import math


class MagicClass:
    """This class represents a MagicClass with a private
    instance attribute: radius."""

    def __init__(self, radius=0):
        """Initializes the MagicClass with the given radius.
        Args:
            radius (float): The radius of the MagicClass circle. Default is 0.
        Raises:
            TypeError: If the radius is not a number.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculates and returns the area of the MagicClass circle.
        Returns:
            float: The area of the MagicClass circle.
        """
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Calculates and returns the circumference of the MagicClass circle.
        Returns:
            float: The circumference of the MagicClass circle.
        """
        return 2 * math.pi * self.__radius
