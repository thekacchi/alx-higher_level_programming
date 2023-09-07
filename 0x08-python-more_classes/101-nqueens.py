#!/usr/bin/python3

import sys

def is_safe(board, row, col, n):
    """check if queen cn be placed in board[r][c]"""
    """check the left side of the row"""
    for i in range(col):
        if board[row][i] == 1:
            return False


    """check upper diagonal on the left side"""
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    """check lower diagoal on the left side"""
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(n):
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    solutions = []

    def solve_util(col):
        if col >= n:
            solution = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        solution.append([i, j])
            solutions.append(solution)
            return

        for i in range(n):
            if is_safe(board, i, col, n):
                board[i][col] = 1
                solve_util(col + 1)
                board[i][col] = 0

    solve_util(0)

    """sort the solutions for consistent output"""
    solutions.sort()

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(n)
