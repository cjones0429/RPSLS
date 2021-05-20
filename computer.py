from player import Player
import random


class Computer(Player):
    def __init__(self):
        self.name = "Wall-e"
        super().__init__()

    def pick_gesture(self):
        self.action = self.hand_gestures[random.randint(0, 4)]
