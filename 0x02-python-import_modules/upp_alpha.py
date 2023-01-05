#!/usr/bin/python3
for chr in range(65, 91):
    print("{:c}".format(chr), end="" if chr < 90 else '\n')
