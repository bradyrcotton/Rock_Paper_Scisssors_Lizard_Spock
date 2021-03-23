from player import Player
from gesture import Gesture
import random

class AI(Player):


    def __init__(self):
        self.name = "Wall-E"
        Gesture()
        super().__init__()
    def pvp(self):
        print("Please enter the number of your choice from the gestures below")
        print(Gesture().gestures)
        choice_1 = int(input("Player One Enter Choice: "))
        choice_2 = get_random_number(0, 4)
        print(f"Player 1 chooses {Gesture().gestures[choice_1]}")
        print(f"Bot chooses {Gesture().gestures[choice_2]}")

        Gesture().choice(choice_1, choice_2)


def random_number(min_value, max_value):
    return random.randint(min_value, max_value)


def get_random_number(num_1, num_2):
    random_int = random_number(num_1, num_2)
    return random_int
