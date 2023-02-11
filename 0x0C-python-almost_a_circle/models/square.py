#!/usr/bin/python3

"""The Square module."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class."""
    def __init__(self, size, x=0, y=0, id=None):
        """Super initializing attributes."""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """returns the square description."""
        desc = f"[{self.__class__.__name__}]"\
               f" ({self.id}) {self.x}/{self.y} - {self.size}"
        return desc

    @property
    def size(self):
        """Get square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.__size = value

    def update(self, *args, **kwargs):
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
