#!/usr/bin/python3
# 6-print_comb3.py

"""Prints all possible different combinations of two digits.

    The two digits must be different, 01 and 10 are considered identical.
    """
for i in range(10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print("{}{}".format(i, j), end=", ")
