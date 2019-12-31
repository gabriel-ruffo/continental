class Player():
    def __init__(self, hand_in_play, downed_hand, 
                    wins, point_total, beginning_hands, 
                    finishing_hands):
        self.hand_in_play = hand_in_play
        self.downed_hand = downed_hand
        self.wins = 0
        self.point_total = 0
        self.beginning_hands = beginning_hands
        self.finishing_hands = finishing_hands

    def increase_wins(self):
        self.wins += 1

    def increase_points(self, amount):
        self.point_total += amount

    def add_to_beginning_hands(self, hand):
        self.beginning_hands.append(hand)

    def add_to_finishing_hands(self, hand):
        self.finishing_hands.append(hand)