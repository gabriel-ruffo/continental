from deck import Deck
from player import Player


def check_win_conditions(current_round, hand):
        """
            Checks if the current hand matches the current
                round's win conditions.
            Parameters:
                hand: hand to check if it contains the
                    necessary cards to win the current
                    round.
            Returns:
                Boolean indicating whether or not that the
                    Player's hand fits the round's win
                    conditions.
        """
        if current_round == 6:
            # two tercias
            tercias = hand.find_tercias()
            tercia_count = hand.get_tercias_count(tercias)

            if tercia_count >= 2:
                return True
            return False
        elif current_round == 7:
            # one tercia, one run
            return False
        elif current_round == 8:
            # two runs
            return False
        elif current_round == 9:
            # three tercias
            return False
        elif current_round == 10:
            # two tercias, one run
            return False
        elif current_round == 11:
            # one tercia, two runs
            return False
        elif current_round == 12:
            # four tercias
            return False
        # second 12: three runs, no discard


def deal(round, players, deck):
        """
            Deals out the cards to each player and sets their
                hands in play and beginning hands.
            Parameters:
                round: Current round to determine how many
                    cards to hand out
            Returns:
                None
        """
        # for each player in the game
        for player in players:
            temp_hand = Deck()
            # give each player a hand of round # of cards
            for _ in range(round):
                temp_hand.add(deck.pop())
            # give player random hand
            player.set_hand_in_play(temp_hand)
            player.add_to_beginning_hands(temp_hand)