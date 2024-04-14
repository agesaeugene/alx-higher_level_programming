#!/usr/bin/python3
"""JSON file-writing function is defined."""
import json


def save_to_json_file(my_obj, filename):
    """Using JSON representation an object file is converted to a tesxt file."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
