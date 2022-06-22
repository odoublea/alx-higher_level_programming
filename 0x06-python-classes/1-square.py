#!/usr/bin/python3
'''This module contains a Square class that has a private instance'''


class Square:
    '''A square has four equal sides. Some can be seen while some are hidden'''

    def __init__(self, size):
        self.__size = size
