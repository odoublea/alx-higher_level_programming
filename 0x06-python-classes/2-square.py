#!/usr/bin/python3

'''This script contain a class Square.'''


class Square:
    '''This is a class with a private size attribute
    and an instation of zero.
    Attributes:
        size -- width of the Square

    '''

    def __init__(self, size=0):
        """Exception:
            ValueError: size must be greater than zero
            TypeError: size must be an integer

        """
        try:
            self.__size = size
            if size < 0:
                raise ValueError('size must be >= 0')
        except TypeError:
            raise ('size must be an integer')
