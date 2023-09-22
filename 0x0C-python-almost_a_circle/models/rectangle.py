#!/usr/bin/python3
"""This module defines the rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class ingeriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initiates Rectangle instance

            Args:
            width: of the rectangle(int)
            height: of the rectangle(int)
            x: x-cordinate of recatngles' position
            y: y-cordinate
            id: Identifier for the rectangle

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter property for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x-coordinates"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for coordinates"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y-coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y-coordinate"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Method to calculate the are of rectangle"""
        area = self.__width * self.__height
        return area

    def display(self):
        """Display the rectangle with # characters"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Returns string representation of the rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)
