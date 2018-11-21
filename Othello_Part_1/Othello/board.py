from tile import Tile


class Board():
    """Draws the board and handles interaction between
    player and computer"""
    def __init__(self, length, space, tile):
        self.length = length
        self.space = space
        self.tile = tile
        self.tiles = tile.tiles
        self.on_board = set()
        self.to_fill = set()
        self.initialize()

    def initialize(self):
        """Initializes to_fill set and the middle four chess of the boards.
        None -> None"""
        for i in range(self.length//self.space):
            for j in range(self.length//self.space):
                self.to_fill.add((i, j))
        middle_x = len(self.tiles)//2
        middle_y = len(self.tiles[0])//2
        self.add_tile((middle_x - 1, middle_y - 1), "white")
        self.add_tile((middle_x, middle_y - 1), "black")
        self.add_tile((middle_x - 1, middle_y), "black")
        self.add_tile((middle_x, middle_y), "white")

    def is_legal(self, x, y):
        """Given two integers representing the coordinates, returns a boolean
        value which indicates the current move is legal or not.
        Integer Integer -> Boolean"""
        # Current implementation: no tile objects already exists here
        if (x, y) not in self.on_board:
            return True
        else:
            return False

    def add_tile(self, pair, color):
        """Given a tuple and a string, add a tile on the position specified
        by the tuple on the board.
        Tuple String -> None"""
        x_coordinate = pair[0] * self.space + self.space//2
        y_coordinate = pair[1] * self.space + self.space//2
        self.tiles[pair[0]][pair[1]] = Tile(
            x_coordinate, y_coordinate, self.space, color
            )
        self.on_board.add(pair)
        self.to_fill.remove(pair)

    def display(self):
        """Display the board and the tiles.
        None -> None"""
        background(0, 0.5, 0)
        for i in range(self.length//self.space):
            line(0, i * self.space, self.length, self.space * i)
        for i in range(self.length//self.space):
            line(i * self.space, 0, i * self.space, self.length)
        self.tile.display()

    def position_left(self):
        """Returns the number of positions left on the board.
        None -> Integer"""
        return len(self.to_fill)

    def sum_of_white(self):
        """Returns the number of white tiles on the board.
        None -> Integer"""
        count = 0
        for rows in self.tiles:
            for tile in rows:
                if tile is not None and tile.color == "white":
                    count += 1
        return count

    def sum_of_black(self):
        """Returns the number of black tiles on the board.
        None -> Integer"""
        count = 0
        for rows in self.tiles:
            for tile in rows:
                if tile is not None and tile.color == "black":
                    count += 1
        return count
