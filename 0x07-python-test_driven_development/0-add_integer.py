#!/usr/bin/python3
'''
    This module contains the addition function


'''


def add_integer(a, b=98):
    '''
    This function returns two sum of two numbers
    '''
    if None or not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    
    if None or not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    
    return int(a) + int(b)
