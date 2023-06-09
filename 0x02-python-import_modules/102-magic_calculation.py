#!/usr/bin/python3


def magic_calculation(a, b):
    """match the bytecode provided by Holberton."""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for number in range(4, 6):
            c = add(c, number)
        return (c)

    else:
        return(sub(a, b))

