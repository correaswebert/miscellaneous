# terminal based 2048 game
import os
import random
from copy import deepcopy


class Game:

    def __init__(self):
        self.board = [[0] * 4 for i in range(4)]        # 4x4 board
        self.highest = 0
        self.points = 0

        x1, y1 = random.randint(0, 3), random.randint(0, 3)
        x2, y2 = random.randint(0, 3), random.randint(0, 3)

        self.board[x1][y1] = 2
        self.board[x2][y2] = 2

    def emptyCells(self):
        empty_cells = []
        for x in range(4):
            for y in range(4):
                if self.board[x][y] == 0:
                    empty_cells.append((x, y))
        return empty_cells

    """
    00  01  02  03        30  20  10  00
    10  11  12  13        31  21  11  01
    20  21  22  23        32  22  12  02
    30  31  32  33        33  23  13  03
    """
    # so that only moveRight logic required
    # repeat clockwise movement to achieve other directional movement

    def rotateClockwise(self):
        new_board = [[0 for y in range(4)] for x in range(4)]
        new_board[0][3] = self.board[0][0]
        new_board[1][3] = self.board[0][1]
        new_board[2][3] = self.board[0][2]
        new_board[3][3] = self.board[0][3]

        new_board[0][2] = self.board[1][0]
        new_board[1][2] = self.board[1][1]
        new_board[2][2] = self.board[1][2]
        new_board[3][2] = self.board[1][3]

        new_board[0][1] = self.board[2][0]
        new_board[1][1] = self.board[2][1]
        new_board[2][1] = self.board[2][2]
        new_board[3][1] = self.board[2][3]

        new_board[0][0] = self.board[3][0]
        new_board[1][0] = self.board[3][1]
        new_board[2][0] = self.board[3][2]
        new_board[3][0] = self.board[3][3]

        self.board = new_board

    """swipe right ;)
    .  .  2  2      .  .  .  4      
    2  2  2  .      .  .  2  4
    4  8  .  .      .  .  4  8
    .  2  .  2      .  .  .  4
    """

    def moveRight(self):
        state_changed = False   # if state doesn't change, don't create new tile
        for x in range(4):
            row = self.board[x]
            # shift existing cells to the right in case of empty cells
            # this removes many extra cases to be encountered otherwise
            # ranges indicate max number or tries to remove empty cells
            # special cases don't allow to use while loop, hence for-break
            for _ in range(3):
                if row[3] != 0:
                    break
                row[3] = row[2]
                row[2] = row[1]
                row[1] = row[0]
                row[0] = 0
                state_changed = True
            for _ in range(2):
                if row[2] != 0:
                    break
                row[2] = row[1]
                row[1] = row[0]
                row[0] = 0
                state_changed = True
            if row[1] == 0:
                row[1] = row[0]
                row[0] = 0
                state_changed = True

            # priority-wise end cells get more priority
            # as in example's row 2: c2 & c3 get priority over c1 & c2
            # update c_i as new values may cause problems while if-comparing
            c1, c2, c3, c4 = row
            if c4 == c3:
                self.points += c3 + c4
                row[3] = c3 + c4
                row[2] = c2
                row[1] = c1
                row[0] = 0
                state_changed = True

            c1, c2, c3, c4 = row
            if c3 == c2:
                self.points += c2 + c3
                row[2] = c2 + c3
                row[1] = c1
                row[0] = 0
                state_changed = True

            c1, c2, c3, c4 = row
            if c2 == c1:
                self.points += c1 + c2
                row[1] = c1 + c2
                row[0] = 0
                state_changed = True

            # BUG: does't work ... example board
            # row = deepcopy(self.board[x])     # instead of simply referencing
            # [0, 0, 0, 2],
            # [0, 0, 0, 2],
            # [0, 0, 0, 2],
            # [0, 4, 8, 2]
            # if self.board[x] == row:
            #     state_changed = True

            # update the highest value
            self.highest = max(self.highest, max(row))
            # self.board[x] = row               # if deepcopy used
        return state_changed

    def moveUp(self):
        self.rotateClockwise()
        state_changed = self.moveRight()
        # rotate anti-clockwise
        self.rotateClockwise()
        self.rotateClockwise()
        self.rotateClockwise()
        return state_changed

    def moveLeft(self):
        # rotate 180
        self.rotateClockwise()
        self.rotateClockwise()
        state_changed = self.moveRight()
        # rotate 180
        self.rotateClockwise()
        self.rotateClockwise()
        return state_changed

    def moveDown(self):
        # rotate anti-clockwise
        self.rotateClockwise()
        self.rotateClockwise()
        self.rotateClockwise()
        state_changed = self.moveRight()
        self.rotateClockwise()
        return state_changed

    def nextNumber(self):
        probability = random.random()

        # 1% probability of 4
        if self.highest <= 256:
            if 0 <= probability < 0.01:
                return 4
            return 2

        #  5% probability of 8
        # 30% probability of 4
        if self.highest <= 1024:
            if 0 <= probability < 0.05:
                return 8
            elif 0.7 <= probability < 1:
                return 4
            return 2

    def createTile(self):
        empty_cells = self.emptyCells()
        # if there are no empty_cells (None) then end function
        # random.choice(None) returns error
        if not empty_cells:
            return

        x, y = random.choice(empty_cells)
        self.board[x][y] = self.nextNumber()

    def isGameOver(self):
        # if there are empty cells, we can fill them
        if self.emptyCells():
            return False

        # copy original board
        player_board = deepcopy(self.board)
        game_over = False

        # try to move in R & U directions
        # L & R and U & D movements are equivalent in full board
        # just the board outcome is mirrored
        # if board doesn't change, then Game Over!

        self.moveUp()
        self.moveRight()
        if player_board == self.board:
            game_over = True
        else:
            game_over = False
        self.board = deepcopy(player_board)

        return game_over

    """
    +----+----+----+----+
    |2048|    |    |    |
    +----+----+----+----+
    |    |  8 |    |    |
    +----+----+----+----+
    |    |  2 | 16 |    |
    +----+----+----+----+
    |  2 |    |    | 512|
    +----+----+----+----+
    """

    def __str__(self):
        board_string = f"SCORE: {self.points}   HIGHEST TILE: {self.highest}\n\n"
        for row in self.board:
            board_string += "+----+----+----+----+\n|"
            for elem in row:
                elem_str = '' if elem == 0 else str(elem)
                if elem // 100 == 0:
                    board_string += elem_str.rjust(3, ' ') + ' |'
                else:
                    board_string += elem_str.rjust(4, ' ') + '|'
            board_string += '\n'
        board_string += "+----+----+----+----+\n"
        return board_string


def test():
    game = Game()
    game.board = [
        [0, 0, 0, 2],
        [0, 0, 0, 2],
        [0, 0, 0, 2],
        [0, 4, 8, 2]
    ]
    # print(game)
    # game.moveDown()
    # print(game)

    # direction_map = {
    #     '2': 2, '4': 4, '6': 6, '8': 8,
    #     's': 2, 'a': 4, 'd': 6, 'w': 8,
    # }
    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(game)

        if game.isGameOver():
            print("Game Over")
            break

        # try:
        #     direction = direction_map[input()]
        # except:
        #     continue              # don't create new tile for faaulty input
        # direction = random.choice((2,4))
        direction = input()
        if direction == 's':
            state_changed = game.moveDown()
        elif direction == 'a':
            state_changed = game.moveLeft()
        elif direction == 'w':
            state_changed = game.moveUp()
        elif direction == 'd':
            state_changed = game.moveRight()
        elif direction == '0':
            break
        else:
            continue

        if state_changed:
            game.createTile()


test()
