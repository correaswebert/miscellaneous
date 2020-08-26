# connect four
import os

BLANK = 0
WHITE = 1
BLACK = -1

transpose = lambda matrix: tuple(zip(*matrix))

# Returns list of lists
def getDiags(board, location=None):
    diagonals = []
    maxH, maxW = len(board[0]), len(board)  # boundary conditinos for board

    def get_TL_BR(startX):
        path = []
        tempX, tempY = startX, 0
        while tempX<maxW and tempY<maxH:
            path.append((tempX, tempY))
            tempX += 1
            tempY += 1
        return path

    def get_BL_TR(startY):
        path = []
        tempX, tempY = 0, startY
        while tempX<maxW and tempY<maxH:
            path.append((tempX, tempY))
            tempX += 1
            tempY -= 1
        return path
    
    # get list of all diagonals
    if location is None:
        for x,y in zip(board[0], transpose(board)[0]):
            diagonals.append(get_TL_BR(x))
            diagonals.append(get_BL_TR(y))
        return diagonals
    
    # get list of diagonals with (x,y) in them
    x, y = location

    path = []
    # TL-BR diagonal (lower than (x,y))
    tempX, tempY = x, y
    while tempX<maxW and tempY<maxH:
        path.append((tempX, tempY))
        tempX += 1
        tempY += 1
    # TL-BR diagonal (above (x,y))
    tempX, tempY = x, y
    while -1<tempX and -1<tempY:
        path.append((tempX, tempY))
        tempX -= 1
        tempY -= 1
    diagonals.append(path)

    path = []
    # BL-TR diagonal (lower than (x,y))
    tempX, tempY = x, y
    while -1<tempX and tempY<maxH:
        path.append((tempX, tempY))
        tempX -= 1
        tempY += 1
    # BL-TR diagonal (above (x,y))
    tempX, tempY = x, y
    while tempX<maxW and -1<tempY:
        path.append((tempX, tempY))
        tempX += 1
        tempY -= 1
    return diagonals

class ConnectFour():
    def __init__(self, rows=7, cols=7, combo=4):
        self.combo = 4      # how many consecutive connectors
        self.height = rows
        self.width = cols
        self.board = [[0]*cols for i in range(rows)]
    
    # Returns disc location if move made, else None
    def move(self, col, player, board=None):
        if board is None:
            board = self.board
        
        i = self.height -1   # start at the bottom and move up until empty, fill
        while board[i][col] != 0 and i > 0:
            i -= 1
        
        # if whole column filled, while won't detect it, just check
        if board[i][col] == 0:
            board[i][col] = player
            return (i, col)
        return None
    
    def iswon(self, player, board=None, location=None):
        if board is None:
            board = self.board
        
        # check row subfunction
        def isconnected(row, player):
            connect_start = False
            combo_made = 0
            for elem in row:
                if elem == player:
                    if connect_start == True and combo_made == self.combo:
                        return True
                    connect_start = True
                    combo_made += 1
                else:
                    combo_made = 0
                    connect_start = False
            return False
        
        boardT = transpose(board)

        # thoroughly check board
        if location is None:
            # check rows and cols simulataneously
            for row, col in zip(board, boardT):
                if isconnected(row, player) or isconnected(col, player):
                    return True
            
            # check diagonals
            for diag in getDiags(board):
                if isconnected(diag, player):
                    return True
            
            return False
        
        # only check for lines with (x,y) in them
        x, y = location
        row, col = board[x], boardT[y]
        if isconnected(row, player) or isconnected(col, player):
            return True
        diag1, diag2 = getDiags(board, location)
        if isconnected(diag1, player) or isconnected(diag2, player):
            return True
        return False

    def getWinner(self):
        if self.iswon(WHITE):
            return WHITE
        if self.iswon(BLACK):
            return BLACK
        return BLANK

    def printBoard(self, board=None):
        if board is None:
            board = self.board
            os.system("cls")
        
        board_string = '+' + ("+---" * self.width)[1:] + "+\n"
        for row in board:
            for elem in row:
                if elem == WHITE: elem = '| + '
                elif elem == BLACK:  elem = '| - '
                else: elem = '|   '
                
                board_string += elem
            board_string += '|\n'
            board_string += '+' + ("+---" * self.width)[1:] + "+\n"

        print(board_string)
                
                

def play():
    game_field = ConnectFour()
    while True:
        winner = game_field.getWinner()
        if winner:
            print(f"{'WHITE' if winner == WHITE else 'BLACK'} won!")
            break
        
        # P1
        game_field.printBoard()
        move = int(input("P1 >>> ")) - 1
        game_field.move(move, WHITE)
        game_field.printBoard()

        # P2
        game_field.printBoard()
        move = int(input("P2 >>> ")) - 1
        game_field.move(move, BLACK)
        game_field.printBoard()
play()