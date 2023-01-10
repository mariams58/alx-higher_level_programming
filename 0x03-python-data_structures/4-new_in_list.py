#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0 or idx > (len(mylist) - 1):
        return my_list.copy()
    new_list[idx] = element
    return new_list


if __name__ == "__new_in_list__":
    new_in_list(my_list, idx, element)
