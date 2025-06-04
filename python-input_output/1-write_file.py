#!/usr/bin/python3
"""a function that print nb of char"""


def write_file(filename="", text=""):
    """writes a string to a text file and returns the numbers of char"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
