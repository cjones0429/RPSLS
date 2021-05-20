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

    def multiplayer(self):
        try:
            user_input = int(input("Press '1' for SinglePlayer and '2' for MultiPlayer"))
            if user_input == 1:
                return False
            elif user_input == 2:
                return True
        except:
            print("Invalid Input. Please press the number key '1' for SinglePlayer or '2' for Multiplayer")
            return self.multiplayer()

    def rounds(self):
        try:
            number = int(input("How many rounds to win? Please enter a number greater than or equal to 2  (i.e 2,3,4)"))
            if number < 2:
                print("You need to win at least 2 rounds")
                return self.rounds()
            return number
        except:
            print("Please enter a number using the numeric keys")
            return self.rounds()



