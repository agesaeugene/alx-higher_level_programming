#!/usr/bin/python3
"""python class-to-JSON function."""


def class_to_json(obj):
    """A dictionary representation of a simple data structure is returned."""
    return obj.__dict__
