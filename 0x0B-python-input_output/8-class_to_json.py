#!/usr/bin/python3
"""This module introduces a function"""


def class_to_json(obj):
    """This function defines a function that converts"""
    json_dict = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (str, int, bool, list, dict)):
            json_dict[key] = value
    return json_dict
