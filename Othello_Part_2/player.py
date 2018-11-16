from board import Board

class Player():
    """Instantiates a human player or a computer player object"""
    def __init__(self, name, board, color):
        self.name = name
        self.board = board
        self.color = color

    def move(self, x, y):
        self.board.add_tile((x, y), self.color)
        # place the tile on the board, does not flip at the moment
        # self.board.flip()