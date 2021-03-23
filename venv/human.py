from player import Player

class Human(Player):
    def pvp(self):
        print("Please enter the number of your choice from the gestures below")
        print(Gesture().gestures)
        choice_1 = int(input("Player One Enter Choice"))
        choice_2 = int(input("Player Two Enter Choice"))
        Gesture().choice(choice_1, choice_2)