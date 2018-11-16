class Tile():
    """Representing a tile"""
    def __init__(self, x, y, diameter, color):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color

    def display(self):
        if self.color == "white":
            fill(1, 1, 1)
        if self.color == "black":
            fill(0, 0, 0)
        ellipse(self.x, self.y, self.diameter, self.diameter)
