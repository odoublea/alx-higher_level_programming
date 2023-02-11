#!/usr/bin/python3

"""The Rectangle module."""
from models.base import Base


class Rectangle(Base):
    """The Rectangle class initialization function
        Args:
            width(int): width of the rectangle
            height(int): height of the rectangle
            x(int): space around the width
            y(int): space around the height
            id(int): id of the rectangle
                    increases when another rectangle is added
    """
    rec_display = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Get width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set rectangle width."""
        if not isinstance(value, int) and value is not type(int):
            raise TypeError(f"width must be an integer")
        if value <= 0:
            raise ValueError(f"width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get position x of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """Set position rectangle x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get position y of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """Set position rectangle y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """Display rectangle with `#`."""
        for i in range(self.__y):
            print()
        for row in range(self.__height):
            for j in range(self.__y):
                print(' ', end='')
            for hash in range(self.__width):
                print("{}".format(self.rec_display), end='')
            print()

    def __str__(self):
        """Return string representation of the rectangle instance"""
        desc = f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y}"\
               f" - {self.__width}/{self.__height}"
        return desc
