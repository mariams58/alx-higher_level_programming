#!/usr/bin/python3
"""Returns the result of division of 2 iven integers"""


def safe_print_division(a, b):
    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        return res
