#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import *

    num_of_args = len(argv)
    
    if num_of_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a, operator, b = int(argv[1]), argv[2], int(argv[3])
    operators = ["+", "-", "*", "/"]
    result = 0

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)
    elif operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    else:
        result = div(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
