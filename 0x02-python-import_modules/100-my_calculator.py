#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import *

    num_of_args = len(argv)
    
    if num_of_args < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    operator = argv[2]
    function = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    operators = ["+", "-", "*", "/"]


    if operator not in operators:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)
    elif operator == "+":
        print("{} {} {} = {}".format(a, operator, b, function[0]))
    elif operator == "-":
        print("{} {} {} = {}".format(a, operator, b, function[1]))
    elif operator == "*":
        print("{} {} {} = {}".format(a, operator, b, function[2]))
    else:
        print("{} {} {} = {}".format(a, operator, b, function[3]))
