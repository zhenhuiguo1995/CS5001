from board import Board
from tiles import Tiles


def test_constructor():
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    assert board.space == 100
    assert board.length == 800
    assert board.tile is tiles
    assert board.count == board.length//board.space
    assert len(board.on_board) == 4
    assert len(board.to_fill) == (
                                (board.length//board.space) ** 2 -
                                len(board.on_board)
                                )
