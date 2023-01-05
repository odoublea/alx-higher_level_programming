#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    len = len(argv)
    arg_num = len - 1
    
    if len == 1:
        print("{} argument.".format(arg_num))
    elif len == 2:
        print("{} arguments:".format(arg_num))
        print("{}: {}".format(arg_num, argv[-1]))

    else:
        print("{} arguments:".format(arg_num))
        for i in argv:
            index = argv.index(i)
            if index == 0:
                continue
            print("{}: {}".format(index, i))        
