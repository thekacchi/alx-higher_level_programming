#!/usr/bin/python3
"""This module contains the definition of a rectangle

"""


class Rectangle:
    """The class Rectangle
    """
    def __init__(self, width=0, height=0):
        if isinstance(width, int) is False:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        if isinstance(height, int) is False:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__width = width
        self._Rectangle__height = height

    @property
    def width(self):
        return self._Rectangle__width

    @property
    def height(self):
        return self._Rectangle__height

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def __str__(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return ""
        rectangle = ""
        for i in range(self._Rectangle__height):
            rectangle += "#" * self._Rectangle__width
            if i < self._Rectangle__height - 1:
                rectangle += "\n"
        return rectangle

    def __repr__(self):
        _width = self._Rectangle__width
        _height = self._Rectangle__height
        return f"Rectangle({_width}, {_height})"

    def area(self):
        return self._Rectangle__width * self._Rectangle__height

    def perimeter(self):
        return (self._Rectangle__width * 2) + (self._Rectangle__height * 2)

    def __del__(self):
        print("Bye  rectangle...")
