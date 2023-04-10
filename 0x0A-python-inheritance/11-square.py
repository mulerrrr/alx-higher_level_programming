
#!/usr/bin/python3
"""This module contain classes called BaseGeometry, Rectangle, Square"""


Rectangle = __import__('10-square').Rectangle


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

    def __str__(self):
        """__str__ method"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
