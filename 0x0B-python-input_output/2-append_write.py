#!/usr/bin/python3
"""File appending function is defined"""


def append_write(filename="", text=""):
    """
    A string  is appended to the end of a UTF8 text file.

    Args:
        filename (str): Filename to append to
        text (str): File to be appended to by string
    Returns:
        Number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
