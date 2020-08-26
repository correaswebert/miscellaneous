import os
from random import randrange, choice

actions = {'w': "Up", 'a': "Left", 's': "Down", 'd': "Right"}


def transpose(field):
    """flip the game field about the TL-BR diagonal"""
    return [list(row) for row in zip(*field)]


def invert(field):
    """flip the game field about the y-axis"""
    return [row[::-1] for row in field]


class GameField(object):
    def __init__(self, height=4, width=4, win=2048):
        self.height = height        # number of rows
        self.width = width          # number of cols
        self.win_value = win
        self.score = 0
        self.reset()

    def reset(self):
        self.score = 0
        self.field = [[0]*self.width for i in range(self.height)]
        self.spawn()
        # self.spawn()

    @staticmethod
    def move_row_left_new(row):
        """make a left swipe in 2048

        tighten
        squeese non-zero elements together
        in:  [2,0,3,0,0,1]
        out: [2,3,1,0,0,0]

        merge
        if two consecutive elements are equal
        then zero the first element and double the second
        else the element remains untouched
        in:  [2,2,4,8, 8,4]
        out: [0,4,4,0,16,4]

        procedure: tighten -> merge -> tighten
        """

        og_len_row = len(row)

        row = [i for i in row if i != 0]
        row += [0] * (og_len_row - len(row))

        pair = False    # if two consecutive elements are equal, set to True
        new_row = []
        for i in range(og_len_row):
            if pair:
                row[i] *= 2
                self.score += 2 * row[i]
                pair = False
            elif i + 1 < len(row) and row[i] == row[i + 1]:
                pair = True
                row[i] = 0

        assert len(new_row) == len(row)

        row = [i for i in row if i != 0]
        row += [0] * (og_len_row - len(row))

        return row

    def move(self, direction):
        def move_row_left(row):
            # squeese non-zero elements together
            #  in: [2,0,3,0,0,1]
            # out: [2,3,1,0,0,0]

            def tighten(row):
                new_row = [i for i in row if i != 0]
                new_row += [0] * (len(row) - len(new_row))
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
        moves['Left'] = lambda field:                       \
            [move_row_left(row) for row in field]
        moves['Right'] = lambda field:                      \
            invert(moves['Left'](invert(field)))
        moves['Up'] = lambda field:                         \
            transpose(moves['Left'](transpose(field)))
        moves['Down'] = lambda field:                       \
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
                         for j in range(self.height) if self.field[i][j] == 0])
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
        check['Left'] = lambda field:						    \
            any(row_is_left_movable(row) for row in field)

        check['Right'] = lambda field:							\
            check['Left'](invert(field))

        check['Up'] = lambda field:					            \
            check['Left'](transpose(field))

        check['Down'] = lambda field:							\
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


def main():
    game_field = GameField(win=32)
    continue_game = True

    while True:
        os.system("cls")
        print("Up (W) | Right (D) | Down (S) | Left (A)", end="\n\n")
        print(game_field)

        try:
            action = actions[input()]
        except KeyError:
            continue

        if game_field.move(action):  # move successful
            if continue_game and game_field.is_win():
                print('Win')
                if input("Continue? (y/n)\n>>> ").lower() == 'n':
                    break
            if game_field.is_gameover():
                print('Gameover')
                break


if __name__ == "__main__":
    main()
