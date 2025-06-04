#!/usr/bin/python3
"""return json of an object"""
import json


def to_json_string(my_obj):
    """return the json represetation of an object"""
    json_str = json.dumps(my_obj)
    print(json_str)
