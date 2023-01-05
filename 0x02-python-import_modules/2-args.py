#!/usr/bin/python3
'''
def argument:
    arg = sys.argv
    len = len(arg)

    if len <= 0:
        print("{}:".format(len))
    elif len == 1:
        print("{}: argument".format(len))
        print("{}: {}".format(arg.index(1), i))

    for i in arg:
        index = arg.index(i)
        len = len(arg)
        if i == 0:
            continue
        elif index == 1:
            print("{}: argument".format(len))
            print("")
'''

if __name__ == "__main__":
    if argv == 0:
        continue
    for i in argv:
        index = argv.index(i)
        print("{}: {}".format(index, i))
