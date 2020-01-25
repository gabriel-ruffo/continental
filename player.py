from deck import Deck

class Player():
    def __init__(self, hand_in_play = Deck(), beginning_hands = [], 
                    finishing_hands = [], downed_hand = []):
        self.wins = 0
        self.point_total = 0
        self.hand_in_play = hand_in_play
        self.beginning_hands = beginning_hands
        self.finishing_hands = finishing_hands
        self.downed_hand = downed_hand
        self.penalty = True

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

    def get_penalty(self):
        return self.penalty

    def set_penalty(self, value):
        self.penalty = value

    def go_down(self, round):
        """
        Sets the downed hand in place according to the
            current round.
        Parameters:
            round: the current round.
        Returns:
            None
        """
        if round == 6:
            # get players tercias dict
            tercias = self.hand_in_play.find_tercias()

            # get the number of tercias and put em in a list
            tercia_count = 0
            tercia_list = []
            for value, count in tercias.items():
                if count >= 3:
                    tercia_list.append(value)
                    tercia_count += 1

            if tercia_count == 2:
                result = Deck()
                for tercia in tercia_list:
                    # for each tercia
                    for card in self.hand_in_play.get_deck():
                        # check each card in the hand in play
                        if card.get_value() == tercia:
                            # and add it do downed hand
                            result.add(card)

                for card in result.get_deck():
                    # remove downed cards from hand in play
                    self.hand_in_play.get_deck().remove(card)

                self.set_downed_hand(result)
                print("DOWNED HAND:", result.deck_to_string())
        elif round == 7:
            # one tercia, one run
            return
        elif round == 8:
            # two runs
            return
        elif round == 9:
            # three tercias
            return
        elif round == 10:
            # two tercias, one run
            return
        elif round == 11:
            # one tercia, two runs
            return
        elif round == 12:
            # four tercias
            return
        # second 12: three runs, no discard

    def has_gone_down(self):
        """
        Checks to see whether the current player has gone
            down or not, meaning has played the cards
            necessary to achieve the respective round's
            conditions.
        Parameters:
            None
        Returns:
            Boolean indicated whether the player has gone
                down or not.
        """
        if self.downed_hand != None:
            return True
        return False

    def has_won(self):
        """
        Checks to see if the player has won the current round
            by checking to see if they have played a hand
            down and if they have no cards left in their hand-
            in-play.
        Parameters:
            None
        Returns:
            Bool indicating if the player has won the current
                round or not.
        """
        if self.downed_hand != None and not self.hand_in_play.get_deck():
            return True
        return False