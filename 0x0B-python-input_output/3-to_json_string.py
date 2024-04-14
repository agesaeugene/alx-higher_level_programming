#!/usr/bin/python3
"""string-to-JSON function is defined."""
import json


def to_json_string(my_obj):
    """JSON representation of a strings object is returned."""
    return json.dumps(my_obj)
