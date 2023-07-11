#!/usr/bin/python3
def lookup(obj):
    """ Function returns the list of available attributes
        and methods of an object

    Args:
    obj: instance of the class

    Returns:
    list: List of attributes and methods of object
    """

    return dir(obj)
