#!/usr/bin/python3

"""
    This script implements Pascal's triangle
"""


def pascal_triangle(n):
    """ Returns a list of list of numbers that represent Pascal's triangle """
    if (n <= 0):
        return []
    triangle = [[1]]
    for i in range(n - 1):
        row = []
        for j in range(len(triangle[i]) + 1):
            if (j - 1 < 0):
                row.append(triangle[i][j])
            elif (j == len(triangle[i])):
                row.append(triangle[i][j - 1])
            else:
                row.append(triangle[i][j] + triangle[i][j - 1])
        triangle.append(row)
    return triangle
