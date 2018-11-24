from board import Board
from game_controller import GameController
from player import Player
from tiles import Tiles
from ai import AI

LENGTH = 800
SPACE = 100
COUNTDOWN = 1500
tiles = Tiles(LENGTH, SPACE)
board = Board(LENGTH, SPACE, tiles)
player = Player("Player", board, "black")
ai = AI(board, player)
game_controller = GameController(player, ai, board)
game_end = False


def setup():
    size(LENGTH, LENGTH)
    colorMode(RGB, 1)
    strokeWeight(2)


def draw():
    global announced, game_end
    if not game_end:
        if game_controller.take_turns:
            if not game_controller.player_announced:
                print('Player\'s turn')
                game_controller.player_announced = True
            if game_controller.player_has_move():
                if mousePressed and mouseX >= 0 and mouseX < LENGTH \
                    and mouseY >= 0 and mouseY < LENGTH:
                    game_controller.player_turn(mouseX, mouseY)
            else:
                game_controller.take_turns = not game_controller.take_turns
        else:
            if not game_controller.ai_announced:
                print('AI\'s turn')
                game_controller.ai_announced = True
            delay(COUNTDOWN)
            if game_controller.ai_has_move():
                game_controller.ai_turn()
            else:
                game_controller.take_turns = not game_controller.take_turns
        game_controller.display()
        game_end = not game_controller.game_can_proceed()
    else:
        game_controller.display()
        game_controller.announce()
