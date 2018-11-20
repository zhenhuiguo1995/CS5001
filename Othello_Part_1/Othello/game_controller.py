class GameController():
    """Controls the flow of the game"""
    def __init__(self, first_player, second_player, board):
        self.first_player = first_player
        self.second_player = second_player
        self.take_turns = True
        self.board = board
        self.printed = False

    def turn(self, x, y):
        """Given two integers representing the coordinates, let the current
        player make a move.
        Integer Integer -> None
        """
        x //= self.board.space
        y //= self.board.space
        if self.board.is_legal(x, y):
            if self.take_turns:
                self.first_player.move(x, y)
                self.take_turns = not self.take_turns
            else:
                self.second_player.move(x, y)
                self.take_turns = not self.take_turns

    def update(self):
        """Decides if the game ends. If yes, prints out the score message.
        None -> None"""
        if self.board.position_left() == 0 and not self.printed:
            if self.board.sum_of_black() == self.board.sum_of_white():
                print("Tie Game!!!")
                print("Balck: {0}".format(self.board.sum_of_black()))
                print("White: {0}".format(self.board.sum_of_white()))
            else:
                if self.board.sum_of_black() >= self.board.sum_of_white():
                    print("Black wins!!!")
                    print("Black tiles: {0}".format(self.board.sum_of_black()))
                else:
                    print("White tiles: {0}".format(self.board.sum_of_white()))
            self.printed = True
