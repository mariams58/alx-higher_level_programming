#!/usr/bin/python3
import sys


def main():
    num_arg = len(sys.argv)
    if num_arg == 1:
        print("{} arguments.".format(num_arg - 1))
    elif num_arg > 1:
        if num_arg > 2:
            print("{} arguments:".format(num_arg - 1))
        elif num_arg == 2:
            print("{} argument:".format(num_arg - 1))
        for i in range(1, num_arg):
            print("{}: {}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
