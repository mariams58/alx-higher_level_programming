#!/usr/bin/python3
"""Returns the result of division of 2 iven integers"""


def safe_print_division(a, b):
    try:
        res = a / b
        print("Inside result: {:.1f}".format(res))
    except (TypeError, ZeroDivisionError):
        res = None
        print("Inside result: {}".format(res))
    finally:
        return res
