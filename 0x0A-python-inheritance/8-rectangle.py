#!/usr/bin/python3
"""inherits a class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that inherits BaseGeometry class"""

    def __init__(self, width, height):
        """uses the super class function to validate width and height

        Args:
            width(int): must be int greater than 0 else error
            height(int): must be int greater than 0 else error
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
