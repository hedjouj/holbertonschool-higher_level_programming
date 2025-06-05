#!/usr/bin/python3
"""define a stud with filtering for json serialization"""


class Student:
    """Defines a student with filtering for JSON serialization."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary of attributes; filters if attrs is a list of strings."""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
