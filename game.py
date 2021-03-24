from ai import AI
from human import Human
from player import Player


class Game:

    def __init__(self):
        self.num_players = ""
        self.player_1 = 0
        self.player_2 = 0
        # self.ai = AI()
        # self.human = Human()

    def mode(self):
        if self.num_players == "":
            print("Welcome to Rock Paper Scissors Lizard Spock")
            self.num_players = int(input("Please enter number of players 1 or 2"))
        game_mode = self.num_players
        if game_mode == 2:
            choices = Human().pvp()
            self.choice(choices[0], choices[1])
        elif game_mode == 1:
            choices = AI().pvp()
            self.choice(choices[0], choices[1])

    def score(self):

        while self.player_1 != 2 and self.player_2 != 2:
            self.mode()
            print(f"Player 1 Score: {self.player_1}")
            print(f"Player 2 Score: {self.player_2}")
        if self.player_1 == 2:
            return print("Player 1 is the winner!!!")
        elif self.player_2 == 2:
            return print("Player 2 is the winner!!!")

    def choice(self, choice_1, choice_2):
        if choice_1 == choice_2:
            print("It's a draw!")
        elif choice_1 == 0 and choice_2 == 1:
            print("Paper covers Rock")
            self.player_2 += 1
        elif choice_1 == 0 and choice_2 == 2:
            print("Rock crushes Scissors")
            self.player_1 += 1
        elif choice_1 == 0 and choice_2 == 3:
            print("Rock crushes Lizard")
            self.player_1 += 1
        elif choice_1 == 0 and choice_2 == 4:
            print("Spock vaporizes Rock")
            self.player_2 += 1
        elif choice_1 == 1 and choice_2 == 0:
            print("Paper covers Rock")
            self.player_1 += 1
        elif choice_1 == 1 and choice_2 == 2:
            print("Scissors cuts Paper")
            self.player_2 += 1
        elif choice_1 == 1 and choice_2 == 3:
            print("Lizard eats Paper")
            self.player_2 += 1
        elif choice_1 == 1 and choice_2 == 4:
            print("Paper disproves Spock")
            self.player_1 += 1
        elif choice_1 == 2 and choice_2 == 0:
            print("Rock crushes Scissors")
            self.player_2 += 1
        elif choice_1 == 2 and choice_2 == 1:
            print("Scissors cuts Paper")
            self.player_1 += 1
        elif choice_1 == 2 and choice_2 == 3:
            print("Scissors decapitates Lizard")
            self.player_1 += 1
        elif choice_1 == 2 and choice_2 == 4:
            print("Spock smashes Scissors")
            self.player_2 += 1
        elif choice_1 == 3 and choice_2 == 0:
            print("Rock crushes Lizard")
            self.player_2 += 1
        elif choice_1 == 3 and choice_2 == 1:
            print("Lizard eats Paper")
            self.player_1 += 1
        elif choice_1 == 3 and choice_2 == 2:
            print("Scissors decapitates Lizard")
            self.player_2 += 1
        elif choice_1 == 3 and choice_2 == 4:
            print("Lizard poisons Spock")
            self.player_1 += 1
        elif choice_1 == 4 and choice_2 == 0:
            print("Spock vaporizes Rock")
            self.player_1 += 1
        elif choice_1 == 4 and choice_2 == 1:
            print("Paper disproves Spock")
            self.player_2 += 1
        elif choice_1 == 4 and choice_2 == 2:
            print("Spock smashes Scissors")
            self.player_1 += 1
        elif choice_1 == 4 and choice_2 == 3:
            print("Lizard poisons Spock")
            self.player_2 += 1
        else:
            if self.player_1 == 1:
                print("Player One wins this round!")
                return self.player_1
            elif self.player_2 == 1:
                print("Player Two wins this round!")
                return self.player_2

Game().score()