#!/usr/bin/python3
"""class checking function is defined."""

def is_same_class(obj, a_class):
    """An object is checked if it is an instance of a given class

    Args:
        obj (any): Object to be checked
        a_class (type):  Type of object to be matched by the class.
    Returns:
        when object is an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
