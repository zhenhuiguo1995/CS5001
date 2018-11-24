from tiles import Tiles


def test_constructor():
    tiles = Tiles(800, 100)
    assert tiles.SPACE == 100
    assert tiles.LENGTH == 800
    for i in range(tiles.LENGTH//tiles.SPACE):
        for j in range(tiles.LENGTH//tiles.SPACE):
            assert tiles.tiles[i][j] is None
