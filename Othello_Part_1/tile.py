class Tile():
    """Representing a tile"""
    def __init__(self, x, y, radian, color):
        self.x = x
        self.y = y
        self.radian = radian
        self.color = color

    def display(self):
        if self.color == "white":
            fill(1, 1, 1)
        if self.color == "black":
            fill(0, 0, 0)
        ellipse(self.x, self.y, self.radian, self.radian)
            
