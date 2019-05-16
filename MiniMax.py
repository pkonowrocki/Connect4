class MiniMax:
    def __init__(self, timePenalty = -0.01, subOptimalWeight = 0.1, limit = 5):
        self.timePenalty = timePenalty
        self.memo = {}
        self.subOptimalWeight = subOptimalWeight
        self.limit = limit

    def play(self, game, player):
        return self._miniMax(game, player)[0]

    def _miniMax(self, game, player, numMoves = 0):
        if(player not in self.memo):
            self.memo[player] = {}
        
        playerMemo = self.memo[player]

        if(game not in playerMemo):
            if(game.gameOver()):
                bestMove = None
                bestScore = game.scoreGame(player)
            elif(numMoves > self.limit):
                bestMove = game.getMoves()[0]
                bestScore = 0
            else:
                altPlayer = [altPlayer for altPlayer in game.players if altPlayer != player][0]
                moves = game.getMoves()
                middle = int(len(moves)/2) + (1 if len(moves)%2 != 0 else 0)
                moves = (moves[0:middle][::-1] + moves[middle:len(moves)])
                bestScore = float("-inf")
                subOptimalSum = 0
                for move in  moves:
                    clone = game.copy()
                    clone.move(player, move)
                    _, score = self._miniMax(clone, player = altPlayer, numMoves=numMoves+1)
                    score *= -1
                    score += self.timePenalty * numMoves
                    subOptimalSum += score

                    if(score > bestScore):
                        bestMove = move
                        bestScore = score

                subOptimalSum -= bestScore
                subOptimal = subOptimalSum / len(moves)
                bestScore = ((1 - self.subOptimalWeight) * bestScore) + (self.subOptimalWeight * subOptimal)
            self.memo[player][game] = (bestMove, bestScore)
        return self.memo[player][game]