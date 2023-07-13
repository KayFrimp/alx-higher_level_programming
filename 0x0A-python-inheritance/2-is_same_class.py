#!/usr/bin/python3
"""Module checks for class instance"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class

    Args:
       obj (object): Any object
       a_class (class): class

    Returns:
       boolean: True of False
    """

    if type(obj) is a_class:
        return True
    return False
