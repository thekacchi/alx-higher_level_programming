#!/usr/bin/python3
"""This module is for square, which inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Definition of the class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes the square instance"""
        super().__init__(size, size, x, y, id)
        """Call the rectangle instructor with size as idth and height"""

    def __str__(self):
        """Returns string representationmof square"""
        return "[Square] ({}) {}/{} - {}".format(
               self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update square attributes for list and dictionaries"""
        if args:
            arg_names = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, arg_names[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def dictionary(self):
        """Return dictionary representation of the square"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
