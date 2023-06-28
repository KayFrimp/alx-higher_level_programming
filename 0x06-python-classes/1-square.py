#!/usr/bin/python3

"""Square Class Defined"""


class Square:
    """An empty class that defines a square.

    Args:
     __size (int): Length of square.

    """

    def __init__(self, size=None):
        """Initializes the data

        Attributes:
        size: Length of square

        """
        if size is not None:
            self.__size = size
