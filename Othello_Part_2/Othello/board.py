from tile import Tile

class Board():
    """Draws the board and handles interaction between
    player and computer"""
    def __init__(self, length, space, tile):
        self.length = length
        self.space = space
        self.tiles = tile.tiles
        self.on_board = set()
        # initializes the middle of the board
        middle_x = len(self.tiles)//2
        middle_y = len(self.tiles[0])//2
        self.add_tile((middle_x - 1, middle_y - 1), "white")
        self.add_tile((middle_x, middle_y - 1), "black")
        self.add_tile((middle_x - 1, middle_y), "black")
        self.add_tile((middle_x, middle_y), "white")


    def is_legal(self, x, y):
        """Decides if a move is legal"""
        # Current implementation: no tile objects already exists here
        if (x, y) not in self.on_board:
            return True
        else:
            return False

    def add_tile(self, pair, color):
        x_coordinate = pair[0] * self.space + self.space//2
        y_coordinate = pair[1] * self.space + self.space//2
        self.tiles[pair[0]][pair[1]] = Tile(x_coordinate, y_coordinate, self.space, color)
        self.on_board.add(pair)

    def display(self):
        """Display the board"""
        background(0, 1, 0)
        for i in range(self.length//self.space):
            line(0, i * self.space, self.length, self.space * i)
        for i in range(self.length//self.space):
            line(i * self.space, 0, i * self.space, self.length)
        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[0])):
                if self.tiles[i][j] is not None:
                    self.tiles[i][j].display()

    def position_left(self):
        num = 0
        for rows in self.tiles:
            for tile in rows:
                if tile is None:
                    num += 1
        return num

    def sum_of_white(self):
        count = 0 
        for rows in self.tiles:
            for tile in rows:
                if tile.color == "white":
                    count += 1
        return count
    
    def sum_of_black(self):
        count = 0 
        for rows in self.tiles:
            for tile in rows:
                if tile.color == "black":
                    count += 1
        return count

    def has_move(self, x, y):
        """determines if there's more legal move to make
        if there's None, return False
        If there's some: return True"""
        pass
    
    def flip_horizontal(self, x, y, color):
        """determines if there's some tiles to flip horizontally
        if yes, return the set of position of the tiles that will be flipped
        if not, return False"""
        pass
    
    def flip_vertically(self, x, y, color):
        """determines if there's some tiles to flip horizontally
        if yes, return the set of position of the tiles that will be flipped
        if not, return False"""
        pass        
    
    def flip_diagonally(self, x, y, color):
        """determines if there's some tiles to flip along the diagonal
        if yes, return the set of position of the tiles that will be flipped
        if not, return False"""
        pass