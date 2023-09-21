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
        self.__width = value

    @property
    def height(self):
        """Getter for the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height"""
        self.__height = value

    @property
    def x(self):
        """Getter for x-coordinates"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for coordinates"""
        self.__x = value

    @property
    def y(self):
        """Getter for y-coordinate"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y-coordinate"""
        self.__y = value
