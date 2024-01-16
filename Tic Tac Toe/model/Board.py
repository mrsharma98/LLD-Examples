from typing import List, Optional, Tuple

from model.PlayingPiece import PlayingPiece


class Board:

    def __init__(self, size: int):
        self.size = size
        self.board = [[None for _ in range(size)] for _ in range(size)]

    def add_piece(self, row: int, column: int, playing_piece: PlayingPiece) -> bool:
        if self.board[row][column] is not None:
            return False

        self.board[row][column] = playing_piece
        return True

    def get_free_cells(self) -> List[Tuple[int, int]]:
        free_cells: List[Tuple[int, int]] = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    rowColum: Tuple[int, int] = (i, j)
                    free_cells.append(rowColum)

        return free_cells

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is not None:
                    print(f"{self.board[i][j].piece_type.name}   ", end=" | ")
                else:
                    print("    ", end=" | ")
            print()
