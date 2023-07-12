#!/usr/bin/python3
"""class_to_json Module"""


def class_to_json(obj):
    """Returns JSON serialization of an object
    """

    return vars(obj)
