#!/usr/bin/python3

"""
    This function checks if an object is an instance
    of the specified class
"""


def is_kind_of_class(obj, a_class):
    """This functions checks if an object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class.
    """
    if isinstance(obj, a_class):
        return True
    return False
