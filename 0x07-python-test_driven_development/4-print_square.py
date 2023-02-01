#!/usr/bin/python3
"""
 This Module prints a square
"""


def print_square(size):
    """
    This function prints a square of hashes ``#``
    Args:
        size(int): The size of ``#`` to be printed
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size == None:
        raise TypeError("missing one argument")

    for i in range(size):
        for j in range(size):
            print("{}".format('#'), end="")
        print()
