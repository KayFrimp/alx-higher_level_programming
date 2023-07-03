#!/usr/bin/python3
"""More Classes"""


class Rectangle:
    """An empty class Rectangle

    Attributes:
    width (int): The width of the rectangle
    height (int): Rectangle height

    """

    def __init__(self, width=0, height=0):
        """Initializes an instance of Rectangle.

        Args:
        width (int): Rectangle width
        height (int): Rectangle height

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves Rectangle width

        Returns:
        int: Rectangle width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Sets Rectangle width

        Args:
        value (int): New width value

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves Rectangle height

        Returns:
        int: Rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Sets Rectangle height

        Args:
        value (int): New height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
