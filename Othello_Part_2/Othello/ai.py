from player import Player


class AI(Player):
    def __init__(self, board, player):
        self.board = board
        self.color = 'white'
        self.name = 'AI'
        self.opponent = player
        # AI should avoid placing a tile at the positions
        # in the around_corner set
        self.corner = set()
        self.upper_left_corner = set()
        self.upper_right_corner = set()
        self.lower_left_corner = set()
        self.lower_right_corner = set()
        self.initializes()

    def initializes(self):
        """Initializes the around_corner set"""
        count = self.board.count
        # add positions around the upper_left corner
        self.upper_left_corner.add((1, 0))
        self.upper_left_corner.add((1, 1))
        self.upper_left_corner.add((0, 1))
        self.corner = self.corner.union(self.upper_left_corner)
        # add posistions around the upper_right corner
        self.upper_right_corner.add((count - 2, 0))
        self.upper_right_corner.add((count - 2, 1))
        self.upper_right_corner.add((count - 1, 1))
        self.corner = self.corner.union(self.upper_right_corner)
        # add positions around the lower_left corner
        self.lower_left_corner.add((0, count - 2))
        self.lower_left_corner.add((1, count - 2))
        self.lower_left_corner.add((1, count - 1))
        self.corner = self.corner.union(self.lower_left_corner)
        # add positions around the lower_right corner
        self.lower_right_corner.add((count - 1, count - 2))
        self.lower_right_corner.add((count - 2, count - 2))
        self.lower_right_corner.add((count - 2, count - 1))
        self.corner = self.corner.union(self.lower_right_corner)

    def greedy_strategy(self):
        """Add a tile at the position which leads to the most flips,
        also protects the corner by not adding a tile at its surroundings
        when there's other available positions"""
        flips = set()
        max_flip_position = (0, 0)
        corner_flips = set()
        conrer_flip_position = (0, 0)
        for pair in self.board.to_fill:
            temp = self.board.has_flip(pair[0], pair[1], self.color)
            if pair not in self.corner:
                if temp and len(temp) > len(flips):
                    flips = temp
                    max_flip_position = pair
            else:
                if temp and len(temp) > len(corner_flips):
                    corner_flips = temp
                    conrer_flip_position = pair
        if len(flips) > 0:
            return [max_flip_position, flips]
        else:
            return [conrer_flip_position, corner_flips]

    """
    def reduce_corner_effect(self):
        # reduces the effect of the corner by occupying
        # its surrounding position
        # checks if the upper_left corner is occupied
        count = self.board.count
        flips = set()
        position = (0, 0)
        if (0, 0) in self.board.on_board:
            for pair in self.upper_left_corner:
                temp = self.board.legal_move(0, 0, self.color)
                if temp and len(temp) > len(flips):
                    flips = temp
                    position = pair
        if (count - 1, 0) in self.board.on_board:
            for pair in self.upper_right_corner:
                temp = self.board.legal_move(count - 1, 0, self.color)
                if temp and len(temp) > len(flips):
                    flips = temp
                    position = pair
        if (0, count - 1) in self.board.on_board:
            for pair in self.lower_left_corner:
                temp = self.board.legal_move(0, count - 1, self.color)
                if temp and len(temp) > len(flips):
                    flips = temp
                    position = pair
        if (count - 1, count - 1) in self.board.on_board:
            for pair in self.lower_right_corner:
                temp = self.board.legal_move(count - 1, count - 1, self.color)
                if temp and len(temp) > len(flips):
                    flips = temp
                    position = pair
        if flips:
            return [position, flips]
    """

    def occupy_corner(self):
        """chechs if the corners are legal moves"""
        count = self.board.count
        max_flip_postion = (count//2, count//2)
        flips = set()
        upper_left = self.board.legal_move(0, 0, self.color)
        if upper_left and len(upper_left) > len(flips):
            max_flip_postion = (0, 0)
            flips = upper_left
        upper_right = self.board.legal_move(count - 1, 0, self.color)
        if upper_right and len(upper_right) > len(flips):
            max_flip_postion = (count - 1, 0)
            flips = upper_right
        lower_left = self.board.legal_move(0, count - 1, self.color)
        if lower_left and len(lower_left) > len(flips):
            max_flip_postion = (0, count - 1)
            flips = lower_left
        lower_right = self.board.legal_move(count - 1, count - 1, self.color)
        if lower_right and len(lower_right) > len(flips):
            max_flip_postion = (count - 1, count - 1)
            flips = lower_right
        if len(flips) > 0:
            return [max_flip_postion, flips]
        else:
            return False

    def prioritize(self):
        """If a corner can be occupied, occupy it; otherwise adpots the greedy
        strategy"""
        temp = self.occupy_corner()
        if temp:
            return temp
        else:
            return self.greedy_strategy()
