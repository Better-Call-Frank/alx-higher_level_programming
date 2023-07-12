#!/usr/bin/python3
"""Defines a class_to_json_file function."""

def class_to_json(obj):
    """
    Returns a dictionary description of an object with a simple data structure suitable for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: A dictionary representation of the object suitable for JSON serialization.
    """
    json_dict = {}
    
    # Iterate over all attributes of the object
    for attr_name in dir(obj):
        # Exclude special attributes and methods
        if not attr_name.startswith("__") and not callable(getattr(obj, attr_name)):
            attr_value = getattr(obj, attr_name)
            
            # Check if the attribute is a simple data type (list, dict, str, int, bool)
            if isinstance(attr_value, (list, dict, str, int, bool)):
                json_dict[attr_name] = attr_value
    
    return json_dict
