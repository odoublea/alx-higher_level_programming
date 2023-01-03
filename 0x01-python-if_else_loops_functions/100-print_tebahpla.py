#!/usr/bin/python3
for alphabet in reversed(range(97, 123)):
    if alphabet % 2 == 0:
        print("{:c}".format(alphabet), end='')
        continue
    print("{:c}".format(alphabet-32), end='')
