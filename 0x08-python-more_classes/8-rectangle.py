#!/usr/bin/python3

"""A class Rectangle"""


class Rectangle:
    """A Rectangle class that checks the height and width of a Rectangle

    Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
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
                print(self.print_symbol, end="")
            if i != self.__height - 1:
                print()
        return ""

    def __repr__(self):
        Rectangle.number_of_instances += 1
        inst = ("Rectangle({}, {})".format(self.__width, self.__height))
        return inst

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.__width * rect_1.__height
        area2 = rect_2.__width * rect_2.__height

        if area1 == area2:
            return rect_1
        elif area1 > area2:
            return rect_1
        else:
            return rect_2
