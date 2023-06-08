#!/usr/bin/python3

if __name__ == "__main__":
    """print addition of all arguments."""
    import sys

    sum_result = 0
    for i in range(len(sys.argv) - 1):
        sum_result += int(sys.argv[i + 1])
    print("{}".format(sum_result))
