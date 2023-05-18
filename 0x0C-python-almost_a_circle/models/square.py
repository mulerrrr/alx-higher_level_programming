#!/usr/bin/python3
"""This module contain a subclass called Square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square subclass that makes an abstraction of a square
    Args:
        Base ([class]): parent class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """__init__ constructor method for square instance
        Args:
            size ([int]): size of square
            x (int, optional): position in x. Defaults to 0.
            y (int, optional): position in y. Defaults to 0.
            id ([type], optional): id of the instance. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """__str__ method that return human readable sting
        representation of an square instance
        Returns:
            [str]: string representation a square instance
        """
        return "[Square] ({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size getter method to get the size of square
        Returns:
            [int]: size of the square
        """
        return self.width

    @size.setter
    def size(self, size):
        """size setter method to set the width and heigth of square
        Args:
            size ([int]): set the width and height
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """update method that assigns an argument to each attribute"""

        names = ["id", "size", "x", "y"]
        if args is not () and args is not None:
            for value, name in zip(args, names):
                setattr(self, name, value)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """to_dictionary method that return dictionary representation
        of an instance
        Returns:
            [dict]: dictionary representation
        """
        dic_repr = {}
        for key, value in vars(self).items():
            if key == "_Rectangle__width" or key == "_Rectangle__height":
                dic_repr["size"] = value
            else:
                dic_repr[key.split("__")[-1]] = value
        return dic_repr

