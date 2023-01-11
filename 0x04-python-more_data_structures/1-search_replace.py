#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is not None:
        new_list = my_list.copy()
        new_list[search] = replace
    return new_list
