#!/usr/bin/python3
"""
This script demonstrates how to import the Square class from the 0-square module
and create an instance of the class. It then prints the type and attributes of the
created object.
"""
# Import the Square class from the 0-square module.
Square = __import__('0-square').Square

# Create an instance of the Square class.
my_square = Square()

# Print the type of the my_square object.
print(type(my_square))

# Print the dictionary of attributes associated with the my_square object.
print(my_square.__dict__)

