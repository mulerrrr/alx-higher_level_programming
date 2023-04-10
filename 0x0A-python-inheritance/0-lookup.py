#!/usr/bin/python3
"""This file contain a function that called lookup"""


def lookup(obj):
    """lookup function that get all attributes and methods of a class
    Args:
        obj (class): class parameter
    Returns:
        list: list with all attributes and methods of the class
    """
    return dir(obj)

