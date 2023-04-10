#!/usr/bin/python3
"""This module contain classes called BaseGeometry, Rectangle"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class
    Args:
        BaseGeometry (Class): parent class
    """
    def __init__(self, width, height):
        """__init__ method
        Args:
            width (int): integer type
            height (int): integer type
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
