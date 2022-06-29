#!/usr/bin/python3

"""Locked class method"""


class LockedClass:
    """A class that prevents users new instance attribute except first_name"""
    __slots__ = ["first_name"]
