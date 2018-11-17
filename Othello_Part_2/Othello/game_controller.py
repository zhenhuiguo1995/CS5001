from player import Player


class GameController():
    def __init__(self, first_player, second_player, board):
        self.first_player = first_player
        self.second_player = second_player
        self.take_turns = True
        self.board = board
        self.finished = False
        self.no_legal_move = False

    def turn(self, x, y):
        x //= self.board.space
        y //= self.board.space
        if self.take_turns:
            if self.first_player.has_legal_move():
                temp = self.board.legal_move(x, y, self.first_player.color)
                if temp:
                    self.first_player.move(x, y, temp)
                    self.take_turns = not self.take_turns
            elif self.second_player.has_legal_move():
                self.take_turns = not self.take_turns
            else:
                self.no_legal_move = True
        else:
            if self.second_player.has_legal_move():
                temp = self.board.legal_move(x, y, self.second_player.color)
                if temp:
                    self.second_player.move(x, y, temp)
                    self.take_turns = not self.take_turns
            elif self.first_player.has_legal_move():
                self.take_turns = not self.take_turns
            else:
                self.no_legal_move = True

    def update(self):
        if self.board.position_left() == 0 or self.no_legal_move:
            # self.board.display()
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
            text("Black: {0}".format(self.board.sum_of_black()), x, y + self.board.space//2)
            text("White: {0}".format(self.board.sum_of_white()), x, y + self.board.space)
            if not self.finished:
                answer = self.input('enter your name:')
                while not answer:
                    answer = self.input('enter your name: ')
                self.save_file(answer, self.board.sum_of_black())
                self.finished = True

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def save_file(self, name, score):
        file = open('scores.txt')
        temp = []
        for line in file:
            line = line.split()
            temp.append((line[0], int(line[1])))
        temp.append((name, int(score)))
        file.close()
        temp = sorted(temp, key=lambda x: x[1], reverse=True)
        file = open('scores.txt', 'w+')
        for pair in temp:
            line = pair[0] + ' ' + str(pair[1]) + '\n'
            file.write(line)
        file.close()
