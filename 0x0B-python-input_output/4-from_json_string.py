#!/usr/bin/python3
"""from_json_string module"""
import json


def from_json_string(my_obj):
    """Returns the Object representation of JSON

    args:
    my_obj (JSON): JSON string

    returns:
    object: Object representation of JSON
    """

    return json.loads(my_obj)
