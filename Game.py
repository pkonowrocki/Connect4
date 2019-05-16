import Connect4 as c
import MiniMax as m

def play(game, bot):
    human = None
    while(human is None):
        human = input("Select player {}: ".format(game.players)).lower()
        if(human not in game.players):
            print("Invalid player.")
            human = None

    comp = [altPlayer for altPlayer in game.players if altPlayer != human][0]
    turn = game.players[0]

    while(not game.gameOver()):
        if(comp == turn):
            move = bot.play(game, comp)
        else:
            print(game)
            move = None
            while(move is None):
                move = input("Input move: ")
                if(move.lower()[:1] == "q"):
                    print("Quit.")
                    return
                if(move.isdigit()):
                    move = int(move)
        if(move in game.getMoves()):
            game.move(turn, move)
            turn = comp if turn == human else human
        else:
            print("Illegal move.")
    print(game)
    if game.winner() == human:
        print("Won.")
    elif game.winner() == comp:
        print("Lost.")
    else:
        print("Draw.")

game = c.Connect(connect=4, height=6, width=7)
game.reset()
play(game, m.MiniMax())