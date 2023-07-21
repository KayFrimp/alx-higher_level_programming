#!/usr/bin/python3
"""3-say_my_name module"""


def say_my_name(first_name, last_name=""):
    """Prints: My name is <first name> <last name>

    Arguments:
        first_name (str): First name variable
        last_name (str): Last name variable
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
