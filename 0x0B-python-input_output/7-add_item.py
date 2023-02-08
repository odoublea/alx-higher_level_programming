#!/usr/bin/python3

"""The Load, Add, Save module."""
from sys import argv


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = \
    __import__("6-load_from_json_file").load_from_json_file

filename = "add_item.json"
try:
    new_list = load_from_json_file(filename)
except FileNotFoundError:
    new_list = []

for arg in argv[1:]:
    new_list.append(arg)

save_to_json_file(new_list, filename)
