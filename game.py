from deck import Deck
from card import Card
from player import Player
from collections import Counter
import sys

class Game:
    def __init__(self, players):
        self.deck = Deck()
        self.discard_pile = Deck()
        self.players = players
        self.current_round = 6

    def setup_next_round(self):
        """
        Sets up the next round by reinitializing the
            deck, emptying the discard pile, clearing
            each player's hands, dealing them their new
            hands, and playing that round.
        Parameters:
            None
        Returns:
            None
        """
        # reset the deck
        self.deck.reinitialize()
        # empty the discard pile
        self.discard_pile = Deck()
        # clear each player's hands
        self.clear_player_hands()

        self.deal(self.current_round)
        self.play()
        self.current_round += 1

    def clear_player_hands(self):
        """
        Clears each player's downed hands at the end
            of the round.
        Parameters:
            None
        Returns:
            None
        """
        for player in self.players:
            player.set_downed_hand(None)


    def check_win_conditions(self, hand):
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
        if self.current_round == 6:
            # two tercias
            tercias, _ = hand.find_tercias()
            if len(tercias) >= 2:
                print("WIN TERCS:", tercias)
                return True
            return False
        elif self.current_round == 7:
            # one tercia, one run
            return False
        elif self.current_round == 8:
            # two runs
            return False
        elif self.current_round == 9:
            # three tercias
            return False
        elif self.current_round == 10:
            # two tercias, one run
            return False
        elif self.current_round == 11:
            # one tercia, two runs
            return False
        elif self.current_round == 12:
            # four tercias
            return False
        # second 12: three runs, no discard

    def get_unnecessary_cards(self, hand):
        """
        (Currently only works for tercia hands.) Finds
            the most unnecessary cards in the given
            hand. Does so by first getting the current
            tercias and possibles, then iterates through
            the hand to add all other cards to a list.
        Parameters:
            hand: Hand to check for unnecessary cards.
        Returns:
            None
        """
        tercias, possibles = hand.find_tercias()
        result = Deck()

        print("\nHAND     :", hand.deck_to_string())
        print("TERCIAS  :", tercias)
        print("POSSIBLES:", possibles)

        for card in hand.my_deck:
            if card.get_value() in tercias or card.get_value() in possibles:
                continue
            else:
                result.add(card)

        # TODO:
        # if result is empty, all cards are necessary
        # in which case, get rid of one extra card of
        # tercias if tercia count is > 3 otherwise get
        # rid of a possible
        print("NEW HAND :", result.deck_to_string())
        return result


    def get_highest_value_card(self, hand):
        """
        Get's the highest valued card from the given hand.
            Does so by setting the first card as the
            highest, then iterates through the rest of the
            hand to see if any other is higher.
        Parameter:
            hand: Hand to check which card has the highest
                point value.
        Returns:
            Highest point valued card.
        """
        highest_card = hand.my_deck[0]
        for card in hand.my_deck[1:]:
            if highest_card.get_points() <= card.get_points():
                highest_card = card

        return highest_card

    def check_downed_hands(self, player, hand):
        downed_hands = []
        for player_check in self.players:
            if player_check.get_downed_hand() != None:
                downed_hands.append(player_check.get_downed_hand())

        discarded_cards = []
        for card_to_discard in hand.my_deck:
            for downed_hand in downed_hands:
                for card_to_check in downed_hand.my_deck:
                    if card_to_check.get_value() == card_to_discard.get_value():
                        downed_hand.add(card_to_discard)
                        discarded_cards.append(card_to_discard)

        for card in discarded_cards:
            if card in hand:
                hand.my_deck.remove(card)
                
        return

    def discard(self, hand, player):
        """
        Discards the least helpful card in the current
            live hand. Uses a helper method to determine
            the card with the highest point value. Later
            on, will have to implement which card is
            least useful if all cards are currently
            being used in a possible play.
        Parameters:
            hand: Hand from which to get the least
                helpful card.
        Returns:
            None
        """
        if player.has_gone_down():
            self.check_downed_hands(player, hand)

        hand_copy = self.get_unnecessary_cards(hand)

        # TODO: need to make sure the hand returned has at
        #       least one card to discard
        print("UNNECES:", hand_copy.deck_to_string())

        discard = self.get_highest_value_card(hand_copy)
        print("DISCARD:", discard.card_to_string())
        print("\n\n")

        # add to the discard pile
        self.discard_pile.add(discard)
        # remove from hand in play
        hand.my_deck.remove(discard)


    def play(self):
        """
        Performs a Player's basic turn:
            - Get current hand
            - Draw a card
            - Sort the hand
            - Check if can go down
            - Discard least helpful card
        Parameters:
            None
        Returns: 
            None
        """
        for player in self.players:
            # hand in play was set by deal()
            hand_in_play = player.get_hand_in_play()

            # draw a card
            # TODO: implement drawing from the discard pile
            hand_in_play.add(self.deck.pop())

            # sort the current hand
            hand_in_play.deck_selection_sort()

            if not player.has_gone_down():
                if self.check_win_conditions(hand_in_play):
                    player.go_down(self.current_round)
                    if player.has_won():
                        print("Player {} has won this round!".format(player))
                        sys.exit()

            self.discard(hand_in_play, player)
            # TODO: after discard, see if other players 
            #       want the discarded card
            if player.has_won():
                print("Player {} has won this round!".format(player))
                # self.setup_next_round()

        self.play()

            
    def deal(self, round):
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
        for player in self.players:
            temp_hand = Deck()
            # give each player a hand of round # of cards
            for _ in range(round):
                temp_hand.add(self.deck.pop())
            # give player random hand
            player.set_hand_in_play(temp_hand)
            player.add_to_beginning_hands(temp_hand)


# players = [Player(), Player()]

# game = Game(players)
# game.setup_next_round()