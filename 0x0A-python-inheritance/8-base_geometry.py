#!/usr/bin/python3

"""
    Geometry module
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a rectangle classs with attr width and height.
    It is a subclass of BaseGeometry
    
    Args:
        width(int): must be int greater than 0 else error
        height(int): must be int greater than 0 else error
    """

    def __init__(self, width, height):
        if self.integer_validator("width", width)\
           and self.integer_validator("height", height):
            self.__width = width
            self.__height = height
            