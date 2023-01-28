#!/usr/bin/python3
"""
    This module holds the function that returns the quotient of
    a matrix (list of lists) division


    """


def matrix_divided(matrix, div):
    """
    Returns the quotient of a matrix (list of lists) division
    """

    if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
    result = []
    for row in matrix:
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        return result.append(int(i) / int(div))
