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
        if len(row) < 1:
            return

    matrix.reverse()
    row1 = [each for row in matrix for each in row if row.index(each) == 0]
    row2 = [each for row in matrix for each in row if row.index(each) == 1]
    row3 = [each for row in matrix for each in row if row.index(each) == 2]
    matrix.clear()
    matrix.append(row1)
    matrix.append(row2)
    matrix.append(row3)
