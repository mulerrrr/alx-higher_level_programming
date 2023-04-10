#!/usr/bin/python3
"""This module contain a class called BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class
    Raises:
        Exception: area() is not implemented
    """
    def area(self):
        """area method that raises an exception
        """
        raise Exception("area() is not implemented")

