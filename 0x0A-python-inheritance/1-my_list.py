#!/usr/bin/python3
"""Defines an inherited list class MyList."""

class  MyList(list):
    """for the builtin list-class sorted rinting is implemented"""

    def print_sorted(self):
        """list in a sorted ascending order is printed."""
        print(sorted(self))
