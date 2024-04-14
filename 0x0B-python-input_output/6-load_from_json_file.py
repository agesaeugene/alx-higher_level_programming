#!/usr/bin/python3
"""JSON file-reading function is defined."""
import json


def load_from_json_file(filename):
    """A Python object is created from a JSON file."""
    with open(filename) as f:
        return json.load(f)
