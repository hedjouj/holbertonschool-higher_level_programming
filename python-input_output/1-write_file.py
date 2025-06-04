#!/usr/bin/python3


def write_file(filename="", text=""):
    """writes a string to a text file and returns the numbers of char"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
