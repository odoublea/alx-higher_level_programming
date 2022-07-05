#!/usr/bin/python3

"""MyList that inherits from list"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """A function that prints a sorted list"""
        print(sorted(self))
