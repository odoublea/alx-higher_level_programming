#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    tuple_c = tuple(map(lambda i, j: i + j, tuple_a, tuple_b))
    return tuple_c[:2]
