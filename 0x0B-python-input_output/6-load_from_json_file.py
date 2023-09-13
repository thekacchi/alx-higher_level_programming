#!/usr/bin/python3
"""This module contains function definition"""
import json


def load_from_json_file(filename):
    """This function creates object from JSON file"""
    with open(filename, 'r', encoding='utf8') as file:
        data = json.load(file)
    return data
