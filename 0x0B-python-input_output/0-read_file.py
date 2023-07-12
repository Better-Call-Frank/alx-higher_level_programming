#!/usr/bin/python3

def read_file(filename=""):
    # Open the file in read mode with UTF-8 encoding
    with open(filename, "r", encoding="utf-8") as file:
        # Read the entire content of the file as a string
        content = file.read()

        # Print the content to stdout
        print(content)
