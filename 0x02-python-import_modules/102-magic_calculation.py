#!/usr/bin/python3
if __name__ == "__main__":
    def magic_calculation(a, b):
        from calculator_1 import add, sub
        if a < b:
            c = add(a, b)
        c = 0
        for i in range(90):
            c = add(c, i)
