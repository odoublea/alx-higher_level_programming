#!/usr/bin/python3

"""The Append to file module"""


def append_write(filename="", text=""):
    """This function appends a string at the end of a text file
    and returns the number of characters added.
    Args:
        filename: name of file to write to,
            if none new one is created
        text: the text to write
        """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
