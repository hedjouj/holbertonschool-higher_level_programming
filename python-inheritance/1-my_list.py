#!/usr/bin/python3
"""list inherits from list"""


class MyList(list):
    """
    a subclass of list
    """

    def print_sorted(self):
        """
        print the list in ascending
        """
        print(sorted(self))