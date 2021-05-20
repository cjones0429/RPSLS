from computer import Computer
from human import Human
from gesture import Gesture


class Rungame:
    def __init__(self):
        self.display_welcome()
        self.display_rules()
        self.player_one = Human(input("Please enter a name for Player One:"))
        self.player_two = Computer()
        self.round = 1

    def display_welcome(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")

    def display_rules(self):
        print("These are the rules: \n"
              "Rock crushes Scissors\n"
              "Scissors cuts Paper\n"
              "Paper covers Rock\n"
              "Rock crushes Lizard\n"
              "Lizard poisons Spock\n"
              "Spock smashes Scissors\n"
              "Scissors decapitates Lizard\n"
              "Lizard eats Paper\n"
              "Paper disproves Spock\n"
              "Spock vaporizes Rock\n")

