#!/usr/bin/python3
"""This module defines the base"""


class Base:
    """This is the definition for the base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """The init method for base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
