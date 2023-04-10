#!/usr/bin/python3
"""This module contain classes called BaseGeometry, Rectangle, Square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class
    Args:
        Rectangle (class): parent class
    """
    def __init__(self, size):
        """__init__ method
        Args:
            size (int): size integer
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

