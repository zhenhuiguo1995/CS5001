from tile import Tile


def test_constructor():
    tile = Tile(150, 150, 100, 'white')
    assert tile.x == 150
    assert tile.y == 150
    assert tile.diameter == 100 * tile.COEFFICIENT
    assert tile.color == 'white'
