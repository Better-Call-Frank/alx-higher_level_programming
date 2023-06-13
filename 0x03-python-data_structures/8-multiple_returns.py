#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(sentence):
    """Returns the length of a string and its first character."""
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
