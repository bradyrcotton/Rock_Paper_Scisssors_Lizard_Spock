from gesture import Gesture


class Player:

    def __init__(self):
        self.choice_1 = ""
        self.choice_2 = ""

    def pvp(self):
        print("Please enter the number of your choice from the gestures below")
        print(Gesture().gestures)
        self.choice_p1 = int(input("Player 1 Enter Choice: "))
        self.choice_p2 = int(input("Player 2 Enter Choice: "))
        print(f"Player 1 chooses {Gesture().gestures[self.choice_p1]}")
        print(f"Player 2 chooses {Gesture().gestures[self.choice_p2]}")
        return self.choice_p1, self.choice_p2







