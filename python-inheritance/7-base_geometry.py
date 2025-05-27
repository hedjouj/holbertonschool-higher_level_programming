#!/usr/bin/python3
"""Write an empty class Basegeometry
"""


class BaseGeometry:
    """BaseGeometry class with integer_validator method."""

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
