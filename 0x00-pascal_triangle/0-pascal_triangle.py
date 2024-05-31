#!/usr/bin/python3

"""
Module to implement a pascal triangle
"""


def pascal_triangle(n):
    """
    Function to return a list of lists of integers representing the
    Pascal’s triangle of n

    Args:
        n (int): The number of rows to generate for Pascal's Triangle

    Returns:
        List[List[int]]: List of lists representing Pascal’s Triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle