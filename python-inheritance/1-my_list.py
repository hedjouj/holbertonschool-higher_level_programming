#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """A subclass of list with a method to print the list sorted."""

    def print_sorted(self):
        sorted = self.copy()
        sorted.sort()
        print(sorted)
