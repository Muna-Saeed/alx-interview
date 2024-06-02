#!/usr/bin/python3
""" N queens """
import sys


def is_safe(board, row, col):
    """ Check if it's safe to place a queen at board[row][col]. """
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(n):
    """ Solve the N Queens problem and print all solutions. """
    def backtrack(row):
        if row == n:
            print_solution()
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    def print_solution():
        solution = []
        for i in range(n):
            solution.append([i, board[i]])
        print(solution)

    board = [-1] * n
    backtrack(0)


def main():
    """ Main entry point of the program. """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve_nqueens(n)


if __name__ == "__main__":
    main()
