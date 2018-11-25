from player import Player
from ai import AI
from board import Board
from tiles import Tiles


def test_constructor():
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    ai = AI(board, player)
    assert ai.board is board
    assert ai.color == 'white'
    assert ai.name == 'AI'
    assert ai.opponent is player
    assert len(ai.corner) == 12
    assert len(ai.upper_left_corner) == 3
    assert len(ai.upper_right_corner) == 3
    assert len(ai.lower_left_corner) == 3
    assert len(ai.lower_right_corner) == 3


def test_greedy_strategy():
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    ai = AI(board, player)
    for i in range(board.count//2 + 1, board.count - 1):
        board.add_tile(i, board.count//2 - 1, 'black')
    assert ai.greedy_strategy()[0] == (board.count - 1, board.count//2 - 1)
    assert len(ai.greedy_strategy()[1]) == board.count//2 - 1
    board.add_tile(board.count//2 - 1, 0,  'white')
    for i in range(1, board.count - 1):
        if board.tiles_list[board.count//2 - 1][i] is None:
            board.add_tile(board.count//2 - 1, i, 'black')
        else:
            board.tiles_list[board.count//2 - 1][i].color = 'black'
    assert ai.greedy_strategy()[0] == (board.count//2 - 1, board.count - 1)
    assert len(ai.greedy_strategy()[1]) == board.count - 2


def test_occupy_corner():
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    ai = AI(board, player)
    assert ai.occupy_corner() is False
    for i in range(1, board.count//2 - 1):
        board.add_tile(i, i, 'black')
    assert ai.occupy_corner()[0] == (0, 0)
    assert len(ai.occupy_corner()[1]) == board.count//2 - 2


def test_prioritize():
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    ai = AI(board, player)
    board.add_tile(board.count//2 - 1, 0,  'white')
    for i in range(1, board.count - 1):
        if board.tiles_list[board.count//2 - 1][i] is None:
            board.add_tile(board.count//2 - 1, i, 'black')
        else:
            board.tiles_list[board.count//2 - 1][i].color = 'black'
    assert ai.prioritize()[0] == (board.count//2 - 1, board.count - 1)
    assert len(ai.prioritize()[1]) == board.count - 2
    for i in range(board.count//2 + 1, board.count - 1):
        board.add_tile(i, i, 'black')
    assert ai.occupy_corner()[0] == (board.count - 1, board.count - 1)
    assert len(ai.occupy_corner()[1]) == board.count//2 - 2
