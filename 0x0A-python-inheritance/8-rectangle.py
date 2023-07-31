#!/usr/bin/python3
"""8-rectangle module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class definition of a Rectangle"""

    def __init__(self, width, height):
        """Initializes a Rectangle instance.

        Arguments:
            width (int): width of rectangle
            height (int): height of rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
