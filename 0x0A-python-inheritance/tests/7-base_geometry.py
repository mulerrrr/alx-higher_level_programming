#!/usr/bin/python3
"""This module contain a class called BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area method that raises an exception
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """integer_validator method that validate integer
        Args:
            name (str): is a string
            value (int): is a integer
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

