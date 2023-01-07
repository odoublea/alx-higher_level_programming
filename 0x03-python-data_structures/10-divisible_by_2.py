#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    for i in new_list:
        if i % 2 == 0:
            new_list.append(i)

    return new_list
