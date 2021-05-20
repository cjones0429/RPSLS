from computer import Computer
from human import Human
from gesture import Gesture


class Rungame:
    def __init__(self):
        self.display_welcome()
        self.display_rules()
        self.player_one = Human(input("Please enter a name for Player One:"))
        print("\n" * 2)
        self.player_two = Computer()
        self.round = 1

    def display_welcome(self):
        #first thing you see, displays welcome
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock!")
        print("\n" * 2)

    def display_rules(self):
        #lists out the rules and what gestures defeat/lose to
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
        #lets user select either single player or multiplayer
        try:
            user_input = int(input("Press '1' for SinglePlayer and '2' for MultiPlayer"))
            print("\n" * 2)
            if user_input == 1:
                return False
            elif user_input == 2:
                return True
        except:
            print("Invalid Input. Please press the number key '1' for SinglePlayer or '2' for Multiplayer")
            return self.multiplayer()

    def rounds(self):
        #asks the user how many rounds they need to win in order to win the overall game,
        # has to be at least 2
        try:
            number = int(input("How many rounds to win? Please enter a number greater than or equal to 2  (i.e 2,3,4)"))
            print("\n" * 2)
            if number < 2:
                print("You need to win at least 2 rounds")
                return self.rounds()
            return number
        except:
            print("Please enter a number using the numeric keys")
            return self.rounds()

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

    def player_picks_action(self, player_turn):
        #promts the user to pick their gesture using number keys 1-5
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
        print("\n" * 3)

    def computer_action(self):
        #randomly selects action for computer
        print("Wall-e is picking his gesture wisely...")
        self.player_two.pick_gesture()
        print("\n" * 2)

    def results(self):
        #prints what each player picked and if they picked the same it will print a tie
        print(f"{self.player_two.name} picked: {self.player_two.action}\n"
              f"{self.player_one.name} picked: {self.player_one.action}\n")

        if self.player_one.action == self.player_two.action:
            print("It's a tie!! Pick again! Choose carefully...")
        else:
            self.compare_result()
            self.round += 1

    def compare_result(self):
        #gesture_action = what each gesture does to the other "smashes, cuts, disproves, etc")
        #comparing each gesture to see if its in the class list keys and if it defeats it
        #will add points to winning gesture player win_count
        player_one_hand_gesture = Gesture(self.player_one.action)
        player_two_hand_gesture = Gesture(self.player_two.action)
        gesture_action = player_one_hand_gesture.result(self.player_one.action, self.player_two.action)
        if gesture_action != "None":
            self.player_one.win_count += 1
            self.display_round_result(self.player_one.name, self.player_one.action, self.player_two.name, self.player_two.action, gesture_action)
        else:
            self.player_two.win_count += 1
            gesture_action = player_two_hand_gesture.result(self.player_two.action, self.player_one.action)
            self.display_round_result(self.player_two.name, self.player_two.action, self.player_one.name, self.player_one.action, gesture_action)

    def display_round_result(self, winner, winner_hand_gesture, loser, loser_hand_gesture, gesture_action):
        #ex player1's paper DISPROVES player2's Spock
        print(f"{winner}'s {winner_hand_gesture} {gesture_action} {loser}'s {loser_hand_gesture}")
        print("\n" * 2)

    def display_winner(self):
        if self.player_one.win_count > self.player_two.win_count:
            print(f"{self.player_one.name} is the Champion!!")
        else:
            print(f"{self.player_two.name} is the Champion!!")

    def play_again(self):
        play_again = input("Do you want to play again? Type 'yes' to play again or hit any button to end")
        if play_again == "yes":
            print("Great! Let's play again!")
            self.start_over()

    def start_over(self):
        user_input = input("Is Player One the same? Please enter 'yes' or 'no'")
        if user_input == "yes":
            #this lets the player one name remain the same (can still pick multiplayer
            self.round = 1
            self.player_one.win_count = 0
            self.player_two.win_count = 0
            self.display_welcome()
            self.display_rules()
            self.start_game()
        else:
            #this completely restarts the game
            self.display_welcome()
            self.display_rules()
            self.player_one = Human(input("Please enter a name for Player One:"))
            self.player_two = Computer()
            self.round = 1
            self.start_game()
