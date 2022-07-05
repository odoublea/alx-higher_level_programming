#!/usr/bin/python3
"""
This module contains a function that adds
a new attribute to the onject is it is possible
"""


def add_attribute(obj, name, value):
    """
    This function adds a new attribute to the
    object if it is possible
    """
    if not hasattr(obj, '__dict__') is True:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
