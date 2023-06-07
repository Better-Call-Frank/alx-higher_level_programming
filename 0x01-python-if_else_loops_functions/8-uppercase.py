#!/usr/bin/python3
# 8-uppercase.py


def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - 32)), end="")
        else:
            print("{}".format(c), end="")
    print()  # Print a new line at the end
