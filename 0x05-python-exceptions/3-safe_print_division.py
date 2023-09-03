#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a/b
        print("Inside result: {:.1f}".format(result))
    except ZeroDivisionError:
        result = "None"
        print("Inside result: None")
        return result
    finally:
        return result
