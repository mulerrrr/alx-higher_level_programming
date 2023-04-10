#!/usr/bin/python3
"""This module contains a function called is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """is_kind_of_class function that determines if obj is instance
    of a_class
    Args:
        obj (instance): is a object
        a_class (class): is a class
    """
    return (isinstance(obj, a_class))
