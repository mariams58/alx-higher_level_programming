#!/usr/bin/python3
import sys

"""Prints integers safely"""


def safe_print_integer_err(value):
    """Print an integer with "{:d}".format().

    Args:
    value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError) as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return False
    else:
        return True
