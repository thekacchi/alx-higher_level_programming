#!/usr/bin/python3
"""This module contains a funtion that reads a file"""

def read_file(filename=""):
    """This function reads a file's content"""
    with open(filename, 'r', encoding= 'utf-8') as file:
        for line in file:
            print(line, end='')
