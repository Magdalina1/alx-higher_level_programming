#!/usr/bin/python3
"""
A class that defines a rectangle
"""


class Rectangle:
    """
    Represents a rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the rectangle class
        Args:
            width (int): Represents the width of the rectangle
            height (int): Represents the height of the rectangle
        Raises:
            TypeError: if width or height is not an integer
            ValueError: if width or height is less than zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width attribute"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height attribute"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints a diagram of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ""
        res = ""
        for i in range(self.__height):
            for j in range(self.__width):
                res += "#"
            if i != self.__height - 1:
                res += "\n"
        return res

    def __repr__(self):
        """Returns a string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Deletes the rectangle and prints a message"""
        print("Bye rectangle...")
