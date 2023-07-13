#!/usr/bin/python3
"""inherits_from module"""


def inherits_from(obj, a_class):
    """ checks if object is an instance of a class
        that inherited from a_class

    Args:
        obj (object): Any object
        a_class (class): class

    Returns:
        boolean: True or False
    """
    if (issubclass(type(obj), a_class) and type(obj) != a_class):
        return True
    return False
