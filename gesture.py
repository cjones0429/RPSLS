class Gesture:
    def __init__(self, gesture):
        self.gesture = gesture
        self.defeats = {}
        if self.gesture == "Rock":
            self.defeats.update({"Scissors": "CRUSHES"})
            self.defeats.update({"Lizard": "CRUSHES"})
        elif self.gesture == "Paper":
            self.defeats.update({"Rock": "COVERS"})
            self.defeats.update({"Spock": "DISPROVES"})
        elif self.gesture == "Scissors":
            self.defeats.update({"Paper": "CUTS"})
            self.defeats.update({"Lizard": "DECAPITATES"})
        elif self.gesture == "Lizard":
            self.defeats.update({"Paper": "EATS"})
            self.defeats.update({"Spock": "POISONS"})
        elif self.gesture == "Spock":
            self.defeats.update({"Scissors": "SMASHES"})
            self.defeats.update({"Rock": "VAPORIZES"})

    def result(self, player_one_gesture, player_two_gesture):
        if player_two_gesture in self.defeats.keys():
            return self.defeats[player_two_gesture]
        else:
            return "None"
