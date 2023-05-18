#!/usr/bin/python3
"""This module contain a subclass called Rectangle"""


from models.base import Base


class Rectangle(Base):
    """Rectangle subclass that makes an abstraction of a rectangle
    Args:
        Base ([class]): base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ constructor method
        Args:
            width ([int]): rectangle width
            height ([int]): rectangle height
            x (int, optional): x value. Defaults to 0.
            y (int, optional): y value. Defaults to 0.
            id ([int], optional): id of instance. Defaults to None.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

# width getter and setter methods
    @property
    def width(self):
        """width getter method
        Returns:
            [int]: width value
        """
        return self.__width

    @width.setter
    def width(self, width):
        """width setter method
        Args:
            width ([int]): width value
        """
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

# height getter and setter methods
    @property
    def height(self):
        """height getter method
        Returns:
            [int]: height value
        """
        return self.__height

    @height.setter
    def height(self, height):
        """height setter method
        Args:
            height ([int]): height value
        """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

# x getter and setter methods
    @property
    def x(self):
        """x getter method
        Returns:
            [int]: x value
        """
        return self.__x

    @x.setter
    def x(self, x):
        """x setter method
        Args:
            x ([int]): x value
        """
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

# y getter and setter methods
    @property
    def y(self):
        """y getter method
        Returns:
            [int]: y value
        """
        return self.__y

    @y.setter
    def y(self, y):
        """y setter method for y
        Args:
            y ([int]): y value
        """
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """area method that determines the area of a rectangle
        Returns:
            [int]: area of the rectangle instance
        """
        return self.__width * self.__height

    def display(self):
        """display method prints in stdout the Rectangle instance
        with the character #"""
        s = "#"
        for i in range(0, self.__y):
            print("")
        for col in range(self.__height):
            for j in range(0, self.__x):
                print(" ", end="")
            print(s * self.__width)

    def __str__(self):
        """__str__ method that return human readable string
        Returns:
            [str]: string value
        """
        return "[Rectangle] ({}) {}/{} - {}/{}\
".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """update method that assigns an argument to each attribute"""

        names = ["id", "width", "height", "x", "y"]
        if args is not () and args is not None:
            for value, name in zip(args, names):
                setattr(self, name, value)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, k, v)

    def to_dictionary(self):
        """to_dictionary method that returns dictionary representation
        of the instance
        Returns:
            [dict]: dictionary representation
        """
        dic_repr = {}
        for key, value in vars(self).items():
            dic_repr[key.split("__")[-1]] = value
        return dic_repr

