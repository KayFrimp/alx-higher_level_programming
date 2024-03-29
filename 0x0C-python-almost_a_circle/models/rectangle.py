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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter function for height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter function for height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter function for x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter function for x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter function for y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter function for y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """represents the rectangle with #"""
        if self.width == 0 or self.height == 0:
            return ""

        for x in range(self.y):
            print()

        for y in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        defines a a string format
        representation of the class
        """
        return (
            f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
            f"{self.__width}/{self.__height}"
        )

    def update(self, *args, **kwargs):
        """update assigns an argument to attribute"""
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
            return
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except IndexError:
            pass

    def to_dictionary(self):
        """returns the dictionary representation of a rectangle"""
        return {
            'id': self.id,
            'width': self.__width,
            'height': self.__height,
            'x': self.__x,
            'y': self.__y
        }
