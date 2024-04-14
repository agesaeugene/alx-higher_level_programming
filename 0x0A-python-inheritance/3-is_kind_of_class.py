#!/usr/bin/python3
"""class and inherited class function is defined."""

def is_kind_of_class(obj, a_class):
    """Determine whether an object is a class instance or an instance that was inherited.

    Args:
        obj (any): The object to be checked.
        a_class (type): Type of objrct to be matched by class

    Returns:
        inherited instance of a_class - True
        Otherwise - False
    """
    if isinstance(obj, a_class):
        return True
    return False
