from gesture import Gesture


class Player:

    def __init__(self):
        self.name = ""

    def pvp(self):
        print("Please enter the number of your choice from the gestures below")
        print(Gesture().gestures)
        choice_1 = int(input("Player One Enter Choice"))
        choice_2 = int(input("Player Two Enter Choice"))
        Gesture().choice(choice_1, choice_2)
    # def pve(self):
    #     print("Please enter the number of your choice from the gestures below")
    #     print(Gesture().gestures)
    #     choice_1 = int(input("Player One Enter Choice"))
    #     choice_2 = get_random_number(1, 5)
    #
    #     Gesture().choice(choice_1, choice_2)







