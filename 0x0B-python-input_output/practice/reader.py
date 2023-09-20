#!/usr/bin/python3

def read_file(a_file=""):
    with open(a_file, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")

read_file("my_file_.t")
    
