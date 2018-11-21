class Tile():
    """Representing a single tile"""
    def __init__(self, x, y, radian, color):
        COEFFICIENT = 0.9
        self.x = x
        self.y = y
        self.radian = radian * COEFFICIENT
        self.color = color

    def display(self):
        """Display a tile on the board
        None -> None"""
        if self.color == "white":
            fill(1, 1, 1)
        if self.color == "black":
            fill(0, 0, 0)
        ellipse(self.x, self.y, self.radian, self.radian)
