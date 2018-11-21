from player import Player
from ai import AI
import os


class GameController():
    def __init__(self, player, ai, board):
        self.player = player
        self.ai = ai
        self.take_turns = True
        self.board = board
        self.finished = False
        self.no_legal_move = False
        self.player_announced = False
        self.ai_announced = False

    def player_has_move(self):
        return self.player.has_legal_move()

    def ai_has_move(self):
        return self.ai.has_legal_move()

    def game_can_proceed(self):
        return self.player_has_move() or self.ai_has_move()

    def player_turn(self, x, y):
        """Player place a tile on board"""
        x //= self.board.space
        y //= self.board.space
        temp = self.board.legal_move(x, y, self.player.color)
        if temp:
            self.player.move(x, y, temp)
            self.take_turns = not self.take_turns
            self.player_announced = False

    def ai_turn(self):
        """AI place a tile on board."""
        temp = self.ai.prioritize()
        pair, flips = temp[0], temp[1]
        self.ai.move(pair[0], pair[1], flips)
        self.take_turns = not self.take_turns
        self.ai_announced = False

    def display(self):
        """Display the board and the tiles"""
        self.board.display()
        self.board.tile.display()
        if self.board.position_left() == 0 or self.no_legal_move:
            return True
        else:
            return False

    def announce(self):
        """Announce the score and record the name"""
        if self.finished:
            fill(1, 0, 0)
            textSize(30)
            x = self.board.length//2 - self.board.space
            y = self.board.length//2 - self.board.space//2
            if self.board.sum_of_black() == self.board.sum_of_white():
                text("Tie Game!!!", x, y)
            elif self.board.sum_of_black() >= self.board.sum_of_white():
                text("Player wins", x, y)
            else:
                text("AI wins!!!", x, y)
            text(
                "Player: {0}".format(self.board.sum_of_black()),
                x, y + self.board.space//2
                )
            text(
                "AI: {0}".format(self.board.sum_of_white()),
                x, y + self.board.space
                )
        if not self.finished:
            self.record()

    def record(self):
        """Record the player's name and write it to file"""
        answer = self.input('enter your name:')
        while not answer:
            answer = self.input('enter your name: ')
        self.save_to_file(answer, self.board.sum_of_black())
        self.finished = True

    def input(self, message=''):
        """Prompts the user a window to input the name"""
        from javax.swing import JOptionPane
        return JOptionPane.showInputDialog(frame, message)

    def save_to_file(self, name, score):
        """Save the player's name and score to a file"""
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
