#!/usr/bin/python3
"""Contains function to find a peak inside a list"""


def find_peak(list_of_integers):
    """Find peak inside a list of integers"""
    if list_of_integers == []:
        return None
    list_of_integers.sort()
    return list_of_integers[-1]
