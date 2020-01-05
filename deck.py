from card import Card
import random

class Deck():
    def __init__(self):
        self.my_deck = []

    def make_deck(self):
        """
        Method:     Reinitializes the deck object. Goes through
                    suits and values and adds them to the new
                    array, and adds four jokers.
        Parameters: None
        Returns:    None
        """
        # adds all suits and values and avoids 'None' and 'JOKER'
        for suit in range(len(Card.suits) - 1):
            for value in range(len(Card.values) - 1):
                self.my_deck.append(Card(Card.suits[suit], Card.values[value]))
                self.my_deck.append(Card(Card.suits[suit], Card.values[value]))

        # adds jokers to the deck
        for _ in range(4):
            self.my_deck.append(Card(Card.suits[-1], Card.values[-1]))

    def shuffle(self):
        """
        Method:     Shuffles the deck IN PLACE.
        Parameters: None
        Returns:    None
        """
        random.shuffle(self.my_deck)

    def deck_to_string(self):
        # for testing purposes
        card_vals = []
        for card in self.my_deck:
            card_vals.append(card.card_to_string())
        return ', '.join(card_vals)

    def pop(self):
        # self-explanatory
        return self.my_deck.pop()

    def add(self, card):
        # self-explanatory
        self.my_deck.append(card)

    def deck_selection_sort(self):
        # TODO: figure out how to sort the ace; something wrong with sort method during full deck sort
        for i in range(len(self.my_deck)):
            lowest_value_index = i
            for j in range(i + 1, len(self.my_deck)):
                if self.my_deck[j].card_less_than(self.my_deck[lowest_value_index]):
                    lowest_value_index = j
            self.my_deck[i], self.my_deck[lowest_value_index] = self.my_deck[lowest_value_index], self.my_deck[i]

    def get_joker_count(self):
        result = 0
        for card in self.my_deck:
            if card.get_value() == 'JOKER':
                result += 1
        return result

    def get_points(self):
        result = 0
        for card in self.my_deck:
            result += card.get_points()
        return result

    def is_tercia(self):
        # two jokers not okay for 3 hand, okay for 4+
        # initial min hand check
        if len(self.my_deck) < 3:
            return False

        if len(self.my_deck) == 3 and self.get_joker_count() > 1:
            return False

        init = self.my_deck[0].get_value()
        for card in self.my_deck:
            if init != card.get_value() and card.get_value() != 'JOKER':
                return False

        return True