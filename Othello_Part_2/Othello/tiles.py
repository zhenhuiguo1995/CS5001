class Tiles:
    """A collection of tiles."""
    def __init__(self, LENGTH, SPACE):
        self.LENGTH = LENGTH
        self.SPACE = SPACE
        self.tiles = [
            [None for _ in range(self.LENGTH//self.SPACE)]
            for _ in range(self.LENGTH//self.SPACE)
            ]

    def display(self):
        for rows in self.tiles:
            for tile in rows:
                if tile is not None:
                    tile.display()