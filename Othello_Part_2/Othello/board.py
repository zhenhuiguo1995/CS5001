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
        # the number of squares each line
        self.count = self.length//self.space
        self.initialize()

    def initialize(self):
        # initialize the to_fill set
        # put four tiles on the middle of the board
        for i in range(self.length//self.space):
            for j in range(self.length//self.space):
                self.to_fill.add((i, j))
        middle_x = self.count//2
        middle_y = self.count//2
        self.add_tile(middle_x - 1, middle_y - 1, "white")
        self.add_tile(middle_x, middle_y - 1, "black")
        self.add_tile(middle_x - 1, middle_y, "black")
        self.add_tile(middle_x, middle_y, "white")

    def add_tile(self, x, y, color):
        """Add a tile on the board"""
        x_coordinate = x * self.space + self.space//2
        y_coordinate = y * self.space + self.space//2
        self.tiles[x][y] = Tile(x_coordinate, y_coordinate, self.space, color)
        self.on_board.add((x, y))
        self.to_fill.remove((x, y))

    def legal_move(self, x, y, color):
        """If there's flips for this move, return the tiles to be fliped as a
        set, else return False"""
        if (x, y) not in self.on_board:
            flip = self.has_flip(x, y, color)
            if flip:
                return flip
            else:
                return False
        else:
            return False

    def has_legal_move(self, color):
        """"If there's a legal move at any position on the board, return
        True, else return False"""
        for pair in self.to_fill:
            if self.legal_move(pair[0], pair[1], color):
                return True
        return False

    def position_left(self):
        """Returns the positions left on the board"""
        return len(self.to_fill)

    def has_flip(self, x, y, color):
        """return the set of tiles that will be flipped
        by placing a tile in the given position"""
        hor_flip = self.flip_horizontal(x, y, color)
        ver_flip = self.flip_vertical(x, y, color)
        diag_flip = self.flip_diagonal(x, y, color)
        flips = hor_flip.union(ver_flip).union(diag_flip)
        return flips

    def flip(self, flips, color):
        for pair in flips:
            self.tiles[pair[0]][pair[1]].color = color

    def display(self):
        """Display the board"""
        background(0, 0.5, 0)
        for i in range(self.count):
            line(0, i * self.space, self.length, self.space * i)
        for i in range(self.count):
            line(i * self.space, 0, i * self.space, self.length)

    def sum_of_white(self):
        count = 0
        for rows in self.tiles:
            for tile in rows:
                if tile is not None and tile.color == "white":
                    count += 1
        return count

    def sum_of_black(self):
        count = 0
        for rows in self.tiles:
            for tile in rows:
                if tile is not None and tile.color == "black":
                    count += 1
        return count

    def flip_horizontal(self, x, y, color):
        """determines if there's some tiles to flip horizontally
        if yes, return the set of position of the tiles that will be flipped
        if not, return False"""
        flip = set()
        # search left
        if x >= 2 and (x - 1, y) in self.on_board \
                and self.tiles[x - 1][y].color != color:
            temp = x - 1
            pending = set()
            while temp >= 0 and (temp, y) in self.on_board \
                    and self.tiles[temp][y].color != color:
                pending.add((temp, y))
                temp -= 1
            if temp >= 0 and (temp, y) in self.on_board \
                    and self.tiles[temp][y].color == color:
                flip = flip.union(pending)
        # search right
        if x <= self.count - 2 and (x + 1, y) in self.on_board \
                and self.tiles[x + 1][y].color != color:
            temp = x + 1
            pending = set()
            while temp < self.count and (temp, y) in self.on_board \
                    and self.tiles[temp][y].color != color:
                pending.add((temp, y))
                temp += 1
            if temp < self.count and (temp, y) in self.on_board \
                    and self.tiles[temp][y].color == color:
                flip = flip.union(pending)
        return flip

    def flip_vertical(self, x, y, color):
        """determines if there's some tiles to flip horizontally
        if yes, return the set of position of the tiles that will be flipped
        if not, return False"""
        flip = set()
        # search upwards
        if y >= 2 and (x, y - 1) in self.on_board \
                and self.tiles[x][y - 1].color != color:
            temp = y - 1
            pending = set()
            while temp >= 0 and (x, temp) in self.on_board \
                    and self.tiles[x][temp].color != color:
                pending.add((x, temp))
                temp -= 1
            if temp >= 0 and (x, temp) in self.on_board \
                    and self.tiles[x][temp].color == color:
                flip = flip.union(pending)
        # search downwards
        if y <= self.count - 2 and (x, y + 1) in self.on_board \
                and self.tiles[x][y + 1].color != color:
            temp = y + 1
            pending = set()
            while temp < self.count and (x, temp) in self.on_board \
                    and self.tiles[x][temp].color != color:
                pending.add((x, temp))
                temp += 1
            if temp < self.count and (x, temp) in self.on_board \
                    and self.tiles[x][temp].color == color:
                flip = flip.union(pending)
        return flip

    def flip_diagonal(self, x, y, color):
        """determines if there's some tiles to flip along the diagonal
        if yes, return the set of position of the tiles that will be flipped
        if not, return False"""
        flip = set()
        # search upper-left
        if x >= 2 and y >= 2 and (x - 1, y - 1) in self.on_board \
                and self.tiles[x - 1][y - 1].color != color:
            temp_x = x - 1
            temp_y = y - 1
            pending = set()
            while temp_x >= 0 and temp_y >= 0 \
                    and (temp_x, temp_y) in self.on_board \
                    and self.tiles[temp_x][temp_y].color != color:
                pending.add((temp_x, temp_y))
                temp_x -= 1
                temp_y -= 1
            if temp_x >= 0 and temp_y >= 0 \
                    and (temp_x, temp_y) in self.on_board \
                    and self.tiles[temp_x][temp_y].color == color:
                flip = flip.union(pending)
                # print("upper_left")
        # search lower-right
        if x <= self.count - 2 and y <= self.count - 2 \
                and (x + 1, y + 1) in self.on_board \
                and self.tiles[x + 1][y + 1].color != color:
            temp_x = x + 1
            temp_y = y + 1
            pending = set()
            while temp_x < self.count and temp_y < self.count \
                    and (temp_x, temp_y) in self.on_board \
                    and self.tiles[temp_x][temp_y].color != color:
                pending.add((temp_x, temp_y))
                temp_x += 1
                temp_y += 1
            if temp_x < self.count and temp_y < self.count \
                    and (temp_x, temp_y) in self.on_board \
                    and self.tiles[temp_x][temp_y].color == color:
                flip = flip.union(pending)
                # print("lower right")
        # search upper-right
        if x <= self.count - 2 and y >= 2 \
                and (x + 1, y - 1) in self.on_board \
                and self.tiles[x + 1][y - 1].color != color:
            temp_x = x + 1
            temp_y = y - 1
            pending = set()
            while temp_x < self.count and temp_y >= 0 \
                    and (temp_x, temp_y) in self.on_board \
                    and self.tiles[temp_x][temp_y].color != color:
                pending.add((temp_x, temp_y))
                temp_x += 1
                temp_y -= 1
            if temp_x < self.count and temp_y >= 0 \
                    and (temp_x, temp_y) in self.on_board \
                    and self.tiles[temp_x][temp_y].color == color:
                flip = flip.union(pending)
                # print("upper right")
        # search lower-left
        if x >= 2 and y <= self.count - 2 \
                and (x - 1, y + 1) in self.on_board \
                and self.tiles[x - 1][y + 1].color != color:
            temp_x = x - 1
            temp_y = y + 1
            pending = set()
            while temp_x >= 0 and temp_y < self.count \
                    and (temp_x, temp_y) in self.on_board \
                    and self.tiles[temp_x][temp_y].color != color:
                pending.add((temp_x, temp_y))
                temp_x -= 1
                temp_y += 1
            if temp_x >= 0 and temp_y < self.count \
                    and (temp_x, temp_y) in self.on_board \
                    and self.tiles[temp_x][temp_y].color == color:
                flip = flip.union(pending)
                # print("lower left")
        return flip
