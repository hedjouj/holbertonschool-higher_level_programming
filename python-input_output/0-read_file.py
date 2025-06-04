#!/usr/bin/python3
"""a fonction that read a file using with"""


def read_file(filename=""):
    """read a file"""

    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
