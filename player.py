from deck import Deck

class Player():
    def __init__(self):
        self.wins = 0
        self.point_total = 0
        self.hand_in_play = Deck()
        self.beginning_hands = []
        self.finishing_hands = []
        self.downed_hand = []

    def increase_wins(self):
        """
        Increases Player's win's by one.
        Parameters:
            None
        Returns:
            None
        """
        self.wins += 1

    def get_wins(self):
        """
        Returns the Pleyer's amount of wins.
        Parameters:
            None
        Returns:
            Number of wins as int.
        """
        return self.wins

    def increase_points(self, hand):
        """
        Increases Player's total points by given hand.
        Parameters:
            hand: Deck object to have points counted.
        Returns:
            None
        """
        self.point_total += hand.get_points()

    def get_points(self):
        """
        Returns Player's total points.
        Parameters:
            None
        Returns:
            Player's total points as int.
        """
        return self.point_total

    def get_hand_in_play(self):
        """
        Returns Player's hand Deck() object.
        Parameters:
            None
        Returns:
            Player's current hand.
        """
        return self.hand_in_play

    def set_hand_in_play(self, hand):
        """
        Set's the Player's current hand.
        Parameters:
            hand: Deck() to replace the current hand.
        Returns:
            None
        """
        self.hand_in_play = hand

    def get_downed_hand(self):
        """
        Returns the hand that has been played and down.
        Parameters:
            None
        Returns:
            The hand that has been played.
        """
        return self.downed_hand

    def set_downed_hand(self, hand):
        """
        Set's the Player's downed hand after having
            achieved that round's necessary hand.
        Parameters:
            hand: Hand to set Player's downed hand.
        Returns:
            None
        """
        self.downed_hand = hand

    def add_to_beginning_hands(self, hand):
        """
        Adds each round's beginning hand to this Deck()
            list.
        Parameters:
            hand: hand to be added to list.
        Returns:
            None
        """
        self.beginning_hands.append(hand)

    def add_to_finishing_hands(self, hand):
        """
        Adds each round's finishing hand to this Deck()
            list.
        Parameters:
            hand: hand to be added to the list.
        Returns:
            None
        """
        self.finishing_hands.append(hand)