#!/usr/bin/python3

"""
Solution to the nqueens problem
"""

import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Backtrack function to solve nqueens problem
    Args:
        r (int): current row
        n (int): number of queens
        cols (set): set of columns occupied by queens
        pos (set): set of positive diagonals occupied by queens
        neg (set): set of negative diagonals occupied by queens
        board (list): chess board
    Return:
        None
    """
    if r == n:
        res = []
        for i in range(len(board)):
            for k in range(len(board[i])):
                if board[i][k] == 1:
                    res.append([i, k])
        # Print the coordinates of the queens
        print(res)
        # Return the result
        return

    for c in range(n):
        # Check if the column or positive diagonal or
        # negative diagonal is occupied
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        # Place the queen on the board
        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        # Recursively call the backtrack function for the next row
        backtrack(r+1, n, cols, pos, neg, board)

        # Remove the queen from the board
        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solution to nqueens problem
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    n = sys.argv
    if len(n) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(n[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)