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
