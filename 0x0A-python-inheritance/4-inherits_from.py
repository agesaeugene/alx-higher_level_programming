#!/usr/bin/python3
"""An inherited class checking function is defined."""

def inherits_from(obj, a_class):
    """determines whether an object is a class instance that was inherited.

    Args:
        obj (any): Object to be checked.
        a_class (type): Class to match type of object to.
    Returns:
        For object inherited instance of a class - True.
        Otherwise - False.
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
