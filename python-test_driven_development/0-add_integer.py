#!/usr/bin/python3
"""
This module provides a function that adds two integers.

The function add_integer(a, b=98) accepts two arguments, which can be
integers or floats. If any of the arguments is not a number,
a TypeError is raised. Floats are cast to integers before addition.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number, must be an integer or float.
        b: The second number, must be an integer or float (default is 98).

    Returns:
        int: The sum of a and b as integers.

    Raises:
        TypeError: If a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
