#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a/b
        print("Inside result: {:.1f}".format(result))
        return result
    except ZeroDivisionError:
        print("Inside resilt: None")
        return None
