#!/usr/bin/python3

if __name__ == "__main__":
    """print sum, difference, multiplication and division of 10 and 5."""
    from calculator_1 import add, multiply, divide, subtract

    a = 10
    b = 5

    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} * {} = {}".format(a, b, multiply(a, b)))
    print("{} / {} = {}".format(a, b, divide(a, b)))
    print("{} - {} = {}".format(a, b, subtract(a, b)))
