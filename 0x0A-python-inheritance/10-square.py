#!/usr/bin/python3
"""
This module contains a class Square
that inherits from Rectangle
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a class Square
    """

    def __init__(self, size):
        """
        This is the Constructor method of Square
        """
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        This method returns the square area
        """
        return self.__size ** 2

    def __str__(self):
        """
        This method returns the Square description
        """
        return("[Rectangle] {}/{}".format(self.__size, self.__size))
