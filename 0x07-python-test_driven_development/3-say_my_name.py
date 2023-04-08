#!/usr/bin/python3
"""This module contain a function that prints a string"""


def say_my_name(first_name, last_name=""):
    """say_my_name function prints My name is <first_name> <last_name>
    Args:
        first_name (str): first parameter
        last_name (str, optional): second parameter.
    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """

    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))

