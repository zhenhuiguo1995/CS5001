class Tile():
    """Represent a tile."""
    def __init__(self, x, y, diameter, color):
        self.COEFFICIENT = 0.9
        self.x = x
        self.y = y
        self.diameter = diameter * self.COEFFICIENT
        self.color = color

    def display(self):
        """Display the tile on the screen."""
        if self.color == "white":
            fill(1, 1, 1)
        if self.color == "black":
            fill(0, 0, 0)
        ellipse(self.x, self.y, self.diameter, self.diameter)
