from player import Player


class GameController():
    def __init__(self, first_player, second_player, board):
        self.first_player = first_player
        self.second_player = second_player
        self.take_turns = True
        self.board = board

    def turn(self, x, y): 
        x //= self.board.space
        y //= self.board.space
        if self.board.is_legal(x, y):
            if self.take_turns:
                self.first_player.move(x, y)
                self.take_turns = False
            else:
                self.second_player.move(x, y)
                self.take_turns = True    
        else:
            print("Not an legal move, try again!")

    def update(self):
        if self.board.position_left() == 0:
            fill(1, 0, 0)
            textSize(30)
            x = self.board.length//2 - self.board.space//2
            y = self.board.length//2
            if self.board.sum_of_black() == self.board.sum_of_white():
                text("Tie Game!!!", x, y)        
            elif self.board.sum_of_black() >= self.board.sum_of_white():
                text("Black wins", x, y)
            else:
                text("White wins!!!", x, y)
            text("Black: {0}".format(self.board.sum_of_black()),
                x, y + self.board.space//2)
            text("White: {0}".format(self.board.sum_of_white()),
                x, y + self.board.space)