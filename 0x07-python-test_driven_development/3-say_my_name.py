#!/usr/bin/python3
"""
    This module prints the name of a person
    """


def say_my_name(first_name, last_name=''):
    """
    Args:
        first_name: string
        last_name: string
        """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == None or first_name == '':
        raise TypeError("Missing first_name and last_name")
    print("My name is {} {}".format(first_name, last_name))
