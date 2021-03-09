"""
Definitions of each of the different chess pieces.
"""

from abc import ABC, abstractmethod

from chessington.engine.data import Player, Square

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board):
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """

    def get_available_moves(self, board):
        position = board.find_piece(self)
        piece = board.get_piece(position)
        moves = []
        if piece.player == Player.WHITE:
            direction = 1
            start_row = 1
        elif piece.player == Player.BLACK:
            direction = -1
            start_row = 6

        move = Square.at(position.row + direction, position.col)
        if board.check_square_is_available(move):
            moves.append(move)
            if position.row == start_row:
                move = Square.at(position.row + 2 * direction, position.col)
                if board.check_square_is_available(move):
                    moves.append(move)

        capture_moves = [
            Square.at(position.row + direction, position.col + direction),
            Square.at(position.row + direction, position.col - direction)
        ]
        for move in capture_moves:
            if board.check_square_has_opponent_piece(move, piece.player):
                moves.append(move)

        return moves


class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        position = board.find_piece(self)
        piece = board.get_piece(position)
        directions = [-1, 0, 1]
        moves = []
        for i in directions:
            for j in directions:
                move = Square.at(position.row + i, position.col + j)
                if (board.check_square_is_available(move) or 
                board.check_square_has_opponent_piece(move, piece.player)):
                    moves.append(move)

        return moves
