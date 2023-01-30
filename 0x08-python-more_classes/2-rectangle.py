#!/usr/bin/python3

"""This is a rectangle module."""


class Rectangle:
    """A class for rectangle with height and width

       Properties:
           height(int): length
           width(int): breadth
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the rectangle area."""
        rectangle_area = self.__height * self.__width
        return rectangle_area

    def perimeter(self):
        """Return the rectangle perimeter."""
        if self.__height == 0 or self.__width == 0:
            rectangle_perimeter = 0
        rectangle_perimeter = 2 * (self.__height + self.__width)
        return rectangle_perimeter
