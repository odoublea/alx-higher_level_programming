#!/usr/bin/python3

"""The To JSON string module"""


def to_json_string(my_obj):
    """This function returns the JSON representation
    of an object (string)
    """
    import json
    return json.dumps(my_obj)
