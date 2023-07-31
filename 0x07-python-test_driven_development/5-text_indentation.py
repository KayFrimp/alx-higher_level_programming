#!/usr/bin/python3
"""5-text_indentation module"""


def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters:
    ., ? and :

    Arguments:
        text (str): Text to perform operation on

    Raises:
        TypeError if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")

    lines = [line.strip() for line in text.split('\n')]
    indented_text = "\n".join(lines)
    print(indented_text, end="")
