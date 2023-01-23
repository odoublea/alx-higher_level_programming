#!/bin/bash/python3
def safe_print_integer(value):
    try:
        int(value)
        print("{:d}".format(value))
    except ValueError as error:
        return False
    else:
        return True
