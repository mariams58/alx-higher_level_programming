#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        d_list = my_list[:x]
    except():
        d_list = my_list[:-1]
    for item in d_list:
        num += 1
        print(item, end='')
    print()
    return num
