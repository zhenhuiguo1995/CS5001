from player import Player


class AI(Player):
    def __init__(self, board, player):
        self.board = board
        self.color = 'white'
        self.name = 'AI'
        self.opponent = player

    def greedy_strategy(self):
        """Add a tile at the position which leads to the most flips"""
        flips = set()
        max_flip_position = (0, 0)
        for pair in self.board.to_fill:
            temp = self.board.has_flip(pair[0], pair[1], self.color)
            if temp and len(temp) > len(flips):
                flips = temp
                max_flip_position = pair
        return [max_flip_position, flips]

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
        temp = self.occupy_corner()
        if temp:
            return temp
        return self.greedy_strategy()
