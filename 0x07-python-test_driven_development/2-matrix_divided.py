#!/usr/bin/python3
"""matrix_divided module"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix

    Parameters:
        matrix (list): Matrix object
        div (int/float): divisor

    Raises:
        TypeError:
            1. If matrix is not a list lists of integers or floats.
            2. If rows in matrix are unequal in size.
            3. If div is not a number(integer/float).
        ZeroDivisionError:
            Whenever div is equal to 0.

    Returns:
        list: Resulting matrix after division
    """
    if not matrix or not isinstance(matrix, list) or \
       not all(isinstance(item, int) or isinstance(item, float) for
               row in matrix for item in row):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, int) or isinstance(div, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
