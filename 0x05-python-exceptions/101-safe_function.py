#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        func = fct(*args)
        return func
    except Exception as e:
        print("{}".format(e), file=sys.stderr)
        return None
