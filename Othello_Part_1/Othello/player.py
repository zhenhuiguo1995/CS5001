from board import Board


class Player():
    """Instantiates a human player or a computer player object"""
    def __init__(self, name, board, color):
        self.name = name
        self.board = board
        self.color = color

    def move(self, x, y):
        """Given two integers representing the coordinates of a tile
        make a move and place a tile on the board.
        Integer Integer -> None"""
        # place the tile on the board, does not flip at the moment
        self.board.add_tile((x, y), self.color)
