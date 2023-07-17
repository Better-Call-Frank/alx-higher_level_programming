#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys

def init_board(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    board = [[' ' for _ in range(n)] for _ in range(n)]
    return board

def board_deepcopy(board):
    """Return a deepcopy of a chessboard."""
    return [row.copy() for row in board]

def get_solution(board):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return solution

def xout(board, row, col):
    """Mark spots on the chessboard as 'x' where queens cannot be placed."""
    n = len(board)
    for i in range(n):
        board[row][i] = "x"  # X out row
        board[i][col] = "x"  # X out column
        if row+i < n and col+i < n:
            board[row+i][col+i] = "x"  # X out diagonal down-right
        if row-i >= 0 and col-i >= 0:
            board[row-i][col-i] = "x"  # X out diagonal up-left
        if row+i < n and col-i >= 0:
            board[row+i][col-i] = "x"  # X out diagonal down-left
        if row-i >= 0 and col+i < n:
            board[row-i][col+i] = "x"  # X out diagonal up-right

def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    n = len(board)
    if queens == n:
        solutions.append(get_solution(board))
        return solutions

    for col in range(n):
        if board[row][col] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][col] = "Q"
            xout(tmp_board, row, col)
            solutions = recursive_solve(tmp_board, row + 1, queens + 1, solutions)

    return solutions

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: nqueens N\nN must be a number")
        sys.exit(1)

    n = int(sys.argv[1])
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(n)
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
