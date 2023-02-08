#!/usr/bin/python3

"""The Write to file module"""


def write_file(filename="", text=""):
    """This function writes to a text file."""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(f"{text}\n")