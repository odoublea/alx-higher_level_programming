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
        super().integer_validator("width", width)
        self.__width = width

        super().integer_validator("height", height)
        self.__height = height
    
    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """returns the rectangle description:"""
        desc = f"[{str(self.__class__.__name__)}] "\
               f"{str(self.__width)}/{str(self.__height)}"
        return desc
