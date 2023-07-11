#!usr/bin/python3
"""MyList Class Module"""


class MyList(list):
    """MyList inherits from class list"""

    def print_sorted(self):
        """Prints list in ascending order."""

        print(sorted(self))
