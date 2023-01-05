#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import *
   
    num_of_args = len(argv) - 1

    if num_of_args != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    
    operators = ["+", "-", "*", "/"]
    functions = [add(a, b), sub(a, b), mul(a, b), div(a, b)]
    if not(argv[2] in operators):
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1)

    for operator, function in zip(operators, functions):
        if operator == argv[2]:
            break
    print("{} {} {} = {}".format(a, argv[2], b, function))
