#!/usr/bin/python3

"""The Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class.
        Args:
            size(int): size of the square
            x(int): space around the width
            y(int): space around the height
            id(int): id of the square
                    increases when another square is added.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Super initializing attributes."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """returns the square description."""
        desc = f"[{self.__class__.__name__}]"\
               f" ({self.id}) {self.x}/{self.y} - {self.width}"
        return desc

    @property
    def size(self):
        """Get square size"""
        return self.width

    @size.setter
    def size(self, value):
        """Set square size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the class Square"""
        attrs = ('id', 'size', 'x', 'y')

        for attr, val in zip(attrs, args):
            setattr(self, attr, val)

        for key, val in kwargs.items():
            setattr(self, key, val)

    def to_dictionary(self):
        """Square instance to dictionary representation."""
        dic = {}
        attrs = ('id', 'x', 'size', 'y')
        for i in attrs:
            dic[i] = getattr(self, i)

        return dic
