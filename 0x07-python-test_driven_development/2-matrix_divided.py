#!/usr/bin/python3
"""
This module contains the function that 
divideds every number in the matrix by a base number
"""


def matrix_divided(matrix, div) -> list:
    """Divide all elements of a matrix

    Arguemnts:
        matrix(a list) of ints or floats)
        div (int/float) that divides throuth the list


    Returns
         list of the dividends
    """
    index = len(matrix[0])
    for mat in matrix:
        if len(mat) != index:
            raise TypeError("matrix must have each row with the same size")

    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []

    for r in range(len(matrix)):
        if type(matrix[r]) is not list:
            raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

        if r > 0 and len(matrix[r]) != len(matrix[r-1]):
            raise TypeError("matrix must have each row with the same size")

        new_matrix.append([])
        for n in matrix[r]:
            if type(n) not in [float, int]:
                raise TypeError("matrix must be a matrix \
(list of lists) of integers/floats")

            new_matrix[r].append(round(n/div, 2))
    return new_matrix
