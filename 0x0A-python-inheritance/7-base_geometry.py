#!/usr/bin/python3

"""
    Geometry module
"""


class BaseGeometry:
    """This is an empty geometry that validates its integers."""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates attributes of base class
        Args:
            name(string)
            value(int)
        """
        if not type(name) == str:
            raise TypeError("{} `name` must be a str"
                            .format(__class__.__name__))
        self.name = name
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
        self.value = value
