#!/usr/bin/python3


def print_reversed_list_integer(my_list=[]):
    if my_list:
        x = len(my_list)
        for i in range(x - 1, -1, -1):
            print("{:d}".format(my_list[i]))


if __name__ == "__print_reversed_list_integer__":
    print_reversed_list_integer(my_list)
