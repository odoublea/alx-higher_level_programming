#!/usr/bin/python3
def no_c(my_string):
    my_string = my_string.split()
    for ch in my_string:
        if ch == 'c' or ch == 'C':
            del ch

        my_string = " ".join(ch)
    return my_string
