#!/usr/bin/python3
"""return an object reprepsented by json str"""
import json


def from_json_string(my_str):
    """switch str to object"""
    return json.loads(my_str)
