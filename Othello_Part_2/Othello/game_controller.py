from player import Player
from ai import AI
import os


class GameController():
    def __init__(self, human, ai, board):
        self.first_player = human
        self.second_player = ai
        self.take_turns = True
        self.board = board
        self.finished = False
        self.no_legal_move = False

    def human_turn(self, x, y):
        x //= self.board.space
        y //= self.board.space
        if self.first_player.has_legal_move():
            temp = self.board.legal_move(x, y, self.first_player.color)
            if temp:
                self.first_player.move(x, y, temp)
                self.take_turns = not self.take_turns
        elif self.second_player.has_legal_move():
            self.take_turns = not self.take_turns
        else:
            self.no_legal_move = True

    def ai_turn(self):
        if self.second_player.has_legal_move():
            temp = self.second_player.prioritize()
            pair, flips = temp[0], temp[1]
            self.second_player.move(pair[0], pair[1], flips)
            self.take_turns = not self.take_turns
        elif self.first_player.has_legal_move():
            self.take_turns = not self.take_turns
        else:
            self.no_legal_move = True

    def update(self):
        self.board.display()
        self.board.tile.display()
        if self.board.position_left() == 0 or self.no_legal_move:
            return True
        else:
            return False

    def display(self):
        if self.finished:
            fill(1, 0, 0)
            textSize(30)
            x = self.board.length//2 - self.board.space//2
            y = self.board.length//2
            if self.board.sum_of_black() == self.board.sum_of_white():
                text("Tie Game!!!", x, y)
            elif self.board.sum_of_black() >= self.board.sum_of_white():
                text("Human wins", x, y)
            else:
                text("AI wins!!!", x, y)
            text(
                "Human: {0}".format(self.board.sum_of_black()),
                x, y + self.board.space//2
                )
            text(
                "AI: {0}".format(self.board.sum_of_white()),
                x, y + self.board.space
                )
        if not self.finished:
            self.record()

    def record(self):
        answer = self.input('enter your name:')
        while not answer:
            answer = self.input('enter your name: ')
        self.save_to_file(answer, self.board.sum_of_black())
        self.finished = True

    def input(self, message=''):
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def save_to_file(self, name, score):
        if 'scores.txt' not in os.listdir('.'):
            file = open('scores.txt', 'w+')
            line = name + ' ' + str(score) + '\n'
            file.write(line)
            file.close()
        else:
            file = open('scores.txt')
            temp = []
            for line in file:
                temp.append(line)
            file.close()
            new_line = name + ' ' + str(score) + '\n'
            first_line = temp[0].rstrip().split()
            if int(first_line[1]) >= score:
                temp.append(new_line)
            else:
                temp.insert(0, new_line)
            file = open('scores.txt', 'w+')
            for line in temp:
                file.write(line)
            file.close()
