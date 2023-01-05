#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    argv = argv[1:]

    answer = 0
    for i in argv:
        answer = int(i) + answer
    print(answer)
