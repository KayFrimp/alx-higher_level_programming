#!/usr/bin/python3
"""Rectangle class module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class definition"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes a Rectangle instance

        Arguments:
            width (int): width of rectangle
            height (int): height of rectangle
            x (int): x
            y (int): y
            id (int): Identification number of rectangle
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter function for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter function for width"""
        self.__width = value

    @property
    def height(self):
        """Getter function for height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for height"""
        self.__height = value

    @property
    def x(self):
        """Getter function for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function for x"""
        self.__x = value

    @property
    def y(self):
        """Getter function for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function for y"""
        self.__y = value
