#!/bin/bash
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
