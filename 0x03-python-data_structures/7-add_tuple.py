#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    #if i in tuple_a == 0 or 
    tuple_c = tuple(map(lambda i, j : i + j, tuple_a, tuple_b))
    return tuple_c
