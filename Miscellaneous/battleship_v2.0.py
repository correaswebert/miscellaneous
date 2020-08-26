from random import randint, randrange
import os, time

# ==============================================================================

# creates a  b_size-1 x b_size-1  sqaure board
b_size = 10
def makeBoard(b_size=5):
	board = [ [i] + ['~']*b_size for i in range(b_size+1) ]
	board[0] = list(range(b_size+1))
	board[0][0] = ' '
	return board

def draw(board):
    os.system("cls")
    for line in board:
            for char in line:
                    print(char, end='\t')
            print('\n')

board = makeBoard(b_size)
draw(board)
			
# ==============================================================================

# # def shipLoc():
	# # row = randint(1, b_size-1)
	# # col = randint(1, b_size-1)
	# # return (row, col)

# # row, col = shipLoc()
# # print(row, col)

# # loc -> (row, col)
# # returns True if loc is in board
# def inBoard(row, col):
    # in_row = 0 < row <= b_size
    # in_col = 0 < col <= b_size
    # return in_row and in_col

# avail = [ [True]*(b_size) ] * (b_size)
# def isAvail(row, col):
    # return avail[row][col]

# def changeCurrentStat(row, col):
    # avail[row][col] = False

# def changeAroundStat(loc):
    # for i in range(-1,2):
        # for j in range(-1,2):
            # try: avail[loc[0]+i][loc[1]+j] = False
            # except: None


# ship_loc_ls = []
# # create a valid ship location
# def createShipLoc(ship_size):
    # ship = []

    # # starting position
    # while True:    
        # start_row = randint(1,b_size-1)
        # start_col = randint(1,b_size-1)
        # if isAvail(start_row, start_col):    
            # ship.append((start_row, start_col))
            # break

    # for part in range(ship_size-1):
        # next_pos = randint(0,3)
        # # up
        # if next_pos == 0:
            # if inBoard( start_row-1, start_col ):
                # ship.append( (start_row-1, start_col) )
                # changeStat( start_row-1, start_col )
        
        # # right
        # if next_pos == 1:
            # if inBoard( start_row, start_col+1 ):
                # ship.append( (start_row, start_col+1) )
                # changeStat( start_row, start_col+1 )

        # # down
        # if next_pos == 2:
            # if inBoard( start_row+1, start_col ):
                # ship.append( (start_row+1, start_col) )
                # changeStat( start_row+1, start_col )

        # # left
        # if next_pos == 3:
            # if inBoard( start_row, start_col-1 ):
                # ship.append( (start_row, start_col-1) )
                # changeStat( start_row, start_col-1 )

    # for loc in ship:
        # changeAroundStat(loc)

    # return ship


# while len(ship_loc_ls) != 5:
    # ship_loc_ls.append(createShipLoc(1))
    # for pos in ship_loc_ls:
        # print(pos)

# print(ship_loc_ls)

# board = makeBoard(b_size)
# for line in ship_loc_ls:
    # for pos in line:
        # board[pos[0]][pos[1]] = "X"
    

# # MAIN Game
# chances = 5
# for turn in range(chances):
    # draw(board)
    # print("You have %d chances left.\n" % (chances-turn))

    # try:
        # guess_row = int(input("Enter row: "))
        # guess_col = int(input("Enter col: "))
    # except ValueError:
        # print("Enter a number!")

    # if guess_col == col and guess_row == row:
        # print("\nYou sunk the battle-ship")
        # print("You win!")
        # break

    # elif not(0 < guess_row <= b_size and 0 < guess_col <= b_size):
        # print("Enter number within the board!")

    # else:
        # print("\nBattle-ship is safe, missed.")
        # board[guess_row][guess_col] = "O"

    # time.sleep(0.75)


# os.system("clear")
# print("Game over!")






















avail = [i for i in range(100)]
locLs = []

def getLoc():
	pos = avail.pop(randrange(len(avail)))
	
	surround = [pos-11, pos-10, pos-9,
				pos-1 ,         pos+1,
				pos+9 , pos+10, pos+11]
	
	for direc in surround:
		try:	avail.remove(direc)
		except:	pass
	
	return pos
	
for i in range(5):
	locLs.append(getLoc())
	
print(locLs)