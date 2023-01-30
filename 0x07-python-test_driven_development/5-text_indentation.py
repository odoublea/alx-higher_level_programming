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
    for i in sep:
        text = text.replace(i, '{}\n'.format(i))
    lines = text.splitlines()
    for index, line in enumerate(lines):
        print(line.strip(), end='' if index == len(lines) - 1 else '\n\n')
