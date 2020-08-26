def isvalid(N, board, x,y):
    """
    Only check for previous col's rows and left-side diagonals...
    Queens are placed 1st col onwards, hence no attacks from right-side
    No attack from current col as queen is shifted from top to bottom
    """
    # check row (traverse the row, hence x is const)
    for j in range(y):
        if board[x][j] == 1:
            return False
    
    # check diagonals (U:upper | L:lower)
    for i,j in zip(range(x,-1,-1), range(y,-1,-1)):
        if board[i][j] == 1:
            return False
    for i,j in zip(range(x,N,1), range(y,-1,-1)):
        if board[i][j] == 1:
            return False
    
    return True

# reference to board is passed, hence original board is altered to the solution
def solve(N, board, col=0):
    """Choose a col, then start placing queen in each row of that col"""
    # if col to place the queen is outside the board, all queens are placed
    if col >= N:
        return True
    
    # try placing queen in every row of that col
    for i in range(N):
        if isvalid(N, board, i,col):
            board[i][col] = 1       # queen safely placed

            if solve(N, board, col+1):
                return True
            
            # during further analysis of this position, problem can't be
            # solved, so revert to previous state and continue loop
            board[i][col] = 0
    
    # all positions tried, but no solution found
    return False

def printBoard(board):
    for row in board:
        for elem in row:
            print(elem, end=' ')
        print()

if __name__ == "__main__":
    n = int(input("Enter size of board: "))
    board = [[0]*n for _ in range(n)]
    solve(n, board)
    printBoard(board)