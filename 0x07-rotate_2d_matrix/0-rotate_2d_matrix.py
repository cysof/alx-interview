#!/usr/bin/python3

"""
Rotate 2D Matrix

    Given an n x n 2D matrix, rotate it 90 degrees clockwise.
    For the “0. Rotate 2D Matrix” project, i am tasked with 
    implementing an in-place algorithm to rotate an n x n 2D matrix 
    by 90 degrees clockwise. This challenge requires a good understanding 
    of matrix manipulation and in-place operations in Python. 
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a 2D matrix clockwise by 90 degrees in-place.

    Parameters:
        matrix (list[list[int]]): The 2D matrix to be rotated.

    Returns:
        None: The matrix is rotated in-place.

    Raises:
        None

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> rotate_2d_matrix(matrix)
        >>> matrix
        [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """

    ziper = zip(*reversed(matrix))
    for column1, column2 in enumerate(ziper):
        matrix[column1] = list(column2)