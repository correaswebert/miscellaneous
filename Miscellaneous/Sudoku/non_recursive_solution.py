"""
Sudoku solver based on backtracking algorithm

My own implementation. It is slower than the recursive solution as there are
more conditional checking than that.
"""

import os

def transpose(matrix):
    return [row for row in zip(*matrix)]

# Returns [(x,y), ...]
def findEmptyCells(board):
    """Returns a list of all empty cells"""
    empty_cells = []
    for x in range(9):
        for y in range(9):
            if board[x][y] == 0:
                empty_cells.append((x,y))
    return empty_cells

# Returns bool
def isvalid(board, num, cell):
    """Checks if num can be validly placed at cell"""
    x, y = cell
    row = board[x]
    col = transpose(board)[y]

    # check row if num already present
    if any(row[i] == num for i in range(9)):
        return False
    # check col if num already present
    if any(col[i] == num for i in range(9)):
        return False
    
    # get start position of box
    Xbox = (x//3) * 3
    Ybox = (y//3) * 3
    for i in range(Xbox, Xbox+3):
        for j in range(Ybox, Ybox+3):
            if board[i][j] == num:
                return False
    
    return True

# Returns True if solved else False
def solve(board):
    empty_cells = findEmptyCells(board)

    # in case prev cell was 9, the 1st if is needed for resetting
    # as the elif block won't be executed as for cond violated

    # also if last elif block not present, then if all 1-9 checked
    # and non work, then the 1st if won't be executed for resetting
    # as inc/dec not executed

    i = 0
    while -1 < i < len(empty_cells):
        x,y = empty_cells[i]

        # start checking next value onwards
        # but if next value is 10, then reset the cell and go to previous
        next_val = board[x][y] + 1
        if next_val == 10:
            board[x][y] = 0
            i -= 1
            continue
        
        for k in range(next_val, 10):
            if isvalid(board, k, (x,y)):
                board[x][y] = k
                i += 1
                break
            # all values 1-9 don't work, empty cell and go to prev
            elif k == 9:
                board[x][y] = 0
                i -= 1
                break
    
    # if an empty cell is found, 'unsolvable', board is exhaustively searched
    if any(board[x][y]==0 for y in range(9) for x in range(9)):
        return False
    return True

def printBoard(board):
    board_string = ""

    for x in range(9):
        if x == 3 or x == 6:
            board_string += "------+-------+------\n"
        for y in range(9):
            if y == 3 or y == 6:
                board_string += "| "
            char = board[x][y]
            char = str(char) if char != 0 else ' '
            board_string += char + ' '
        board_string += '\n'
    
    print(board_string)

# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    board = [
        [9,0,0,  0,0,0,  0,0,1],
        [0,0,3,  6,0,0,  0,0,0],
        [0,7,0,  0,9,0,  2,0,0],

        [0,5,0,  0,0,7,  0,0,0],
        [0,0,0,  0,4,5,  7,0,0],
        [0,0,0,  1,0,0,  0,3,0],
        
        [0,0,1,  0,0,0,  0,6,8],
        [0,0,8,  5,0,0,  0,1,0],
        [0,9,0,  0,0,0,  4,0,0]
    ]

    starburst = [
        [0,0,0,  0,0,0,  0,0,0],
        [0,0,0,  0,0,3,  0,8,5],
        [0,0,1,  0,2,0,  0,0,0],

        [0,0,0,  5,0,7,  0,0,0],
        [0,0,4,  0,0,0,  1,0,0],
        [0,9,0,  0,0,0,  0,0,0],

        [5,0,0,  0,0,0,  0,7,3],
        [0,0,2,  0,1,0,  0,0,0],
        [0,0,0,  0,4,0,  0,0,9],
    ]

    solved = solve(board)
    if solved:
        printBoard(board)
    else:
        print("Unsolvable!")

"""
---------
-----3-85
--1-2----
---5-7---
--4---1--
-9-------
5------73
--2-1----
----4---9
"""