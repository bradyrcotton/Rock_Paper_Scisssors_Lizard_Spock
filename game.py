from ai import AI
from human import Human
from gesture import Gesture
from player import Player
class Game:

    def __init__(self):
        self.game = "game"

    def mode(self):
        print("Welcome to Rock Paper Scissors Lizard Spock")
        game_mode = 2
        if game_mode == 1:
            Human().pvp()
        elif game_mode == 2:
            AI().pvp()
    def score(self):
        while Gesture().choice().player_1 != 2 or Gesture().choice().player_2 != 2:
            Game().mode()
        if Gesture().choice().player_1 == 2:
            print("Player 1 is the winner!!!")
        elif Gesture().choice().player_2 == 2:
            print("Player 2 is the winner!!!")



# input("Please enter number of players 1 or 2")
