#!/usr/bin/python3

"""This is a rectangle module."""


class Rectangle:
    """A class for rectangle with height and width

       Args:
           width: breadth
           height: length
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    """Get width of the rectangle."""
    def width(self):
        return self.__width

    @width.setter
    """Set rectangle width."""
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
    """Get height of the rectangle."""
        return self.__height

    @height.setter
    """Set rectangle width"""
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
