#!/usr/bin/python3

"""Save Object to a JSON file module"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj: object to write
        filename: file to write on
    """
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
