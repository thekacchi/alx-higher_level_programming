#!/usr/bin/python3
"""This module defines a function"""
import json


def save_to_json_file(my_obj, filename):
    """function writes an object to a text file with JSON rep"""
    with open(filename, 'w') as file:
        return json.dump(my_obj, file)
