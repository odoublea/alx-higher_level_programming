#!/usr/bin/python3
"""
This module contains a class MyInt that
inherits from int and implements
eq and ne
"""


class MyInt(int):
    """
    This is the class MyInt
    """

    def __eq__(self, item):
        """
        This method implements eq
        """
        return False

    def __ne__(self, item):
        """
        This method implements ne
        """
        return True
