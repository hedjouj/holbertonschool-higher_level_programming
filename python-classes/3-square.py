#!/usr/bin/python3
"""Module 3-square
Défini un carré base on 2-square
"""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        """Initialize a square with optional size.
        Args:
        size int: size of the square, must be a non negative integer.
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate the area of the square.
        Returns:
            int: the area of the square.
        """
        return self.__size ** 2
