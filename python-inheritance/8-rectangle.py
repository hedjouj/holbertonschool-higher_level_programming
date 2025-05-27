#!/usr/bin/python3
"""reactangle"""


class BaseGeometry:
    """the parent
    """
    def area(self):
        """
        Méthode qui lève une exception pour indiquer que
        la zone n'est pas encore implémentée.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """the kid of the parent
    """
    def __init__(self, width, height):
        """instantiation
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
