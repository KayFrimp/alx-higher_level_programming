#!/usr/bin/python3
"""4-print_square module"""


def print_square(size):
    """Prints square with '#' character

    Arguments:
        size (int): length of size of square

    Raises:
        TypeError:
            1. If size is not an integer
        ValueError:
            2. If size is less than 0
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
