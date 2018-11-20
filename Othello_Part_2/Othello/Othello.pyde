from board import Board
from game_controller import GameController
from player import Player
from tiles import Tiles
from ai import AI

LENGTH = 800
SPACE = 100
tiles = Tiles(LENGTH, SPACE)
board = Board(LENGTH, SPACE, tiles)
first_player = Player("Human", board, "black")
second_player = AI(board, first_player)
game_controller = GameController(first_player, second_player, board)


def setup():
    size(LENGTH, LENGTH)
    colorMode(RGB, 1)
    strokeWeight(2)


def draw():
    if game_controller.take_turns:
        if mousePressed and mouseX < LENGTH and mouseY < LENGTH:
            game_controller.human_turn(mouseX, mouseY)
    else:
        delay(1000)
        game_controller.ai_turn()
    game_controller.update()
