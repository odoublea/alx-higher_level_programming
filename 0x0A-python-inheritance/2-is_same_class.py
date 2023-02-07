#!/usr/bin/python3

"""
    This function checks if an object is exactly an instance of the specified class
"""


def is_same_class(obj, a_class):
    """This functions matches their exact class"""
    if type(obj) == a_class:
        return True
    return False