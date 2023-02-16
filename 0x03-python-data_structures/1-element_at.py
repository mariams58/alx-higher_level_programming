#!/usr/bin/python3


def element_at(my_list, idx):
    if my_list:
        if idx < 0 or idx > (len(my_list) - 1):
            return None
        return my_list[idx - 1]


if __name__ == "__element_at__":
    element_at(my_list, idx)
