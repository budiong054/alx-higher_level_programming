#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]
    if (operator != '+') and (operator != '-') \
            and (operator != '*') and (operator != '/'):
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    if operator == '+':
        print(f"{a:d} + {b:d} = {add(a, b):d}")
    elif operator == '-':
        print(f"{a:d} - {b:d} = {sub(a, b):d}")
    elif operator == '*':
        print(f"{a:d} * {b:d} = {mul(a, b):d}")
    else:
        print(f"{a:d} / {b:d} = {div(a, b):f}")
