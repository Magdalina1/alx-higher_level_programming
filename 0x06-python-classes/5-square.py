#!/usr/bin/python3
"""this module defines a class square"""


class Square:
    """
    Represents a square with a size attribute.
    """

    def __init__(self, size=0):
        """
        Initializes the Square instance.

        Args:
            size (int): Size of the square. Default is 0.
        """

        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Retrieves the value of the size attribute.

        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the value of the size attribute.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #.

        If the size is equal to 0, it prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print('#' * self.__size)
