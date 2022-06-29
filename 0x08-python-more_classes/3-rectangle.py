#!/usr/bin/python3

"""A class Rectangle"""


class Rectangle:
    """A Rectangle class that checks the height and width of a Rectangle

    Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        r_area = self.__width * self.__height
        return r_area

    def perimeter(self):
        r_perimeter = 2 * (self.__width + self.__height)
        if self.__width == 0 or self.__height == 0:
            r_perimeter = 0
        return r_perimeter

    def __str__(self):
        """function that prints a rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end="")
            if i != self.__height - 1:
                print()
        return ""
