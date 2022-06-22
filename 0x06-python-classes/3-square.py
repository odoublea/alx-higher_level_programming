#!/usr/bin/python3
'''This module defines a square and calculates its area'''


class Square:
    '''A square has four equal sides. Calulate the area of a square*2'''

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        return (self.__size ** 2)
