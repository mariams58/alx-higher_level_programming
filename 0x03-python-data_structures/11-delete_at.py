#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    x = len(my_list)
    if my_list:
        new_list = []
        if idx < x or id > 0:
            return(my_list)
        for i in range(x):
            if i != idx:
                new_list.append(my_list[i])
        my_list = new_list
        return(my_list)


if __name__ == "__delete_at__":
    delete_at(my_list=[], idx=0)
