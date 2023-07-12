#!/usr/bin/python3
"""Defines a Pascal’s Triangle function."""

def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle for a given n.

    Args:
        n (int): The number of rows to generate in Pascal's triangle.

    Returns:
        list: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
