#!/usr/bin/python3

"""Method that checks an object"""


def inherits_from(obj, a_class):
    """Function that checks if an object is an instance
        of a class inherited directly or indirectly

    Args:
        obj(any): object to check
        a_class(class): class to check in"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
