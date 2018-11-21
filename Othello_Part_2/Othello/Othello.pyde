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
player = Player("Player", board, "black")
ai = AI(board, player)
game_controller = GameController(player, ai, board)
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
                print('Player\'s turn')
                announced = True
            if mousePressed and mouseX >= 0 and mouseX < LENGTH \
                and mouseY >= 0 and mouseY < LENGTH:
                game_controller.player_turn(mouseX, mouseY)
                announced = False
        else:
            print('AI\'s turn')
            delay(COUNTDOWN)
            game_controller.ai_turn()
        game_controller.display()
        game_end = not game_controller.game_can_proceed()
    else:
        game_controller.display()
        game_controller.announce()
