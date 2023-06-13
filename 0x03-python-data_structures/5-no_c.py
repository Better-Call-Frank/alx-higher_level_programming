#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):
    """Removes all characters c and C from a string."""
    new_string = ""
    for char in my_string:
        if char.lower() != 'c':
            new_string += char
    return new_string
