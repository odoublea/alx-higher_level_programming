#!/usr/bin/python3

"""The Write to file module"""


def write_file(filename="", text=""):
    """This function writes to a text file.
    Args:
        filename: name of file to write to,
            if none new one is created
        text: the text to write
        """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
