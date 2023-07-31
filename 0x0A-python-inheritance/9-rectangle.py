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

        def area(self):
            """Calculates area of Rectangle

            Returns:
                int: area of rectangle
            """
            return self.__width * self.__height

        def __str__(self):
            """returns string representation of
               rectangle"""
            return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
