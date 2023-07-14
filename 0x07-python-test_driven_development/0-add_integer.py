#!/usr/bin/python3
"""
Integer addition module
"""


def add_integer(a, b=98):
    """Adds two(2) integers

    args:
        a (int): Integer value a
        b (int): Integer value b defaults to 98

    returns:
        int: Sum of a and b

    """

    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")

    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")

    return a + b
