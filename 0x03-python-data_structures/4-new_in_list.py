#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if isinstance(my_list, list):
        new_list = my_list.copy()
    if 0 < idx < len(my_list):
        new_list[idx] = element
        return(new_list)
    return(new_list)
