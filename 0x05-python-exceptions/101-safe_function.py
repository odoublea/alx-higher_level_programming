#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        func = fct(*args)
    except Exception as f:
        print("Exception: {}".format(f), file=sys.stderr)
        return None
    else:
        return func
