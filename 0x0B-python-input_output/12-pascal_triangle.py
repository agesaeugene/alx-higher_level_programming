#!/usr/bin/python3
"""Pascal's Triangle function is defined."""


def pascal_triangle(n):
    """Pascal's Triangle of size n is represented.

    List of lists of integers representing the triangle is returned.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
