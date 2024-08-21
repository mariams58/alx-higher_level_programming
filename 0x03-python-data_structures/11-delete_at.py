#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    x = len(my_list)
    if idx > x and idx <= 0:
        return my_list
    del my_list[idx]
    return my_list
