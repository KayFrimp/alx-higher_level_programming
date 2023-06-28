#!/usr/bin/python3

"""Square Class Defined"""


class Square:
    """An empty class that defines a square.

    Args:
    size (int): Length of square.

    """

    def __init__(self, size=0):
        """Initializes the data

        Attributes:
        size: Length of square

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be an integer")
        else:
            self.__size = size
