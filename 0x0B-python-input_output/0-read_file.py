#!/usr/bin/python3
"""This module contains a function called read_file"""


def read_file(filename=""):
    """read_file function that reads a file
    Args:
        filename (str, optional): file name string. Defaults to "".
    """
    with open(filename, encoding='utf-8') as a_file:
        line = a_file.read()
        print(line, end="")

