#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the sum of a and b"""
    from sys import argv
    from calculator_1 import add, sub, mul, div
    x = len(argv)
    if x != 4:
        print("{} <a> <operator> <b>".format(argv[0]))
        exit(1)
    op = {'+': add, '-': sub, '*': mul, '/': div}
    if argv[2] in op:
        a = int(argv[1])
        b = int(argv[3])
        ops = op[argv[2]]
        res = ops(a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, b, argv[2], res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    exit(0)
