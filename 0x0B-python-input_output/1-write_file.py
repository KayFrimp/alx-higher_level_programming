#!/usr/bin/python3
"""write_file module"""


def write_file(filename="", text=""):
    """Writes a string to a text file

    args:
    filename (file): File to write to
    """

    with open(filename, mode="w", encoding="utf-8") as myFile:
        return myFile.write(text)
