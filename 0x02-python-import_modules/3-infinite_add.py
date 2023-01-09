#!/usr/bin/python3
import sys


def main():
    sum = 0
    if len(sys.argv) > 2:
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
    print("{}".format(sum))


if __name__ == "__main__":
    main()
