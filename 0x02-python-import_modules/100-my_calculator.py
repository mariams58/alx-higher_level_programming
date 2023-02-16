#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    op_list = ['+', '-', '*', '/']
    a = sys.argv[1]
    b = sys.argv[3]
    result = 0
    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    if sys.argv[2] not in op_list:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
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
