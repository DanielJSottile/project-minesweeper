import random
from typing import Tuple
# import collections


class Board:
    """This object works for the minesweeper board.
    It likely takes some amount of values and creates a new
    board with it.  I dunno."""

    def __init__(self, w, h, b=0, f='', seed=random.seed()):
        self.width = w
        self.height = h
        self.bombs = b
        self.filename = f
        self.seed = seed
        self.data = [['_'] * self.width for _ in range(self.height)]
        self.bomb_data = [['_'] * self.width for _ in range(self.height)]

    def make_rand_coord(self):
        row = random.randrange(0, self.height)
        col = random.randrange(0, self.width)
        cord = (row, col)
        return cord

    def create_bomb_data(self):
        bomb_cord_list = set()
        while len(bomb_cord_list) < self.bombs:
            bomb_cord_list.add(self.make_rand_coord())
        for j in bomb_cord_list:
            self.bomb_data[j[0]][j[1]] = 'B'
        return self.bomb_data

    def print_board(self):
        print('    ', end='')
        for i in range(self.width):
            print(str(i) + ' ', end='')
        print('')
        print('  +-' + ('--' * self.width) + '+')
        for i, row in enumerate(self.data):
            print(str(i) + f' | {" ".join(row)} |')
        print('  +-' + ('--' * self.width) + '+')
        return 0

    def print_bomb_board(self):
        print('    ', end='')
        for i in range(self.width):
            print(str(i) + ' ', end='')
        print('')
        print('  +-' + ('--' * self.width) + '+')
        for i, row in enumerate(self.bomb_data):
            print(str(i) + f' | {" ".join(row)} |')
        print('  +-' + ('--' * self.width) + '+')
        return 0


def enter_integer(s: str) -> int:
    while True:
        input_s = input(s)
        if not input_s.isdigit():
            print("!!! must be a positive integer")
        i = int(input_s)
        if i < 1:
            print("!!! must be a positive integer")
        return i


def make_dimensions() -> Tuple[int, int, int]:
    while True:
        w = enter_integer("****** enter a width:")
        if w > 10:
            print("!!! the board dimension must not be larger than 10")
            continue
        break
    while True:
        h = enter_integer("****** enter a hight:")
        if h > 10:
            print("!!! the board dimension must not be larger than 10")
            continue
        break
    while True:
        b = enter_integer("****** enter the number of bombs:")
        if b >= (w * h) - 9:
            # there must be at least 9 tiles clicked around 1st
            print("!!! number of bombs exceeds the size of the board")
            continue
        break
    return (w, h, b)


def main():

    choice = ''
    while choice != 'q' or choice != 'quit':
        print("\n- (s)tart game")
        print("- (l)oad game")
        print("- seed (r)andom")
        print("- (q)uit (or ^C or ^D)")

        # Ask for the user's choice.
        choice = input("\n*** What would you like to do?\n")

        # Respond to the user's choice.
        if choice == 's' or choice == 'start game':
            # enter prompts
            pass
        elif choice == 'l' or choice == 'load game':
            # enter prompts
            pass
        elif choice == 'r' or choice == 'seed random':
            # enter prompts
            pass
        elif choice == 'q' or choice == 'quit':
            print("\nLeaving the game...Goodbye!\n")
            return 0
        else:
            print("\nIncorrect prompt. Please try again.\n")

    w, h, b = make_dimensions()
    gameboard = Board(w, h, b, f, seed)
    gameboard.print_board()
    gameboard.create_bomb_data()
    gameboard.print_bomb_board()
    return 0


if __name__ == '__main__':
    exit(main())
