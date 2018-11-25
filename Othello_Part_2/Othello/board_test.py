from board import Board
from tiles import Tiles
import random as rnd


def test_constructor():
    """Test the constructor."""
    tiles = Tiles(600, 100)
    board = Board(600, 100, tiles)
    assert board.space == 100
    assert board.length == 600
    assert board.tiles is tiles
    assert board.count == board.length//board.space
    assert len(board.on_board) == 4
    assert len(board.to_fill) == (
                                (board.length//board.space) ** 2 -
                                len(board.on_board)
                                )


def test_add_tile():
    """Test the add_tile method of the Board class."""
    tiles = Tiles(600, 100)
    board = Board(600, 100, tiles)
    i = rnd.randint(0, board.count - 1)
    j = rnd.randint(0, board.count - 1)
    board.add_tile(i, j, 'white')
    assert board.tiles_list[i][j].x == i * board.space + board.space//2
    assert board.tiles_list[i][j].y == j * board.space + board.space//2
    assert board.tiles_list[i][j].color == 'white'
    assert (i, j) in board.on_board
    assert (i, j) not in board.to_fill


def test_position_left():
    """Test the position_left method of the Board class."""
    tiles = Tiles(600, 100)
    board = Board(600, 100, tiles)
    assert board.position_left() == (board.length//board.space) ** 2 - 4
    board.add_tile(0, 0, 'black')
    assert board.position_left() == (board.length//board.space) ** 2 - 5


def test_sum_of_black():
    """Test the sum_of_black method of the Board class."""
    tiles = Tiles(600, 100)
    board = Board(600, 100, tiles)
    assert board.sum_of_black() == 2
    board.add_tile(0, 0, 'black')
    assert board.sum_of_black() == 3


def test_sum_of_white():
    """Test the sum_of_white method of the Board class."""
    tiles = Tiles(600, 100)
    board = Board(600, 100, tiles)
    assert board.sum_of_white() == 2
    board.add_tile(0, 0, 'white')
    assert board.sum_of_white() == 3


def test_flip_horizontal():
    """Test the flip_horizontal method of the Board class."""
    tiles = Tiles(600, 100)
    board = Board(600, 100, tiles)
    assert len(board.flip_horizontal(0, 0, 'white')) == 0
    assert len(board.flip_horizontal(0, 0, 'black')) == 0
    i, j = board.count//2 - 2, board.count//2
    assert len(board.flip_horizontal(i, j, 'black')) == 0
    assert len(board.flip_horizontal(i, j, 'white')) == 1
    i, j = board.count//2 - 2, board.count//2 - 1
    assert len(board.flip_horizontal(i, j, 'black')) == 1
    assert len(board.flip_horizontal(i, j, 'white')) == 0


def test_flip_vertical():
    """Test the flip_vertical method of the Board class."""
    tiles = Tiles(600, 100)
    board = Board(600, 100, tiles)
    assert len(board.flip_vertical(0, 0, 'white')) == 0
    assert len(board.flip_vertical(0, 0, 'black')) == 0
    i, j = board.count//2 - 1, board.count//2 - 2
    assert len(board.flip_vertical(i, j, 'white')) == 0
    assert len(board.flip_vertical(i, j, 'black')) == 1
    i, j = board.count//2, board.count//2 - 2
    assert len(board.flip_vertical(i, j, 'white')) == 1
    assert len(board.flip_vertical(i, j, 'black')) == 0


def test_flip_diagonal():
    """Test the flip_diagonal method of the Board class."""
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    assert len(board.flip_diagonal(0, 0, 'white')) == 0
    assert len(board.flip_diagonal(0, 0, 'black')) == 0
    i, j = board.count//2 + 1, board.count//2 - 2
    board.add_tile(i, j, 'white')
    i, j = board.count//2 + 2, board.count//2 - 3
    assert len(board.flip_diagonal(i, j, 'white')) == 0
    assert len(board.flip_diagonal(i, j, 'black')) == 1
    i, j = board.count//2 - 2, board.count//2 + 1
    board.add_tile(i, j, 'white')
    i, j = board.count//2 - 3, board.count//2 + 2
    assert len(board.flip_diagonal(i, j, 'white')) == 0
    assert len(board.flip_diagonal(i, j, 'black')) == 1
    i, j = board.count//2 - 2, board.count//2 - 2
    board.add_tile(i, j, 'black')
    i, j = board.count//2 - 3, board.count//2 - 3
    assert len(board.flip_diagonal(i, j, 'white')) == 1
    assert len(board.flip_diagonal(i, j, 'black')) == 0
    i, j = board.count//2 + 1, board.count//2 + 1
    board.add_tile(i, j, 'black')
    i, j = board.count//2 + 2, board.count//2 + 2
    assert len(board.flip_diagonal(i, j, 'white')) == 1
    assert len(board.flip_diagonal(i, j, 'black')) == 0


def test_has_legal_move():
    """Test the has_legal_move method of the Board class."""
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    assert board.has_legal_move('black') is True
    assert board.has_legal_move('white') is True
    for pair in board.on_board:
        board.tiles_list[pair[0]][pair[1]].color = 'black'
    assert board.has_legal_move('black') is False
    assert board.has_legal_move('white') is False


def test_legal_move():
    """Test the legal_move method of the Board class."""
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    for pair in board.on_board:
        assert board.legal_move(pair[0], pair[1], 'white') is False
        assert board.legal_move(pair[0], pair[1], 'blacj') is False
