#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Create a new matrix of the same size as the input matrix
    result = [[0 for _ in row] for row in matrix]

    # Iterate over each element in the input matrix and compute its square
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = matrix[i][j] ** 2

    return result
