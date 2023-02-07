#!/usr/bin/python3

"""My integer module."""


class MyInt(int):
    """This is a rebel int class"""
    def __eq__(self, value):
        """changes the equal to not equal"""
        return super().real != value

    def __ne__(self, value):
        """changes not equal to equal"""
        return super().real == value
