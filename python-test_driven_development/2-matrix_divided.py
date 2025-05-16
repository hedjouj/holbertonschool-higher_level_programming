#!/usr/bin/python3
"""
This module defines a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div, rounded to 2 decimal places.

    Args:
        matrix: list of lists of integers or floats.
        div: number (int or float) to divide by.

    Returns:
        A new matrix with each element divided by div.

    Raises:
        TypeError: if matrix is not a list of lists of integers/floats.
        TypeError: if each row of the matrix is not the same size.
        TypeError: if div is not a number.
        ZeroDivisionError: if div is 0.

    Examples:
    >>> matrix_divided([[1, 2], [3, 4]], 2)
    [[0.5, 1.0], [1.5, 2.0]]
    >>> matrix_divided([[3.3, 5.7], [6.3, 1.2]], 3)
    [[1.1, 1.9], [2.1, 0.4]]
    >>> matrix_divided([[1, 2, 3]], 3)
    [[0.33, 0.67, 1.0]]
    >>> matrix_divided([[1, 2], [3]], 2)
    Traceback (most recent call last):
        ...
    TypeError: Each row of the matrix must have the same size
    >>> matrix_divided([[1, 'a']], 2)
    Traceback (most recent call last):
        ...
    TypeError: matrix must be a matrix (list of lists) of integers/floats
    >>> matrix_divided([[1, 2]], "2")
    Traceback (most recent call last):
        ...
    TypeError: div must be a number
    >>> matrix_divided([[1, 2]], 0)
    Traceback (most recent call last):
        ...
    ZeroDivisionError: division by zero
    """
    if (not isinstance(matrix, list) or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists)of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(item / div, 2) for item in row] for row in matrix]
