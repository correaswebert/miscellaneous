# 2048 A.I.
# v1.0

# main strategy
# move in only 2 directions as much as possible
# jam the highest value in the corner
# try to make more points and reduce the number of tiles (heuristic motif)

# decision making junctures

"""
DOWN is better
RIGHT would jam the 2 in between 4 & 8(4+4)
.  .  .  4
.  .  2  .
.  .  4  4
.  .  8 16
"""

"""
RIGHT is better 
DOWN would prevent the 4 + 4
Chance to be taken as new 2 can be generated between the 4s
.  .  .  4
.  .  .  .
.  2  2  4
.  .  8 16
"""

"""
DOWN is better
RIGHT would jam the 2 in between 4 & 8
.  4  .  .  
.  .  2  .
.  .  4  8
.  .  8 16
"""

"""
RIGHT is better
DOWN would unblock the 'locked' bottom row (as RIGHT would be next)
.  .  .  .
.  .  .  4
.  4  4  8
2  4  8 16
"""

"""
RANDOM move (RIGHT/DOWN)
DOWN slightly favored as all blocks limited to bottom 2 rows
.  .  .  .
.  .  .  4
.  .  4  4
2  4  8 32
"""

"""
DOWN is better as 2 would not be generated between 4 & 8
.  .  .  4
.  .  .  .
.  .  4  8
2  . 16 32
"""

"""
DOWN is better
LEFT (firstly is not necessary as D|R rule-wise D available) would put 2 at R3C4
this will cause inconvinience as 16 will next combine with 32
.  .  .  2
.  .  .  .
.  .  4 16
2  4 16 32
"""

"""
LEFT is better
RIGHT is possible but ...
(2 + 2) + 4 possible with LEFT
with RIGHT only (2 + 2) possible
.  .  .  .
.  2  .  .
2  8  .  2
4 16 32 64
"""

"""
DOWN is better
D|R both lead to 64 creation
but DOWN will add the 2, 2, 4 in 1st 2 rows on the way to 64 creation
.  .  2   .
.  4  .   2
8  8 16   8
8 16 32 128
"""

"""
DOWN is better
both D|R lead to 2 + 2 = 4
but DOWN will lock bottom row with higher value 4 than 2 with  RIGHT
.  .  .   .
2  .  .   2
.  8  4  32
2 16 64 128
"""

"""
DOWN is better
(4 + 4) + 8 possible but not with RIGHT
"""

from random import randrange, choice # generate and place new tile
import os
actions = {'w': "Up", 'a': "Left", 's': "Down", 'd': "Right"}


def transpose(field):
    # return list(*zip(field))                    # return list of tuples
    return [list(row) for row in zip(*field)]   # return list of lists


def invert(field):
    return [row[::-1] for row in field]


class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height
        self.width = width
        self.win_value = win
        self.reset()

    def reset(self):
        self.score = 0
        self.field = [[0]*self.width for i in range(self.height)]
        self.spawn()
        self.spawn()

    def move(self, direction):
        def move_row_left(row):
            # squeese non-zero elements together
            #  in: [2,0,3,0,0,1]
            # out: [2,3,1,0,0,0]
            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0 for i in range(len(row) - len(new_row))]
                return new_row
            # if two consecutive elements are equal
            # then make the first element 0
            # and double the second element
            # else the element remains untouched
            #  in: [2,2,4,8, 8,4]
            # out: [0,4,4,0,16,4]

            def merge(row):
                # if two consecutive elements are equal, set to True
                pair = False
                new_row = []
                for i in range(len(row)):
                    if pair:
                        new_row.append(2 * row[i])
                        self.score += 2 * row[i]
                        pair = False
                    else:
                        if i + 1 < len(row) and row[i] == row[i + 1]:
                            pair = True
                            new_row.append(0)
                        else:
                            new_row.append(row[i])
                assert len(new_row) == len(row)
                return new_row
            return tighten(merge(tighten(row)))

        moves = {}
        moves['Left'] = lambda field:                          \
            [move_row_left(row) for row in field]
        moves['Right'] = lambda field:                          \
            invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field:                          \
            transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field:                          \
            transpose(moves['Right'](transpose(field)))

        if direction not in moves:
            return False
        if self.move_is_possible(direction):
            self.field = moves[direction](self.field)
            self.spawn()
            return True

    def is_win(self):
        return any(max(row) >= self.win_value for row in self.field)

    def is_gameover(self):
        return not any(self.move_is_possible(move) for move in actions)

    def spawn(self):
        # 10% chance of 4
        new_element = 4 if randrange(100) > 89 else 2
        (i, j) = choice([(i, j) for i in range(self.width)
                         for j in range(self.height)
                         if self.field[i][j] == 0])
        self.field[i][j] = new_element

    def move_is_possible(self, direction):
        for row in self.field:
            if min(row) == 0:
                return True

        def row_is_left_movable(row):
            for i in range(len(row)):
                if row[i] == row[i + 1] != 0:  # Merge
                    return True
                return False

        check = {}
        check['Left'] = lambda field:								\
            any(row_is_left_movable(row) for row in field)

        check['Right'] = lambda field:								\
            check['Left'](invert(field))

        check['Up'] = lambda field:								\
            check['Left'](transpose(field))

        check['Down'] = lambda field:								\
            check['Right'](transpose(field))

        if direction not in check:
            return False
        return check[direction](self.field)

    def __str__(self):
        board_string = f"SCORE: {self.score}\n\n"
        for row in self.field:
            board_string += '+' + ("+----" * self.width)[1:] + "+\n|"
            for elem in row:
                elem_str = '' if elem == 0 else str(elem)
                if elem // 100 == 0:
                    board_string += elem_str.rjust(3, ' ') + ' |'
                else:
                    board_string += elem_str.rjust(4, ' ') + '|'
            board_string += '\n'
        board_string += '+' + ("+----" * self.width)[1:] + '+'
        return board_string


class AI(GameField):
    def __init__(self):
        super().__init__()

    def evaluateBoard(self, board):
        pass

    # expectimax with only one player (expect max output)
    def expectimax(self, board, depth, chance=False):
        pass


def main():
    game_field = GameField(win=32)
    end_game = False

    auto_input = input("Automatic? (y/n) >>> ") == 'y'

    while True:
        os.system("cls" if os.name == "nt" else "clear")
        print(game_field)

        action = actions[choice(['w', 'a', 's', 'd'])
                         ] if auto_input else actions[input()]

        if game_field.move(action):  # move successful
            if game_field.is_win() and not end_game:
                print('Win')
                end_game = input("Do you wish to exit? (y/n) >>> ") == 'n'
                if not end_game:
                    break
            if game_field.is_gameover():
                print('Gameover')
                break


main()
