#!/usr/bin/python3
"""
returns true if the object is exactly an instance of the specified class
otherwise false
"""


def is_same_class(obj, a_class):
    """
    function that will take an object and a class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
