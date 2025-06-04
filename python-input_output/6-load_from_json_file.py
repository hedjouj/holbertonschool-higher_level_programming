#!/usr/bin/python3
"""create an object from a json file"""
import json


def load_from_json_file(filename):
    """load from a json file"""
    with open(filename, "r") as f:
        return json.load(f)
