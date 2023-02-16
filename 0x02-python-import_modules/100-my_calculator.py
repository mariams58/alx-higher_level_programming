#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    op_list = ['+', '-', '*', '/']
    items = len(sys.argv)
    result = 0
    if items < 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] not in op_list:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        a = sys.argv[1]
        b = sys.argv[3]
        if sys.argv[2] == op_list[0]:
            result = add(int(a), int(b))
        elif sys.argv[2] == op_list[1]:
            result = sub(int(a), int(b))
        elif sys.argv[2] == op_list[2]:
            result = mul(int(a), int(b))
        elif sys.argv[2] == op_list[3]:
            result = div(int(a), int(b))
        print("{} {} {} = {}".format(a, sys.argv[2], b, result))


if __name__ == "__main__":
    main()
