#!/usr/bin/python3
"""Text file-reading function is defined."""


def read_file(filename=""):
    """The contents of a UTF8 text file to stdout are printed."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

