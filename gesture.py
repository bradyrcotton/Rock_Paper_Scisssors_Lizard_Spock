class Gesture:

    def __init__(self):
        self.gestures = ["[1]Rock", "[2]Paper", "[3]Scissors", "[4]Lizard", "[5]Spock"]


    def choice(self,choice_1,choice_2):
        # print("Please enter the number of your choice from the gestures below")
        # print(" [1]Rock", "[2]Paper", "[3]Scissors", "[4]Lizard", "[5]Spock")
        player_1 = 0
        player_2 = 0
        # choice_1 = int(input("Player One Enter Choice"))
        # choice_2 = int(input("Player Two Enter Choice"))
        if choice_1 == choice_2:
            print("It's a draw!")
        elif choice_1 == 1 and choice_2 == 2:
            print("Paper covers Rock")
            player_2 += 1
        elif choice_1 == 1 and choice_2 == 3:
            print("Rock crushes Scissors")
            player_1 += 1
        elif choice_1 == 1 and choice_2 == 4:
            print("Rock crushes Lizard")
            player_1 += 1
        elif choice_1 == 1 and choice_2 == 5:
            print("Spock vaporizes Rock")
            player_2 += 1
        elif choice_1 == 2 and choice_2 == 1:
            print("Paper covers Rock")
            player_1 += 1
        elif choice_1 == 2 and choice_2 == 3:
            print("Scissors cuts Paper")
            player_2 += 1
        elif choice_1 == 2 and choice_2 == 4:
            print("Lizard eats Paper")
            player_2 += 1
        elif choice_1 == 2 and choice_2 == 5:
            print("Paper disproves Spock")
            player_1 += 1
        elif choice_1 == 3 and choice_2 == 1:
            print("Rock crushes Scissors")
            player_2 += 1
        elif choice_1 == 3 and choice_2 == 2:
            print("Scissors cuts Paper")
            player_1 += 1
        elif choice_1 == 3 and choice_2 == 4:
            print("Scissors decapitates Lizard")
            player_1 += 1
        elif choice_1 == 3 and choice_2 == 5:
            print("Spock smashes Scissors")
            player_2 += 1
        elif choice_1 == 4 and choice_2 == 1:
            print("Rock crushes Lizard")
            player_2 += 1
        elif choice_1 == 4 and choice_2 == 2:
            print("Lizard eats Paper")
            player_1 += 1
        elif choice_1 == 4 and choice_2 == 3:
            print("Scissors decapitates Lizard")
            player_2 += 1
        elif choice_1 == 4 and choice_2 == 5:
            print("Lizard poisons Spock")
            player_1 += 1
        elif choice_1 == 5 and choice_2 == 1:
            print("Spock vaporizes Rock")
            player_1 += 1
        elif choice_1 == 5 and choice_2 == 2:
            print("Paper disproves Spock")
            player_2 += 1
        elif choice_1 == 5 and choice_2 == 3:
            print("Spock smashes Scissors")
            player_1 += 1
        elif choice_1 == 5 and choice_2 == 4:
            print("Lizard poisons Spock")
            player_2 += 1
        else:
            if player_1 == 1:
                print("Player One wins this round!")
                return player_1
            elif player_2 == 1:
                print("Player Two wins this round!")
                return player_2






