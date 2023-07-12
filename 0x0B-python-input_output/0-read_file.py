#!/usr/bin/python3
"""read_file module"""


def read_file(filename=""):
    """Prints contents of a file to stdout

    args:
    filename (file): The txt file.
    """

    with open(filename, encoding="utf-8") as myFile:
        while True:
            line = myFile.readline()
            if not line:
                break
            print(line, end="")
