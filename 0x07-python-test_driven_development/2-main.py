#!/usr/bin/python3

matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [22, 4, 6],
    [8, 10, 12]
]
div = float('inf') 
print(matrix_divided(matrix, div))
print(matrix)
