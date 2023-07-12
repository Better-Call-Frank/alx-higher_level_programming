#!/usr/bin/python3
"""Reads from standard input and computes metrics.

import sys

def print_statistics(file_size_dict, status_code_dict):
    """
    Prints the computed statistics for the given file size and status code dictionaries.

    Args:
        file_size_dict (dict): Dictionary containing the file size statistics.
        status_code_dict (dict): Dictionary containing the status code statistics.

    Returns:
        None
    """
    total_size = sum(file_size_dict.values())
    print(f"Total file size: {total_size}")

    for status_code in sorted(status_code_dict.keys()):
        count = status_code_dict[status_code]
        print(f"{status_code}: {count}")

def compute_metrics():
    """
    Reads input from stdin line by line, computes metrics, and prints statistics every 10 lines
    or after a keyboard interruption (CTRL + C).

    Returns:
        None
    """
    file_size_dict = {}
    status_code_dict = {}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            line = line.strip()

            # Parse the line and extract file size and status code
            parts = line.split()
            if len(parts) >= 7:
                file_size = int(parts[-1])
                status_code = parts[-2]

                # Update file size dictionary
                file_size_dict[line_count] = file_size

                # Update status code dictionary
                status_code_dict[status_code] = status_code_dict.get(status_code, 0) + 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(file_size_dict, status_code_dict)

    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        print_statistics(file_size_dict, status_code_dict)

if __name__ == "__main__":
    compute_metrics()
