class Player():
    """Instantiates a human player or a computer player object"""
    def __init__(self, name, board, color):
        self.name = name
        self.board = board
        self.color = color

    def has_legal_move(self):
        return self.board.has_legal_move(self.color)

    def move(self, x, y, flips):
        self.board.add_tile(x, y, self.color)
        self.board.flip(flips, self.color)
        # place the tile on the board and flips the tiles
