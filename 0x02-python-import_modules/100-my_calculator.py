#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    if operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    opertions = {
            "+": add,
            "-": sub,
            "*": mul,
            "/": div,
    }

    func = operations[operator]
    result = func(a, b)
    print("{} {} {} = {}".format(a, operator, b, result))
