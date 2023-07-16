#!/usr/bin/python3
# 0-add_integer.py
"""Defines a function for adding integers."""


def add_integer(a, b=98):
    """Return the sum of two integers, a and b.

    If either a or b is a float, it is converted to an integer before addition.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
