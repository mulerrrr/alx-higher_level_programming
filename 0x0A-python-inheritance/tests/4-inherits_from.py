#!/usr/bin/python3
"""This module contain a function called inherits_from"""


def inherits_from(obj, a_class):
    """inherits_from function that determine if obj is instance of the
    actual a_class, and a_class is not subclass of type(obj)
    Args:
        obj (instance): is an instance
        a_class (class): is a class
    """
    return isinstance(obj, a_class) and not issubclass(a_class, type(obj))

