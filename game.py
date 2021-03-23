from player import Player
from ai import AI

class Game:

    def __init__(self):
        self.game = "game"

    def mode(self):
        print("Welcome to Rock Paper Scissors Lizard Spock")
        game_mode = input("Please enter number of players 1 or 2")
        if game_mode == 1:
            Player().pvp()
        elif game_mode == 2:
            AI().pve()


Game().mode()

