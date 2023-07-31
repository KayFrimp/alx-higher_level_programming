#!/usr/bin/python3
"""Base class module"""


class Base:
    """Base Class definition

    Attributes:
        __nb_objects (int): Number of base instances
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a base instance

        Arguments:
            id (int): Identification number"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
