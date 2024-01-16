from collections import deque
from typing import List, Tuple

from model.Board import Board
from model.PieceType import PieceType
from model.Player import Player
from model.PlayingPieceO import PlayingPieceO
from model.PlayingPieceX import PlayingPieceX


class TicTacToeGame:
    players = deque()
    gameBoard: Board

    def initialize_game(self):

        crossPiece: PlayingPieceX = PlayingPieceX()
        player1: Player = Player("Player1", crossPiece)

        noughtsPiece: PlayingPieceO = PlayingPieceO()
        player2: Player = Player("Player2", noughtsPiece)

        self.players.append(player1)
        self.players.append(player2)

        self.gameBoard = Board(3)

    def start_game(self) -> str:

        noWinner: bool = True

        while (noWinner):
            playerTurn: Player = self.players.popleft()

            self.gameBoard.print_board()

            free_spaces: List[Tuple[int, int]] = self.gameBoard.get_free_cells()
            if not free_spaces:
                noWinner = False
                continue

            print(f"Player: {playerTurn.name} Enter row, column: ")
            user_input: str = input()
            values: list[str] = user_input.split(",")
            input_row: int = int(values[0])
            input_column: int = int(values[1])

            pieceAddedSuccessfully: bool = self.gameBoard.add_piece(input_row, input_column, playerTurn.playing_piece)

            if not pieceAddedSuccessfully:
                print(f"Incorrect position chosen, try again")
                self.players.appendleft(playerTurn)
                continue

            self.players.append(playerTurn)

            winner: bool = self.is_there_winner(input_row, input_column, playerTurn.playing_piece.piece_type)

            if winner:
                return playerTurn.name

        return "tie"

    def is_there_winner(self, row: int, column: int, piece_type: PieceType) -> bool:
        row_match: bool = True
        column_match: bool = True
        diagonal_match: bool = True
        anti_diagonal_match: bool = True

        for i in range(self.gameBoard.size):
            if self.gameBoard.board[row][i] is None or self.gameBoard.board[row][i].piece_type != piece_type:
                row_match = False

        for i in range(self.gameBoard.size):
            if self.gameBoard.board[i][column] is None or self.gameBoard.board[i][column].piece_type != piece_type:
                column_match = False

        for i in range(self.gameBoard.size):
            j: int = i
            if self.gameBoard.board[i][j] is None or self.gameBoard.board[i][j].piece_type != piece_type:
                diagonal_match = False

        for i in range(self.gameBoard.size):
            j: int = self.gameBoard.size - i - 1
            if self.gameBoard.board[i][j] is None or self.gameBoard.board[i][j].piece_type != piece_type:
                anti_diagonal_match = False

        return row_match or column_match or diagonal_match or anti_diagonal_match
