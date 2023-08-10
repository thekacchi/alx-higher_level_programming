#!/usr/bin/python3
# 12-fizzbuzzz.py

def fizzbuzz():
    """
    Print the numbers from 1 to 100 separated by a space.
    Multiples of 3 are replaced with 'Fizz'.
    Multiples of 5 are replaced with 'Buzz'.
    Multiples of both 3 and 5 are replaced with 'FizzBuzz'.
    """
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
