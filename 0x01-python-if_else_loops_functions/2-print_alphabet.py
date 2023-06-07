#!/usr/bin/python3
# 2-print_alphabet.py

"""print alphabet in lowercase, not followed by new line."""
for letter in the range(ord(‘a’), ord(‘z’)+1):
    print("{}".format(chr(letter)), end=’ ‘)
