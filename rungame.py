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

    def start_game(self):
        multiplayer = self.multiplayer()
        rounds_to_win = self.rounds()
        if multiplayer:
            self.player_two = Human("Player 2")
        while self.player_one.win_count < rounds_to_win and self.player_two.win_count < rounds_to_win:
            self.player_picks_action(self.player_one)
            if self.player_two.name == "Player 2":
                self.player_picks_action(self.player_two)
            else:
                self.computer_action()
            self.results()
        self.display_winner()
        self.play_again()

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

    def player_picks_action(self, player_turn):
        try:
            print(f"{player_turn.name}: It's your turn!")
            print("Please enter a number 1-5 using numeric keys")
            user_input = int(input(f"Round {self.round}\n"
                                   f"Score: {self.player_one.name} has {self.player_one.win_count}\n"
                                   f"{self.player_two.name} has {self.player_two.win_count}\n"
                                   f"1: Rock\n"
                                   f"2: Paper\n"
                                   f"3: Scissors\n"
                                   f"4: Lizard\n"
                                   f"5: Spock\n"
                                   f"Your pick:")) - 1
            player_turn.action = player_turn.hand_gestures[user_input]
            assert user_input >= 0
        except:
            self.player_picks_action(player_turn)
        print("\n" * 100)

    def computer_action(self):
        print("Wall-e is picking his gesture wisely...")
        self.player_two.pick_gesture()



