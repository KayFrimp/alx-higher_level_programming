#!/usr/bin/python3

"""Square Class Defined"""


class Square:
    """A class representing a square.

    Attributes:
        size (int): The length of the square.

    """

    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size (int): The length of the square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size


    def area(self):
        """Calculates area of Square

        Returns:
            int: current square area

        """
        return self.__size ** 2
