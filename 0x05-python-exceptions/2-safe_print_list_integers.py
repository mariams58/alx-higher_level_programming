#!/usr/bin/python3
"""Prints a lists of integers safely"""


def safe_print_list_integers(my_list=[], x=0):
    cnt = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            cnt += 1
        except (TypeError, ValueError):
            continue
    print("")
    return cnt
