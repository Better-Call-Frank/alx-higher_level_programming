#!/usr/bin/python3
# 7-islower.py


def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= ord(‘a’) and ord(c) <= ord(‘z’):
        return True
    else:
        return False
