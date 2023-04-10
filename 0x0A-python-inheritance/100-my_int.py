#!/usr/bin/python3
"""This module has a rebel class"""


class MyInt(int):
    """MyInt class
    Args:
        int (class): int class
    """
    def __init__(self, value):
        """__init__ method
        Args:
            value (int): integer value
        """
        self.value = value

    @property
    def value(self):
        """value getter
        Returns:
            [int]: int value
        """
        return self.__value

    @value.setter
    def value(self, value):
        """value setter
        Args:
            value (int): integer value
        """
        self.__value = value

    def __str__(self):
        """__str__ method
        Returns:
            [str]: string value
        """
        return "{:d}".format(self.__value)

    def __eq__(self, other):
        """__eq__ method
        Args:
            other (int): other integer
        Returns:
            [bool]: False
        """
        return self.__value != other

    def __ne__(self, other):
        """__ne__ method
        Args:
            other (int): integer value
        Returns:
            [bool]: True
        """
        return self.__value == other

