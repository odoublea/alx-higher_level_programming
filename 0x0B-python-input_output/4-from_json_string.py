#!/usr/bin/python3

"""The JSON string to Object module."""


def from_json_string(my_str):
    """This function loads a json"""
    import json
    return json.loads(my_str)