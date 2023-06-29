#!/usr/bin/python3

"""Square Class Defined"""


class Square:
    """A class representing a square.

    Attributes:
        size (int): The length of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a Square instance.

        Args:
            size (int): The length of the square
            position (tuple): Coordinates of Square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or
                len(position) != 2 or
                not isinstance(position[0], int) or
                not isinstance(position[1], int) or
                position[0] < 0 or position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Retrieves size of Square

        Returns:
            int: size of square

        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of Square"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves position of Square"""

        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of Square with a tuple"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates area of Square

        Returns:
            int: current square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints square with '#' character"""

        if self.__size == 0:
            print()
        else:
            if self.__position[1] > 0:
                for k in range(self.__position[1]):
                    print()
            elif self.__position[1] == 0:
                pass
            for i in range(self.__size):
                for m in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
