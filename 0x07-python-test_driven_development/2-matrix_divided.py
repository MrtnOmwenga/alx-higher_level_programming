#!/usr/bin/python3
"""
Divides every component of the matrix by a number
Every element of matrix must be int or float
Each row must be the same size
div mut be an integer or float
Result must be rounded to 2 decimal places
"""


def matrix_divided(matrix, div):
    """Divides matrix by div"""

    """Check div"""
    if div is None:
        raise TypeError("div must be a number")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    """Check matrix"""
    if matrix is None:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
    for element in matrix:
        if type(element) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")
        if len(element) != len(matrix[0]):
            raise TypeError("Each row of the matrix \
must have the same size")
        for item in element:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    """Result"""
    result = []
    for i in range(len(matrix)):
        result.append([])
        for j in range(len(matrix[i])):
            result[i].append(float(matrix[i][j]) / div)
            result[i][j] = round(result[i][j], 2)

    return (result)
