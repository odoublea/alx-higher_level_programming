#!/usr/bin/python3

"""
    In this module, there is a class that inherits from a list class.
    """


class MyList(list):
    """This class inherits attributes from the superclass list."""

    def print_sorted(self):
        print(sorted(self))
