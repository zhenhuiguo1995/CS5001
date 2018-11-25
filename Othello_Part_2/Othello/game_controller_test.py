from game_controller import GameController
from ai import AI
from player import Player
from board import Board
from tiles import Tiles


def test_constructor():
    """Test the constructor of the GameController class."""
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    ai = AI(board, player)
    game_controller = GameController(player, ai, board)
    assert game_controller.ai is ai
    assert game_controller.player is player
    assert game_controller.board is board
    assert game_controller.take_turns is True
    assert game_controller.finished is False
    assert game_controller.no_legal_move is False
    assert game_controller.player_announced is False
    assert game_controller.ai_announced is False


def test_player_has_move():
    """Test the player_has_move method."""
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    ai = AI(board, player)
    game_controller = GameController(player, ai, board)
    assert game_controller.player_has_move() is True
    for pair in board.on_board:
        board.tiles_list[pair[0]][pair[1]].color = 'black'
    assert game_controller.player_has_move() is False


def test_ai_has_move():
    """Test the ai_has_move method."""
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    ai = AI(board, player)
    game_controller = GameController(player, ai, board)
    assert game_controller.ai_has_move() is True
    for pair in board.on_board:
        board.tiles_list[pair[0]][pair[1]].color = 'white'
    assert game_controller.ai_has_move() is False


def test_game_can_proceed():
    """Test the game_can_proceed method."""
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    ai = AI(board, player)
    game_controller = GameController(player, ai, board)
    assert game_controller.game_can_proceed() is True
    for pair in board.on_board:
        board.tiles_list[pair[0]][pair[1]].color = 'white'
    assert game_controller.ai_has_move() is False


def test_player_turn():
    """Test the player_turn method."""
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    ai = AI(board, player)
    game_controller = GameController(player, ai, board)
    x, y = board.space * 0, board.space * 0
    game_controller.player_turn(x, y)
    assert game_controller.take_turns is True
    x, y = board.space * (board.count//2 + 1),  board.space * board.count//2
    game_controller.player_turn(x, y)
    assert game_controller.take_turns is False


def test_ai_turn():
    """Test the ai_turn method."""
    tiles = Tiles(800, 100)
    board = Board(800, 100, tiles)
    player = Player('Alfred', board, 'black')
    ai = AI(board, player)
    game_controller = GameController(player, ai, board)
    assert game_controller.take_turns is True
    x, y = board.space * (board.count//2 + 1),  board.space * board.count//2
    game_controller.player_turn(x, y)
    assert game_controller.take_turns is False
    game_controller.ai_turn()
    assert game_controller.take_turns is True
