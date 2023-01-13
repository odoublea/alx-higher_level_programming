#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dict = a_dictionary.copy()
    if value not in a_dictionary.values():
        return new_dict
    for k, v in new_dict.items():
        if v == value:
            del a_dictionary[k]
    return a_dictionary
