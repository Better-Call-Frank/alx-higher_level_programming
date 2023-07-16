#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if len(m_a) == 0 or any(not isinstance(row, list) for row in m_a):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or any(not isinstance(row, list) for row in m_b):
        raise ValueError("m_b can't be empty")

    if not isinstance(m_a, list) or any(
            not all(isinstance(ele, int) or isinstance(ele, float) for ele in row)
            for row in m_a):
        raise TypeError("m_a must be a list of lists of integers or floats")

    if not isinstance(m_b, list) or any(
            not all(isinstance(ele, int) or isinstance(ele, float) for ele in row)
            for row in m_b):
        raise TypeError("m_b must be a list of lists of integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must have the same size")

    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must have the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    inverted_b = [[m_b[c][r] for c in range(len(m_b))] for r in range(len(m_b[0]))]

    new_matrix = []
    for row in m_a:
        new_row = []
        for col in inverted_b:
            prod = sum(row[i] * col[i] for i in range(len(col)))
            new_row.append(prod)
        new_matrix.append(new_row)

    return new_matrix
