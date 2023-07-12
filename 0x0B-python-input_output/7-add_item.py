#!/usr/bin/python3
"""Adds all arguments to a Python list, and then save them to a file."""
import sys
import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj: The object to be serialized and written to the file.
        filename (str): The name of the file to write.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)

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

# Add all arguments to a Python list
arguments = sys.argv[1:]

# Load existing list from file, if it exists
try:
    existing_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_list = []

# Append arguments to the existing list
existing_list.extend(arguments)

# Save the updated list to the file
save_to_json_file(existing_list, "add_item.json")
