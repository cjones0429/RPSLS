from player import Player


class Human(Player):
    def __init__(self, player):
        self.name = player
        super().__init__()

    def player_one_name(self):
        self.name = input("Enter a name for Player One")


