#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        d_list = my_list[:x]
        print(d_list)
    except:
        d_list = my_list[:-1]
        print(d_list)
    for item in d_list:
        num += 1
    return num
