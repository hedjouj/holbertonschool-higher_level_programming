#!/usr/bin/python3
"""Write an empty class Basegeometry
"""


class BaseGeometry:
    """classe pour forme géométrique
    """

    def integer_validator(self, name, value):
        """validate the value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
