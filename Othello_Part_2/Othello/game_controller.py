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
        if self.take_turns:
            if self.first_player.has_legal_move():
                temp = self.board.legal_move(x, y, self.first_player.color)
                if temp:
                    self.first_player.move(x, y, temp)
                    self.take_turns = not self.take_turns
            else:
                self.take_turns = not self.take_turns
        else:
            if self.second_player.has_legal_move():
                temp = self.board.legal_move(x, y, self.second_player.color)
                if temp:
                    self.second_player.move(x, y, temp)
                    self.take_turns = not self.take_turns
            else:
                self.take_turns = not self.take_turns

    def update(self):
        print(self.board.position_left())
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
            answer = input('enter your name:')
            if answer:
                print("Hi", answer)
            elif answer == '':
                print('empty string')
            else:
                print(answer)

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)