#!/usr/bin/python3


def print_rev_alphabet():
    for i in range(90, 65, -1):
        if i % 2 == 0:
            i = i + 32
        x = chr(i)
        print("{}".format(x), end='')
    print()
