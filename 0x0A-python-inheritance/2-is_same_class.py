#!/usr/bin/python3

"""Sub-class checking function"""


def is_same_class(obj, a_class):
    """Checks if an object is an instance of a class

    Args:
        obj(any): Object of class to check
        a_class (class): The class to check in
    """
    if type(obj) == a_class:
        return True
    else:
        return False
