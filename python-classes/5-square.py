#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initialise la taille du carré"""
        self.size = size

    @property
    def size(self):
        """Récupère la taille du carré"""
        return self.__size

    @size.setter
    def size(self, value):
        """Change la taille du carré avec des vérifications"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Retourne l'aire du carré"""
        return self.__size ** 2

    def my_print(self):
        """Affiche le carré avec le caractère #"""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
