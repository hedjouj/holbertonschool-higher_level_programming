#!/usr/bin/python3
"""write an object to a text file using json"""
import json


def save_to_json_file(my_obj, filename):
    """save an object to a text file using JSON representation"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
