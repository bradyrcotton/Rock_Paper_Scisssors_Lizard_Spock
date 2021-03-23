from gesture import Gesture


class Player:

    def __init__(self):
        self.name = ""

    def pvp(self):
        print("Please enter the number of your choice from the gestures below")
        print(Gesture().gestures)
        choice_1 = int(input("Player One Enter Choice: "))
        choice_2 = int(input("Player Two Enter Choice: "))
        print(f"Player 1 chooses {Gesture().gestures[choice_1]}")
        print(f"Player 2 chooses {Gesture().gestures[choice_1]}")
        Gesture().choice(choice_1, choice_2)








