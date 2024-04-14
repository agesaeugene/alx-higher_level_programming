#!/usr/bin/python3
# 6-from_json_string.py
"""JSON-to-object function is defined."""
import json


def from_json_string(my_str):
    """Python object representation of a JSON string is returned."""
    return json.loads(my_str)
