#!/usr/bin/python3
"""This module contains a fucntion that rotatesa 2D matrix by 90 degrees"""


def rotate_2d_matrix(matrix) -> None:
    """a function that rotates a 2D matrix"""

    if type(matrix) != list:
        return
    if len(matrix) < 1:
        return
    for row in matrix:
        if type(row) != list:
            return

    first_list_length = len(matrix[0])

    # Check the lengths of the remaining lists
    for sublist in matrix:
        if len(sublist) != first_list_length:
            return

    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()
