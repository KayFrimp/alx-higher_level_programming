#!/usr/bin/python3
"""append_write module"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file

    args:
    filename (file): File to append string
    text (string):  String to append

    returns:
    int: number of characters added
    """

    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
