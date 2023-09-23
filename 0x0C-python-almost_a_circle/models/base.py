#!/usr/bin/python3
"""This module defines the base"""
import json


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

    def to_json_string(list_dictionaries):
        """Serializes a list of dictionaries into JSON string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    def from_json_string(json_string):
        """Returns list of dictionary from json string
        Args: json string rep of list dictionaries
        """
        if not json_string:
            return []
        return json.loads(json_string)
