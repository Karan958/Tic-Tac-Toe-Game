"""
tic tac toe board with functions
"""
import numpy as np
from variables import *

# board
Board = np.zeros((rows, cols))


def is_available(x, y):
    return Board[x][y] == 0


def get_empty_square():
    res = []
    for i in range(3):
        for j in range(3):
            if Board[i][j] == 0:
                res.append([i, j])

    return res


def mark_board(x, y, player):
    Board[x][y] = player


def is_full():
    for i in range(rows):
        for j in range(cols):
            if Board[i][j] == 0:
                return False
    return True

