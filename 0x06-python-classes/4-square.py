#!/usr/bin/python3

'''This script contain a class Square.'''


class Square:
    '''This is a class with a private size attribute
    and an instation of zero.
    Attributes:
        size -- width of the Square

    '''

    def __init__(self, size=0):
        """Initializing a new square

        Args:
            size(int): size of the square

        Exception:
            ValueError: size must be greater than zero
            TypeError: size must be an integer

        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')

    def area(self):
        """Returns the area of the square."""
        return (self.__size ** 2)

    @property
    def size(self):
        """Get the value of size."""
        return self.__size

    @size.setter
    def size(self, value):
        """set the value of size."""
        self.__size = value
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
