#!/usr/bin/python3
"""11-square module"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class definition of  a Square"""

    def __init__(self, size):
        """ Method that initializes a Square """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """ Method that returns a string with the area """
        return super().area()

    def __str__(self):
        """ Special method that returns a printable string """
        return "[Square] {}/{}".format(self.__size, self.__size)
