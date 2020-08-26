# Sudoku solver
# Recursive solver used from
# https://techwithtim.net/tutorials/python-programming/sudoku-solver-backtracking/
# Non-recursive implementation my own

import os
import timeit

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

# Returns (x,y)
def firstEmptyCell(board):
    """Returns first occurence of an empty cell"""
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)  # row, col
    return None

# ---------------------------------------------------------------------------- #

class SudokuSolver():
    
    def __init__(self, board):
        self.board = board
        self.ITERATIONS = 0

    def isvalid(self, num, cell):
        """Checks if num can be validly placed at cell"""
        x, y = cell
        row = self.board[x]
        col = transpose(self.board)[y]

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
                if self.board[i][j] == num:
                    return False
        
        return True

    def solveNotRecursively(self):
        empty_cells = findEmptyCells(self.board)

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
            next_val = self.board[x][y] + 1
            if next_val == 10:
                self.board[x][y] = 0
                i -= 1
                continue
            
            for k in range(next_val, 10):
                self.ITERATIONS += 1
                if self.isvalid(k, (x,y)):
                    self.board[x][y] = k
                    i += 1
                    break
                # all values 1-9 don't work, empty cell and go to prev
                elif k == 9:
                    self.board[x][y] = 0
                    i -= 1
                    break

    def solveRecursively(self):
        cell = firstEmptyCell(board)
        # Base case for recursion
        # no empty cells, also all other cells filled validly, so board solved
        if cell is None:
            return True
        
        x, y = cell
        for i in range(1,10):
            self.ITERATIONS += 1
            # if i is valid at cell in board, go to next empty cell (recursively)
            if self.isvalid(i, cell):
                self.board[x][y] = i

                # try filling next empty cell till successful
                if self.solveRecursively():
                    return True

                # i is invalid in cell, try i+1
                self.board[x][y] = 0
        
        # board can't be solved
        return False

    def solve(self, recursive=False):
        if recursive:
            return self.solveRecursively()
        return self.solveNotRecursively()

    def printBoard(self):
        board_string = ""

        for x in range(9):
            if x == 3 or x == 6:
                board_string += "------+-------+------\n"
            for y in range(9):
                if y == 3 or y == 6:
                    board_string += "| "
                char = self.board[x][y]
                char = str(char) if char != 0 else ' '
                board_string += char + ' '
            board_string += '\n'
        
        print(board_string)

# ---------------------------------------------------------------------------- #

board = [
    [8,0,0,0,0,0,0,0,0],
    [0,0,3,6,0,0,0,0,0],
    [0,7,0,0,9,0,2,0,0],
    [0,5,0,0,0,7,0,0,0],
    [0,0,0,0,4,5,7,0,0],
    [0,0,0,1,0,0,0,3,0],
    [0,0,1,0,0,0,0,6,8],
    [0,0,8,5,0,0,0,1,0],
    [0,9,0,0,0,0,4,0,0]]
solver = SudokuSolver(board)

# Time comparisons
# timeit.timeit('solver.solve(recursive=True)', setup="from __main__ import solver", number=1)

# recursive_time = timeit.timeit("solver.solve(recursive=True)",
#                             setup="from __main__ import solver", number=10000)
# nonrecursive_time = timeit.timeit("solver.solve(recursive=False)",
#                             setup="from __main__ import solver", number=10000)

# print("Time taken to solve the sudoku puzzle 10000 times")
# print("    Recursive method: ", recursive_time)
# print("Non-recursive method: ", nonrecursive_time)
# print("The solution is ...")
# solver.printBoard()

solver.solveNotRecursively()
print("Non-Recursive:", solver.ITERATIONS)
solver.ITERATIONS = 0
solver.solveRecursively()
print("    Recursive:", solver.ITERATIONS)


"""answer
7 8 5  | 4 3 9  | 1 2 6
6 1 2  | 8 7 5  | 3 4 9
4 9 3  | 6 2 1  | 5 7 8
- - - - - - - - - - - - 
8 5 7  | 9 4 3  | 2 6 1
2 6 1  | 7 5 8  | 9 3 4
9 3 4  | 1 6 2  | 7 8 5
- - - - - - - - - - - - 
5 7 8  | 3 9 4  | 6 1 2
1 2 6  | 5 8 7  | 4 9 3
3 4 9  | 2 1 6  | 8 5 7
"""