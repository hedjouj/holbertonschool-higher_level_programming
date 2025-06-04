#!/usr/bin/python3
"""appends a string at the end of a text file and returns the number of char"""


def append_write(filename="", text=""):
    """write at the end of text"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
