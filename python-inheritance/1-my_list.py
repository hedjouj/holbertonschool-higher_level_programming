#!/usr/bin/python3
"""Module that defines a MyList class inheriting from list."""


class MyList(list):
    """A subclass of list with a method to print the list sorted."""

    def print_sorted(self):
        """Prints the list in ascending sorted order (does not modify the list)."""
        print(sorted(self))
