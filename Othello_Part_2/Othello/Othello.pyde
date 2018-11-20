from board import Board
from game_controller import GameController
from player import Player
from tiles import Tiles
from ai import AI

LENGTH = 400
SPACE = 100
COUNTDOWN = 1000
tiles = Tiles(LENGTH, SPACE)
board = Board(LENGTH, SPACE, tiles)
first_player = Player("Human", board, "black")
second_player = AI(board, first_player)
game_controller = GameController(first_player, second_player, board)
announced = False
game_end = False


def setup():
    size(LENGTH, LENGTH)
    colorMode(RGB, 1)
    strokeWeight(2)


def draw():
    global announced, game_end
    if not game_end:
        if game_controller.take_turns:
            if not announced:
                print('Human player\'s turn')
                announced = True
            if mousePressed and mouseX >= 0 and mouseX < LENGTH \
                and mouseY >= 0 and mouseY < LENGTH:
                game_controller.human_turn(mouseX, mouseY)
                announced = False
        else:
            print('AI\'s turn')
            delay(COUNTDOWN)
            game_controller.ai_turn()
        game_end = game_controller.update()
    else:
        game_controller.display()
