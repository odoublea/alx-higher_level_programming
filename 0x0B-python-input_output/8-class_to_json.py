#!/usr/bin/python3

"""Class to JSON module."""


def class_to_json(obj):
    """This function returens a dictionary description with
    simple data structure (list, dictionary, string, integer
    and boolean) for JSON serialization of an object.
    Args:
        obj(an instance of a Class)
    """
    return obj.__dict__
