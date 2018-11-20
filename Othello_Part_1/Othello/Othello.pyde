from board import Board
from game_controller import GameController
from player import Player
from tiles import Tiles


LENGTH = 400
SPACE = 100
tiles = Tiles(LENGTH, SPACE)
board = Board(LENGTH, SPACE, tiles)
first_player = Player("Human", board, "black")
second_player = Player("Computer", board, "white")
game_controller = GameController(first_player, second_player, board)


def setup():
    size(LENGTH, LENGTH)
    colorMode(RGB, 1)
    strokeWeight(2)


def draw():
    # tiles.display()
    board.display()
    if mousePressed:
        if mouseX > 0 and mouseX < LENGTH and mouseY > 0 and mouseY < LENGTH:
                game_controller.turn(mouseX, mouseY)
    game_controller.update()
