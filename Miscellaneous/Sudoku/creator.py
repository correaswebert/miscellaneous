"""Program to create Sudoku puzzle"""

import random
from recursive_solution import solve, printBoard

def naiveCreator():
    puzzle = []
    board = [[0]*9 for _ in range(9)]
    while not solve(board):
        # choose location and number to be put at that location
        x,y, num = random.choice(range(1,10)), random.choice(range(1,10)), random.choice(range(1,10))
        # if cell pre-occupied then don't replace it
        if board[x][y]!=0:
            continue
        board[x][y] = num
        puzzle.append((num, x,y))
    return puzzle

def makeBoard():
    puzzle = naiveCreator()
    board = [[0]*9 for _ in range(9)]
    for item in puzzle:
        num, x, y = item
        board[x][y] = num
    return board


printBoard(makeBoard())
