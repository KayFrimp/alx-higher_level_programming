#!/usr/bin/python3
"""More Classes"""


class Rectangle:
    """An empty class Rectangle

    Attributes:
    width (int): The width of the rectangle
    height (int): Rectangle height"""

    # Class variables

    # Keeps record of instances created
    number_of_instances = 0
    # Symbol for string representation
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes an instance of Rectangle.

        Args:
        width (int): Rectangle width
        height (int): Rectangle height

        """
        self.width = width
        self.height = height

        # For every instance created, count
        Rectangle.number_of_instances += 1

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

    def area(self):
        """Calculates Rectangle area

        Returns:
        int: Area of Rectangle

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of Rectangle

        Returns:
        int: Perimeter of Rectangle

        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints Rectangle with #"""
        rect = ''
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(self.__height):
            rect += (str(self.print_symbol) * self.__width) + '\n'
        return rect[:-1]

    def __repr__(self):
        """Return string representation of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Executes when an instance is deleted"""

        # For every instance destroyed, decrement number_of_instances
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two instances of Rectangle

        args:
        rect_1 (Rectangle): An instance of Rectangle
        rect_2 (Rectangle): Another instance of Rectangle

        returns:
        Rectangle: First Instance if equal or the bigger instance
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance

        args:
        size (int): width and height of Rectangle

        returns:
        Rectangle: Rectangle object
        """
        return cls(size, size)
