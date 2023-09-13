#!/usr/bin/python3
"""This module contains a class"""


class Student:
    """This class defines a student"""
    def __init__(self, first_name, last_name, age):
        """This is a method (init mthd) of class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This method convs to json"""
        if attrs is None:
            return self.__dict__
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict
