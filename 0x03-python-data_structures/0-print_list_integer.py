#!/usr/bin/python3
# 0-print_list_integer.py


def print_list_integer(my_list=[]):
    """Prints all integers of a list."""
    for number in range(len(my_list)):
        print("{:d}".format(my_list[number]))
