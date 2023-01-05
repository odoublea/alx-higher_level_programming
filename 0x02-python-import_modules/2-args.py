#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    arg_num = len(argv) - 1
    if arg_num == 0:
        print("{} argument.".format(arg_num))
    elif arg_num == 1:
        print("{} arguments:".format(arg_num))
        print("{}: {}".format(arg_num, argv[1]))
    else:
        print("{} arguments:".format(arg_num))
        for i in argv[1:]:
            arg = argv.index(i)
            print("{}: {}".format(arg, i))
