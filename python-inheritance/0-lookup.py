#!/usr/bin/python3
"""This module print the list of attributes/methods"""


def lookup(obj):
    """look after the object

    Args:
        obj: Any python object.

        Returns:
        list: list of names
    """
    return dir(obj)
