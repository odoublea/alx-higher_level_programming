#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = ()
    length = len(sentence)
    first = sentence[0]

    if len(sentence) == 0:
        my_tuple = length, 'None'

    my_tuple = length, first
    return my_tuple
