from player import Player
from gesture import Gesture
import random


class AI(Player):



    def __init__(self):

        super().__init__()



    def pvp(self):

        print("Please enter the number of your choice from the gestures below")
        print(Gesture().gestures)
        self.choice_1 = int(input("Player One Enter Choice: "))
        self.choice_2 = get_random_number(0, 4)
        print("_____________________________________________________")
        print(f"Player 1 chooses {Gesture().gestures[self.choice_1]}")
        print(f"Bot chooses {Gesture().gestures[self.choice_2]}")
        print("_____________________________________________________")
        return self.choice_1, self.choice_2



def random_number(min_value, max_value):
    return random.randint(min_value, max_value)


def get_random_number(num_1, num_2):
    random_int = random_number(num_1, num_2)
    return random_int
