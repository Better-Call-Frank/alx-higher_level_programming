#!/usr/bin/python3
"""Module that contains a function to find the maximum integer in a list.
"""


def max_integer(lst=[]):
    """Find and return the maximum integer in a list of integers.
    
    If the list is empty, the function returns None.
    """
    if len(lst) == 0:
        return None
    
    max_num = lst[0]
    i = 1
    while i < len(lst):
        if lst[i] > max_num:
            max_num = lst[i]
        i += 1
    
    return max_num
