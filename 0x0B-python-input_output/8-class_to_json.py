#!/usr/bin/python3
"""class_to_json Module"""
import json


def class_to_json(obj):
    """Returns JSON serialization of an object
    """

    return json.dumps(vars(obj))
