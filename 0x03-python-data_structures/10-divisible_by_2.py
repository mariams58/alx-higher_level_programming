#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    n_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 > 0:
            n_list.append(False)
        else:
            n_list.append(True)
    return n_list
