#!/usr/bin/python3
'''This module defines a square and its attributes'''


class Square:
    '''A square has four equal sides. And they are made of positive integers'''

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
