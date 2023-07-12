#!/usr/bin/python3
"""Defines a from_json_string function."""
import json

def from_json_string(my_str):
    """
    Returns a Python object represented by a JSON string.

    Args:
        my_str (str): The JSON string representing the object.

    Returns:
        object: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
