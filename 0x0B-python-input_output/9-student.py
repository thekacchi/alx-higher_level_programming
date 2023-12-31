#!/usr/bin/python3
"""This module contains a class"""


class Student:
    """This class defines a student"""
    def __init__(self, first_name, last_name, age):
        """This is a method (init mthd) of class student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """This method convs to json"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
