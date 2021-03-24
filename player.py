from gesture import Gesture


class Player:

    def __init__(self):
        self.choice_1 = ""
        self.choice_2 = ""

    def pvp(self):
        print("Please enter the number of your choice from the gestures below")
        print(Gesture().gestures)
        self.choice_1 = int(input("Player 1 Enter Choice: "))
        while self.choice_1 != 0 and self.choice_1 != 1 and self.choice_1 != 2 and self.choice_1 != 3 and self.choice_1 != 4:
            print("Invalid input please try again")
            self.choice_1 = int(input("Player 1 Enter Choice: "))
        self.choice_2 = int(input("Player 2 Enter Choice: "))
        while self.choice_2 != 0 and self.choice_2 != 1 and self.choice_2 != 2 and self.choice_2 != 3 and self.choice_2 != 4:
            print("Invalid input please try again")
            self.choice_2 = int(input("Player 2 Enter Choice: "))
        print("_____________________________________________________")
        print(f"Player 1 chooses {Gesture().gestures[self.choice_1]}")
        print(f"Player 2 chooses {Gesture().gestures[self.choice_2]}")
        print("_____________________________________________________")
        return self.choice_1, self.choice_2







