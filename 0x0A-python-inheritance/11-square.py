#!/usr/bin/python3

"""
    Geometry module
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This is a rectangle classs with attr size.
    It is a subclass of Rectangle

    Args:
        size(int): must be int greater than 0 else error
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the square area."""
        return self.__size * self.__size

    def __str__(self):
        """returns the square description."""
        desc = f"[{str(self.__class__.__name__)}] "\
               f"{str(self.__size)}/{str(self.__size)}"
        return desc
