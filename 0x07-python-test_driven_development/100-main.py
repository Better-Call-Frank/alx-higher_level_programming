#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

# Example 1
matrix_1 = [[1, 2], [3, 4]]
matrix_2 = [[1, 2], [3, 4]]
result_1 = matrix_mul(matrix_1, matrix_2)
print(result_1)

# Example 2
matrix_3 = [[1, 2]]
matrix_4 = [[3, 4], [5, 6]]
result_2 = matrix_mul(matrix_3, matrix_4)
print(result_2)
