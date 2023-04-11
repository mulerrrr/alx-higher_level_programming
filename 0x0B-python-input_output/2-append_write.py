#!/usr/bin/python3
"""This module contain a function called read_lines"""


def read_lines(filename="", nb_lines=0):
    """read_lines function that read nb_lines of a file
    Args:
        filename (str, optional): file name. Defaults to "".
        nb_lines (int, optional): lines to read from the file. Defaults to 0.
    """
    num_lines = 0
    with open(filename, encoding='UTF-8') as a_file:
        for _ in a_file:
            num_lines += 1
    with open(filename, encoding='UTF-8') as a_file:
        if nb_lines <= 0 or nb_lines >= num_lines:
            for i in a_file:
                print(i, end="")
        else:
            j = 0
            while j < nb_lines:
                print(a_file.readline(), end="")
                j += 1

