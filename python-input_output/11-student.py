#!/usr/bin/python3
"""define a student with seri/deserialization"""


class Student:
    """Defines a student with serialization/deserialization."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns dictionary representation (filtered if attrs is a list)."""
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Updates attributes from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
