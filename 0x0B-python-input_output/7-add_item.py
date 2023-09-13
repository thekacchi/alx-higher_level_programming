#!/usr/bin/python3
"""This module contains a function definition"""
import sys
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

"""Check if it exists"""
file_exists = exists("add_item.json")

"""load existing or create new"""
if file_exists:
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []

"""Add CL arg to the list"""
for arg in sys.argv[1:]:
    my_list.append(arg)

"""Svae updated list to add_item.json file"""
save_to_json_file(my_list, "add_item.json")
