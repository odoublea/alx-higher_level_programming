#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    length = len(sentence)
    first = sentence[0]

    if length == 0:
        my_tuple = 0, 'None'
    my_tuple = length, first

    return my_tuple
