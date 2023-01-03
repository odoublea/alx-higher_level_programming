#!/usr/bin/python3
def uppercase(str):
    tmp = list(str)
    for c in range(len(tmp)):
        if ord(tmp[c]) >= 97 and ord(tmp[c]) <= 123:
            tmp[c] = chr(ord(tmp[c]) - 32)
    print("{}".format("".join(tmp)))
