#!/usr/bin/python3
"""BaseGeometry Class module"""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """Not yet implemented"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value

        Raises:
            TypeError if value is not an integer
            ValueError if value is less or equal to 0
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
