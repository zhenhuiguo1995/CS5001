from player import Player
from board import Board
from tiles import Tiles


def test_constructor():
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    assert player.name == 'Alfred'
    assert player.board is board
    assert player.color == 'black'


def test_has_legal_move():
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    assert player.has_legal_move() is True


def test_move():
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    i, j = player.board.count//2 + 1, player.board.count//2
    flips = set()
    flips.add((player.board.count//2, player.board.count//2))
    player.move(i, j, flips)
    assert player.board.tiles_list[i][j].color == 'black'
    assert player.board.tiles_list[i - 1][j].color == 'black'
