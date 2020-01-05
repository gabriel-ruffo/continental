class Player():
    def __init__(self, hand_in_play, beginning_hands,
                    finishing_hands, downed_hand):
        self.wins = 0
        self.point_total = 0
        self.hand_in_play = hand_in_play
        self.beginning_hands = beginning_hands
        self.finishing_hands = finishing_hands
        self.downed_hand = downed_hand

    def increase_wins(self):
        self.wins += 1

    def get_wins(self):
        return self.wins

    def increase_points(self, hand):
        self.point_total += hand.get_points()

    def get_points(self):
        return self.point_total

    def get_hand_in_play(self):
        return self.hand_in_play

    def set_hand_in_play(self, hand):
        self.hand_in_play = hand

    def get_downed_hand(self):
        return self.downed_hand

    def set_downed_hand(self, hand):
        self.downed_hand = hand

    def add_to_beginning_hands(self, hand):
        self.beginning_hands.append(hand)

    def add_to_finishing_hands(self, hand):
        self.finishing_hands.append(hand)