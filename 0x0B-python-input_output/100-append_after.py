#!/usr/bin/python3
"""This module defines a function"""


def append_after(filename="", search_string="", new_string=""):
    """This function appends a string when it finds search_string"""
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
