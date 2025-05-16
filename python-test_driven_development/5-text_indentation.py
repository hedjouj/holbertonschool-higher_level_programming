#!/usr/bin/python3
"""
This module is function that prints a text with 2 lines after '.', '?' and ':'.
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after '.', '?' and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[:i + 1].strip())
            print()
            text = text[i + 1:]
            i = 0
        else:
            i += 1
    if text.strip():
        print(text.strip())
