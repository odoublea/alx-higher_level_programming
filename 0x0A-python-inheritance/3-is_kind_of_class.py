#!/usr/bin/python3

"""Method that checks a class object"""


def is_kind_of_class(obj, a_class):
    """a function that returns True if the object is an instance of,
            or if the object is an instance of a class that inherited from,
                the specified class ; otherwise False
    Args:
    obj(any): Object to check
    a_class(class): class to check in
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
