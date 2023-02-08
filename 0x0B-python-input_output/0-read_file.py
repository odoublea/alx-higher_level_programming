#!/usr/bin/python3

"""The Read file module"""


def read_file(filename=""):
    """This function takes a text file and churns out it content."""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end="")
