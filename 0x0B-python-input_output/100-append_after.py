#!/usr/bin/python3
"""Defines a text file insertion function."""

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text into a file after each line containing a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line of the file.
        new_string (str): The line of text to insert after each line containing the search string.

    Returns:
        None
    """
    with open(filename, "r+") as file:
        lines = file.readlines()
        file.seek(0)  # Move the file pointer to the beginning

        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)

        file.truncate()  # Truncate the remaining content if the new lines are shorter than the original lines
