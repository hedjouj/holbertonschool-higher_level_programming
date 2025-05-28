#!/usr/bin/python3
""" a square with the rectangle attributes"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """un carré avec les attributs du rectangle"""
    def __init__(self, size):
        """Initialize a square"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return the area"""
        return self.__size ** 2
