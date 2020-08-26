"""Recursive approach to Sudoku Backtracking Solver

Sudoku solver based on backtracking algorithm using recursion.
The recursive (faster) implementation is forked from
https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
"""

def transpose(matrix):
    return [row for row in zip(*matrix)]

# Returns (x,y)
def firstEmptyCell(board):
    """Returns first occurence of an empty cell"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

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
    """
    Recursive method to solve Sudoku (unique solution)

    First empty cell is found everytime the function is called. This cell is
    then filled from 1 to 9 until it satisfies the rules. If later on solution
    can't be found via that route, next number is tried. Proper Sudoku is
    assumed, so multiple solutions are not found
    """
    cell = firstEmptyCell(board)
    # Base case for recursion
    # no empty cells, also all other cells filled validly, so board solved
    if cell is None:
        return True
    
    x, y = cell
    for i in range(1,10):
        # if i is valid at cell in board, go to next empty cell (recursively)
        if isvalid(board, i, cell):
            board[x][y] = i

            # try filling next empty cell till successful
            if solve(board):
                return True

            # i is invalid in cell, try i+1
            board[x][y] = 0
    
    # board can't be solved
    return False

solutions = []
def solveX(board):
    global solutions
    cell = firstEmptyCell(board)
    # Base case for recursion
    # no empty cells, also all other cells filled validly, so board solved
    if cell is None:
        printBoard(board)
        if board not in solutions:
            solutions.append(board)
            printBoard(board)
        return
    
    x, y = cell
    for i in range(1,10):
        # if i is valid at cell in board, go to next empty cell (recursively)
        if isvalid(board, i, cell):
            board[x][y] = i

            # try filling next empty cell till successful
            solveX(board)

            # i is invalid in cell, try i+1
            board[x][y] = 0
    
    # board can't be solved
    return

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

    many_sols = [
        [0,8,0,  0,0,9,  7,4,3],
        [0,5,0,  0,0,8,  0,1,0],
        [0,1,0,  0,0,0,  0,0,0],

        [8,0,0,  0,0,5,  0,0,0],
        [0,0,0,  8,0,4,  0,0,0],
        [0,0,0,  3,0,0,  0,0,6],

        [0,0,0,  0,0,0,  0,7,0],
        [0,3,0,  5,0,0,  0,8,0],
        [9,7,2,  4,0,0,  0,5,0]
    ]

    ms = [
        [5,3,0,  0,7,0,  0,0,0],
        [6,0,0,  1,0,5,  0,0,0],
        [0,9,8,  0,0,0,  0,6,0],

        [8,0,0,  0,0,0,  0,0,3],
        [4,0,0,  8,0,3,  0,0,1],
        [7,0,0,  0,2,0,  0,0,6],

        [0,6,0,  0,0,0,  2,8,0],
        [0,0,0,  4,1,9,  0,0,5],
        [0,0,0,  0,8,0,  0,7,9]
    ]

    solved = solve(board)
    if solved:
        printBoard(ms)
    else:
        print("Unsolvable!")

    # still doesn't work as meant
    # shows repeated solutions for many_sols
    # solveX(many_sols)
    # for sol in solutions:
    #     printBoard(sol)

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
