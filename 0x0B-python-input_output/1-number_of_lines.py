#!/usr/bin/python3
"""This module contains a function called number_of_lines"""


def number_of_lines(filename=""):
    """number_of_lines function that find the number if lines in a file
    Args:
        filename (str, optional): file name string. Defaults to "".
    Returns:
        [int]: number of lines in the file
    """
    with open("{}".format(filename), encoding='utf-8') as a_file:
        lines = 0
        for a_line in a_file:
            lines += 1
        return lines

