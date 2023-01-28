#!/usr/bin/python3
"""
    This module holds the function that returns the quotient of
    a matrix (list of lists) division


    """


def matrix_divided(matrix, div):
    """
    This function takes a matrix (list of lists) and a divisor as input and returns the divided matrix.
    Each element of the matrix is divided by the divisor and rounded to 2 decimal places.
    """

    if type(matrix) != list or not all(isinstance(i, list) for i in matrix):
        raise TypeError("matrix must be a list of lists")
    # Checking if the input is a list of lists, if not raises a TypeError

    if not all(isinstance(i, (int, float)) for row in matrix for i in row):
        raise TypeError("matrix must contain only integers or floats")
    # checking if the matrix contain only integers or floats, if not raises a TypeError

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    # Checking if all the rows have the same length, if not raises a TypeError

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Checking if div is a number, if not raises a TypeError

    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Checking if div is zero, if it's the case raises a ZeroDivisionError

    return [[round(i / div, 2) for i in row] for row in matrix]
    # returning the matrix where each element is divided by div and rounded to 2 decimal places
