#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of size n.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list: List of lists representing Pascal's triangle.

    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        previous_row = triangle[i - 1]

        for j in range(1, i):
            row.append(previous_row[j - 1] + previous_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
