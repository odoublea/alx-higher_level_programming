#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) < 0:
        return 0
    nominator = sum(map(sum, my_list))
    denominator = sum(j for i, j in my_list)
    result = nominator / denominator
    return result
