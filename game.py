from ai import AI
from human import Human



class Game:

    def __init__(self):
        self.num_players = ""
        self.player_1 = 0
        self.player_2 = 0

    def mode(self):
        if self.num_players == "":
            print("Welcome to Rock Paper Scissors Lizard Spock")
            print("_____________________________________________________")
            print("The rules are as follows:")
            print("Rock crushes Scissors")
            print("Scissors cuts Paper")
            print("Scissors cuts Paper")
            print("Rock crushes Lizard")
            print("Lizard poisons Spock")
            print("Spock smashes Scissors")
            print("Scissors decapitates Lizard")
            print("Lizard eats Paper")
            print("Paper disproves Spock")
            print("Spock vaporizes Rock")
            print("Game is best 2 of 3")
            print("_____________________________________________________")

            self.num_players = int(input("Please enter number of players 1 or 2: "))
        while self.num_players != 1 and self.num_players != 2:
            print("invalid input please try again")
            self.num_players = int(input("Please enter number of players 1 or 2: "))
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
            print("_____________________________________________________")
            print(f"Player 1 Score: {self.player_1}")
            print(f"Player 2 Score: {self.player_2}")
            print("_____________________________________________________")

        if self.player_1 == 2:
            print("_____________________________________________________")
            return print("*************Player 1 is the winner!!!*************")
        elif self.player_2 == 2:
            print("_____________________________________________________")
            return print("*************Player 2 is the winner!!!*************")

    def choice(self, choice_1, choice_2):
        if choice_1 == choice_2:
            print("It's a draw!")
        elif choice_1 == 0 and choice_2 == 1:
            print("Paper covers Rock")
            print("Player 2 wins this round.")
            self.player_2 += 1
        elif choice_1 == 0 and choice_2 == 2:
            print("Rock crushes Scissors")
            print("Player 1 wins this round.")
            self.player_1 += 1
        elif choice_1 == 0 and choice_2 == 3:
            print("Rock crushes Lizard")
            print("Player 1 wins this round.")
            self.player_1 += 1
        elif choice_1 == 0 and choice_2 == 4:
            print("Spock vaporizes Rock")
            print("Player 2 wins this round.")
            self.player_2 += 1
        elif choice_1 == 1 and choice_2 == 0:
            print("Paper covers Rock")
            print("Player 1 wins this round.")
            self.player_1 += 1
        elif choice_1 == 1 and choice_2 == 2:
            print("Scissors cuts Paper")
            print("Player 2 wins this round.")
            self.player_2 += 1
        elif choice_1 == 1 and choice_2 == 3:
            print("Lizard eats Paper")
            print("Player 2 wins this round.")
            self.player_2 += 1
        elif choice_1 == 1 and choice_2 == 4:
            print("Paper disproves Spock")
            print("Player 1 wins this round.")
            self.player_1 += 1
        elif choice_1 == 2 and choice_2 == 0:
            print("Rock crushes Scissors")
            print("Player 2 wins this round.")
            self.player_2 += 1
        elif choice_1 == 2 and choice_2 == 1:
            print("Scissors cuts Paper")
            print("Player 1 wins this round.")
            self.player_1 += 1
        elif choice_1 == 2 and choice_2 == 3:
            print("Scissors decapitates Lizard")
            print("Player 1 wins this round.")
            self.player_1 += 1
        elif choice_1 == 2 and choice_2 == 4:
            print("Spock smashes Scissors")
            print("Player 2 wins this round.")
            self.player_2 += 1
        elif choice_1 == 3 and choice_2 == 0:
            print("Rock crushes Lizard")
            print("Player 2 wins this round.")
            self.player_2 += 1
        elif choice_1 == 3 and choice_2 == 1:
            print("Lizard eats Paper")
            print("Player 1 wins this round.")
            self.player_1 += 1
        elif choice_1 == 3 and choice_2 == 2:
            print("Scissors decapitates Lizard")
            print("Player 2 wins this round.")
            self.player_2 += 1
        elif choice_1 == 3 and choice_2 == 4:
            print("Lizard poisons Spock")
            print("Player 1 wins this round.")
            self.player_1 += 1
        elif choice_1 == 4 and choice_2 == 0:
            print("Spock vaporizes Rock")
            print("Player 1 wins this round.")
            self.player_1 += 1
        elif choice_1 == 4 and choice_2 == 1:
            print("Paper disproves Spock")
            print("Player 2 wins this round.")
            self.player_2 += 1
        elif choice_1 == 4 and choice_2 == 2:
            print("Spock smashes Scissors")
            print("Player 1 wins this round.")
            self.player_1 += 1
        elif choice_1 == 4 and choice_2 == 3:
            print("Lizard poisons Spock")
            print("Player 2 wins this round.")
            self.player_2 += 1


Game().score()
