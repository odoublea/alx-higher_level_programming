#!/usr/bin/python3
"""This module returns a peak in a list."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if len(list_of_integers) == 0:
        return None
    elif len(list_of_integers) == 1:
        for i in list_of_integers:
            return i
    else:
        list_of_integers.sort()
        return list_of_integers[-1]
