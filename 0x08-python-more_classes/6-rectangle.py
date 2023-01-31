#!/usr/bin/python3

"""This is a rectangle module."""


class Rectangle:
    """A class for rectangle with height and width

       Args:
           width: breadth
           height: length
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width."""
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
    def height(self, value):
        """Set rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
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

    def __str__(self):
        """Print rectangle hashes."""
        if self.__height == 0 or self.__width == 0:
            return ''
        for i in range(self.__height):
            for j in range(self.__width):
                print("{}".format('#'), end="")
            if i != (self.__height - 1):
                print()

        return ''

    def __repr__(self):
        Rectangle.number_of_instances += 1
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
