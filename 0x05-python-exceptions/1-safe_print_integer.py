#!/bin/bash/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except Exception:
        return True
    else:
        return False
