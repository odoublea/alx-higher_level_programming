#!/usr/bin/python3

"""
    This function checks if an object is a subclass
    of the specified class
"""


def inherits_from(obj, a_class):
    """This functions checks if an object is a of or inherits from a
    specified class.
    """
    if issubclass(type(obj), a_class):
        return obj
    return False
