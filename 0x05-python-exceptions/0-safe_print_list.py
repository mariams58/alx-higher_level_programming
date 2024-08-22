#!/usr/bin/python3
"""Prints lists"""


def safe_print_list(my_list=[], x=0):
    cnt = 0
    for i in range(0, x):
        try:
            print("{}".format(my_list[i]), end="")
            cnt += 1
        except IndexError:
            break
    print("")
    return cnt
