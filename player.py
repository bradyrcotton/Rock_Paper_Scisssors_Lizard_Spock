from gesture import Gesture
import random


class Player:

    def __init__(self):
        Gesture()

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


def get_random_number(num_1, num_2):
    random_int = random_number(num_1,num_2)
    return random_int


def random_number(min_value, max_value):
    return random.randint(min_value, max_value)


Player().pvp()
