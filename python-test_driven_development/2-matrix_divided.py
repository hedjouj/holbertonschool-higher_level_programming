#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number

    Args:
        matrix (list): list of lists of integers or floats
        div (int/float): the divisor

    Returns:
        list: a new matrix with all elements divided and rounded to 2 decimals

    Raises:
        TypeError: if matrix is not a list of lists of int/float
        TypeError: if rows are not of the same size
        TypeError: if div is not a number
        ZeroDivisionError: if div is zero
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(
        all(isinstance(x, (int, float)) for x in row) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(element / div, 2) for element in row] for row in matrix
    ]
