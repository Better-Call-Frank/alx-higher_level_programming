#!/usr/bin/python3
"""Defines a load_from_json_file function."""
import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    Args:
        filename (str): The name of the JSON file.

    Returns:
        object: The object created from the JSON file.
    """
    with open(filename, "r", encoding="utf-8") as file:
        json_data = file.read()
        obj = json.loads(json_data)
    return obj
