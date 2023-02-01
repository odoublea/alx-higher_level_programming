#!/usr/bin/python3
"""
    This module holds the function that returns the quotient of
    a matrix (list of lists) division


    """


def matrix_divided(matrix, div):
    """
    This function takes a matrix (list of lists) and a divisor as input and
    returns the divided matrix.
    Each element of the matrix is divided by the divisor and rounded to 2
    decimal places.

    Args:
        matrix (list of lists): The dividend
        div: the divisor
    """

    if not isinstance(matrix, list) or not all(isinstance(i, list) for i in
                                               matrix) or not any(matrix):
        raise TypeError("""matrix must be a matrix (list of lists)
                        of integers/floats""")

    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("""matrix must be a matrix (list of lists)
                        of integers/floats""")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(i / div, 2) for i in row] for row in matrix]
