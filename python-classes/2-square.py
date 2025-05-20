#!/usr/bin/python3
"""un carré
Defines a Square class with size validation.
"""


class Square:
    """Représente un carré basé sur lexo 1."""
    def __init__(self, size=0):
        """Initializes the square with a size.

         Args:
         size (int): la taille du carré ne doit pas être un entier négatif.

         Raises:
         TypeError: If size is not an integer.
         ValueError: If size is less than 0.
         """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
