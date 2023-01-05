#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    number_of_args = len(argv) - 1

    if number_of_args == 0:
        print("{} argument.".format(number_of_args))
    elif number_of_args == 1:
        print("{} arguments:".format(number_of_args))
        print("{}: {}".format(number_of_args, argv[1]))
    else:
        print("{} arguments:".format(number_of_args))
        for i in argv[1:]:
            arg = argv.index(i)
            print("{}: {}".format(arg, i))
