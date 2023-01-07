#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div

    num_of_args = len(argv)

    if num_of_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, operator, b = int(argv[1]), argv[2], int(argv[3])
    operators = ["+", "-", "*", "/"]
    funcs = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    result = 0

    for i, ops in enumerate(operators):
        if argv[2] == ops:
            print("{} {} {} = {}".format(a, ops, b, funcs[i]))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
