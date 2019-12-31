from card import Card
import random

class Deck():
    def __init__(self, my_deck):
        self.my_deck = my_deck

    def make_deck(self):
        """
        Method:     Reinitializes the deck object. Goes through
                    suits and values and adds them to the new
                    array, and adds four jokers.
        Parameters: None
        Returns:    None
        """
        self.my_deck = []
        # adds all suits and values and avoids 'None' and 'JOKER'
        for suit in range(len(Card.suits) - 1):
            for value in range(len(Card.values) - 1):
                self.my_deck.append(Card(Card.suits[suit], Card.values[value]))
                self.my_deck.append(Card(Card.suits[suit], Card.values[value]))

        # adds jokers to the deck
        self.my_deck.append(Card(Card.suits[-1], Card.values[-1]))
        self.my_deck.append(Card(Card.suits[-1], Card.values[-1]))
        self.my_deck.append(Card(Card.suits[-1], Card.values[-1]))
        self.my_deck.append(Card(Card.suits[-1], Card.values[-1]))

    def shuffle(self):
        """
        Method:     Shuffles the deck IN PLACE.
        Parameters: None
        Returns:    None
        """
        random.shuffle(self.my_deck)

    def __str__(self):
        return print(*self.my_deck, sep=', ')

deck = Deck([])
deck.make_deck()
print(deck.__str__())
deck.shuffle()
print(deck.__str__())