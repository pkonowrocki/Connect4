class Connect:
    def __init__(self, connect=4, width=7, height=6):
        self.height = height
        self.width = width
        self.connect = connect
        self.players = ["x", "o"]
        self.reset()

    def reset(self):
        self.board = [[" " for _ in range(self.width)] for _ in range(self.height)]

    def __str__(self):
        temp = ""
        for row in range(self.height):
            temp += "|"
            for c in range(self.width):
                temp += "{0}|".format(self.board[row][c])
            temp += "\n"
        temp += "|"
        for c in range(self.width):
            temp += "{0}|".format(c)
        temp += "\n"
        return temp[:-1]
    
    def __eq__(self, other):
        if(isinstance(other, type(self))):
            return self.board==other.board
        else:
            return False

    def __hash__(self):
        return hash("".join(sum(self.board,[])))
    
    def copy(self):
        new = self.__class__(connect=self.connect, width=self.width, height=self.height)
        new.board = [x[:] for x in self.board]
        return new

    def getMoves(self):
        return [index for index, value in enumerate(self.board[0]) if value==" "]

    def _isMatch(self, match):
        s_match = set(match)
        if(len(s_match) == 1 and " " not in s_match):
            return match[0]
    
    def move(self, player, col):
        player = player.lower()
        assert col in self.getMoves(), "Illegal move"
        assert player in self.players, "Illegal player"
        moveRow = 0
        for row in reversed(range(self.height)):
            if(self.board[row][col]==" "):
                moveRow = row
                break
        self.board[moveRow][col] = player

    def winner(self):
        for row in range(self.height):
            for col in range(self.width - self.connect + 1):
                match = [self.board[row][col+off] for off in range(self.connect)]
                if self._isMatch(match) is not None:
                    return match[0]

        for row in range(self.height - self.connect + 1):
            for col in range(self.width):
                match = [self.board[row+off][col] for off in range(self.connect)]
                if self._isMatch(match) is not None:
                    return match[0]

        for row in range(self.height - self.connect // 2 - 1):
            for col in range(self.width - self.connect // 2 - 1):
                match = [self.board[row + off][col + off] for off in range(self.connect)]
                if self._isMatch(match) is not None:
                    return match[0]
                match = [self.board[off][self.width - off - 1] for off in range(self.connect)]
                if self._isMatch(match) is not None:
                    return match[0]

    def scoreGame(self, player):
        if(self.winner() == player):
            return 1
        elif(self.winner() in self.players):
            return -1
        return 0

    def gameOver(self):
        return len(self.getMoves()) == 0 or self.winner() is not None