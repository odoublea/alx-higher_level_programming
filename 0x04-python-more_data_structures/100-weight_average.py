#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return 0
    freq = sum((x * y) for x, y in my_list)
    weight = sum(j for i, j in my_list)
    weight_average = freq / weight
    return weight_average
