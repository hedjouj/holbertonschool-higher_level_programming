#!/usr/bin/python3
"""return the dictionnary description with simple data"""
import json


def class_to_json(obj):
    """save class to json rep"""
    return json.dumps(obj.__dict__)
