class Player():
    """Instantiates a human player or a computer player object"""
    def __init__(self, name, board, color):
        self.name = name
        self.board = board
        self.color = color

    def has_legal_move(self):
        """Return a boolean value representing if the player has a
        legal move or not."""
        return self.board.has_legal_move(self.color)

    def move(self, x, y, flips):
        """Given two Integers and a set, return nothing.
        Player make a move."""
        self.board.add_tile(x, y, self.color)
        self.board.flip(flips, self.color)
