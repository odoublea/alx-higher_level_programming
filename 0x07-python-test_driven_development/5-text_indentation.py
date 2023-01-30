#!/usr/bin/python3
"""
    This module contains a function that split strings
    """

def text_indentation(text):
    """This function takes a string argument, text and print with 
    2 new linws after each of these characters: ``.``, ``?`` and ``:``
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    sep = ['.', '?', ':']
    res = re.split(sep, text) 
