#!/usr/bin/python3

if __name__ == "__main__":
    """print number of and list of arguments."""
    import sys

num_args = len(sys.argv) - 1
args_list = sys.argv[1:]

print("Number of argument(s):", num_args)

if num_args == 0:
    print(".", end="\n")
else:
    print(":", end="\n")
    for i, arg in enumerate(args_list, start=1):
        print(i, ":", arg)
