from random import randint

TILESIZE  = 20
MAPHEIGHT = 10
MAPWIDTH  = 10

board   = [[0 for r in range(5)] for c in range(5)]



def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
print (ship_row)
print (ship_col)

for turn in range(4):

    try:
        guess_row = int(input("Guess Row: "))
        guess_col = int(input("Guess Col: "))

        if guess_row == ship_row and guess_col == ship_col:
            print ("Congratulations! You sunk my battleship!")

            break

        else:
            if (guess_row < 0 or guess_row > 4) or (guess_col < 0     or guess_col > 4):
                print ("Oops, that's not even in the ocean.")
            elif(board[guess_row][guess_col] == "X"):
                print ("You guessed that one already.")
            else:
                print ("You missed my battleship!")


        if turn == 3:

                print ("Game Over.")

        print ("Turn", turn + 1, '\n')

    except ValueError:
        print("Oops, please hit a number!")



# v_2.0


from random import randint

# assumes board is square
size = 5
board = [ ['~' for col in range(size)] for row in range(size)]

def ship_loc():
	row = randint(0, size-1)
	col = randint(0, size-1)
	return (row, col)

s_row, s_col = ship_loc()
# for test purpose only
print(s_row, s_col)


# MAIN Game

for turn in range(5):
	print(board)

	g_row = input("Enter row: ")
	g_col = input("Enter col: ")

	# switch 
