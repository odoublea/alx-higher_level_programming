#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    number_of_args = len(argv) - 1
    if number_of_args == 0:
        print("0 arguments.")
    else:
        print("1 argument:" if number_of_args < 2 else
              "{} arguments:".format(number_of_args))
        for i in argv[1:]:
            arg = argv.index(i)
            print("{}: {}".format(arg, i))
