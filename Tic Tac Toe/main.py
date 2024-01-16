# This is a sample Python script.
from TicTacToeGame import TicTacToeGame


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def main():
    game: TicTacToeGame = TicTacToeGame()
    game.initialize_game()
    print(f"Game winner is: {game.start_game()}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
