#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    len = len(argv)
    arg_num = len - 1
    if arg_num == 0:
        print("{} argument.".format(arg_num))
    elif arg_num == 1:
        print("{} arguments:".format(arg_num))
        print("{}: {}".format(arg_num, argv[arg_num]))

    else:
        print("{} arguments:".format(arg_num))
        for i in argv:
            arg = argv.index(i)
            if arg == 0:
                continue
            print("{}: {}".format(arg, i))
