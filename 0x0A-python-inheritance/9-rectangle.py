#!/usr/bin/python3
"""This module defines class (child) Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class inherits BaseGeometry"""

    def __init__(self, width, height):
        """Initializes class Rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Calculates area of recrangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """string representation"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
