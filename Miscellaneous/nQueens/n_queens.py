__version__ = "1.0"     # ultra-naive

class NQueens():
    def __init__(self):
        self.n = 0
        self.N = 0
        self.occupied = []
        self.squares = set()

    def setParams(self, n):
        self.n = n
        self.N = n
        self.occupied = []  # nxn board
        self.squares = {(x,y) for y in range(n) for x in range(n)}
        # self.available = [[1]*n for _ in range(n)]  # nxn board

    def findAvailable(self):
        attacked = set()
        for square in self.occupied:
            attacked |= self.findAttackingSquares(*square)
        return self.squares - attacked
    
    def findAttackingSquares(self, x,y):
        # add the row and column to the attacking squares list
        squares = {(i,y) for i in range(self.n)} | {(x,j) for j in range(self.n)}

        # add diagonals to the list now    
        # TL-BR diagonal (lower than (x,y))
        tempX, tempY = x, y
        while tempX<self.n and tempY<self.n:
            squares |= {(tempX,tempY)}
            tempX += 1
            tempY += 1
        # TL-BR diagonal (above (x,y))
        tempX, tempY = x, y
        while -1<tempX and -1<tempY:
            squares |= {(tempX,tempY)}
            tempX -= 1
            tempY -= 1
        # BL-TR diagonal (lower than (x,y))
        tempX, tempY = x, y
        while -1<tempX and tempY<self.n:
            squares |= {(tempX,tempY)}
            tempX -= 1
            tempY += 1
        # BL-TR diagonal (above (x,y))
        tempX, tempY = x, y
        while tempX<self.n and -1<tempY:
            squares |= {(tempX,tempY)}
            tempX += 1
            tempY -= 1
        
        return squares

    def isvalid(self, x,y):
        if (x,y) in self.findAvailable():
            return True
        return False

    # Returns True if solved else False
    def solve(self):
        if self.N == 0:
            return True
        
        for avail in self.findAvailable():
            # self.printBoard(self.findAvailable()); print(); self.printBoard(); input()
            if avail is None:
                return False

            self.occupied.append(avail)
            self.N -= 1
            if self.solve():
                return True
            self.occupied.remove(avail)
            self.N += 1

        return False

    def printBoard(self, squares=None):
        if squares is None:
            squares = self.occupied
        
        board_string = '+' + ("+---"*n)[1:] + "+\n"
        for x in range(self.n):
            for y in range(self.n):
                if (x,y) in squares: elem = '| + '
                else: elem = '|   '                
                board_string += elem
            board_string += '|\n'
            board_string += '+' + ("+---"*n)[1:] + "+\n"

        print(board_string)

if __name__ == "__main__":
    n = int(input("> "))
    nq = NQueens()
    nq.setParams(n)
    nq.solve()
    nq.printBoard()