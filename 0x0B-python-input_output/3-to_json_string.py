#!/usr/bin/python3
"""to_json_string module"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of string object

    args:
    my_obj (string): string object

    returns:
    JSON: JSON representation of my_obj
    """

    return json.dumps(my_obj)
