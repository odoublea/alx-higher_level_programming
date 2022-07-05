#!/usr/bin/python3

"""A BaseGeometry class"""


class BaseGeometry:
    """A BaseGeometry class that raises exception"""

    def area(self):
        """raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates the value attribute
            Args:
                name(string)
                value(int)
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
