from player import Player


class AI(Player):
    def __init__(self, board, human_player):
        self.board = board
        self.color = 'white'
        self.name = 'AI'
        self.opponent = human_player

    def greedy_strategy(self):
        """Add a tile at the position which will lead to the most flips"""
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
        length = self.board.length
        max_flip_postion = (length//2, length//2)
        flips = set()
        upper_left = self.board.legal_move(0, 0, self.color)
        if upper_left and len(upper_left) > len(flips):
            max_flip_postion = (0, 0)
            flips = upper_left
        if upper_left is False:
            print("Upper left conrer can not be occupied")
        upper_right = self.board.legal_move(length - 1, 0, self.color)
        if upper_right and len(upper_right) > len(flips):
            max_flip_postion = (length - 1, 0)
            flips = upper_right
        if upper_right is False:
            print("Upper right conrer can not be occupied")
        lower_left = self.board.legal_move(0, length - 1, self.color)
        if lower_left and len(lower_left) > len(flips):
            max_flip_postion = (0, length - 1)
            flips = lower_left
        if lower_left is False:
            print("lower left conrer can not be occupied")
        lower_right = self.board.legal_move(length - 1, length - 1, self.color)
        if lower_right and len(lower_right) > len(flips):
            max_flip_postion = (length - 1, length - 1)
            flips = lower_right
        if lower_right is False:
            print("lower right corner cannot be occupied")
        if len(flips) > 0:
            return [max_flip_postion, flips]
        else:
            return False

    def block_path():
        "checks if there's move which can block the human player's next move"
        pass
        """ flips = set()
        block_point = None
        for pair in self.board.to_fill:
            temp = self.board.has_flip(pair[0], pair[1], self.color)
            new_board = self.board.copy()
            if temp and len(temp) > len(flips):
                flips = temp
                max_flip_position = pair
        return [max_flip_position, flips] """

    def prioritize(self):
        temp = self.occupy_corner()
        length = self.board.length
        print(temp)
        if temp:
            if (0, 0) in temp:
                print("(0, 0) can be reached")
            if (0, length - 1) in temp:
                print("(0, 7) can be reached")
            if (length - 1, 0) in temp:
                print("(7, 0) can be reached")
            if (length - 1, length - 1) in temp:
                print("(7, 7) can be reached")
            return temp
        else:
            print("No corner can be occupied")
            return self.greedy_strategy()
