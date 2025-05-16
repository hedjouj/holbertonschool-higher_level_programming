#!/usr/bin/python3
"""
Module that defines a function to indent text after '.', '?' and ':'
"""


def text_indentation(text):
    """
    Prints text with 2 new lines after each '.', '?', and ':'

    Args:
        text (str): the text to format

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            # Skip any spaces after punctuation
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
