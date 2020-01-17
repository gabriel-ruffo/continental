from card import Card
import random

class Deck():
    def __init__(self):
        """
        Constructor for Deck class. Creates an empty list.
        Parameters:
            None
        """
        self.my_deck = []

    def make_deck(self):
        """
        Reinitializes the deck object. Goes through
            suits and values and adds them to the new
            array.
        Parameters: 
            None
        """
        for suit in range(len(Card.suits)):
            for value in range(len(Card.values)):
                self.my_deck.append(Card(Card.suits[suit], Card.values[value]))
                self.my_deck.append(Card(Card.suits[suit], Card.values[value]))

    def shuffle(self):
        """
        Shuffles the deck IN PLACE.
        Parameters:
            None
        """
        random.shuffle(self.my_deck)

    def reinitialize(self):
        """
        Reinitializes the deck by deleting all of
            the contents, remaking, and reshuffling.
        Parameters:
            None
        """
        del self.my_deck[:]
        self.make_deck()
        self.shuffle()

    def deck_to_string(self):
        """
        Creates a string representation of the deck.
            Mainly for testing purposes.
        Parameters:
            None
        Returns:
            String containing all of the cards' values
            and suits.
        """
        card_vals = []
        for card in self.my_deck:
            card_vals.append(card.card_to_string())
        return ', '.join(card_vals)

    def pop(self):
        """
        Gives caller the next card in the deck.
        Parameters:
            None
        Returns:
            Next card in the deck.
        """
        return self.my_deck.pop()

    def add(self, card):
        """
        Adds a card to the deck.
        Parameters:
            card (Card): The card to be added
        """
        # self-explanatory
        self.my_deck.append(card)

    def deck_selection_sort(self):
        for i in range(len(self.my_deck)):
            lowest_value_index = i
            for j in range(i + 1, len(self.my_deck)):
                if self.my_deck[j].card_less_than(self.my_deck[lowest_value_index]):
                    lowest_value_index = j
            self.my_deck[i], self.my_deck[lowest_value_index] = self.my_deck[lowest_value_index], self.my_deck[i]

    def get_points(self):
        """
        Calculates the total amount of points in a hand/deck.
        Parameters:
            None
        Returns:
            Total point value of hand/deck.
        """
        result = 0
        for card in self.my_deck:
            result += card.get_points()
        return result

    def get_values_count(self, my_value):
        """
        Returns the number of cards that share the given value.
        Parameters:
            my_value (int/str): The value by which the other
                                cards in the deck will be
                                compared against.
        Returns:
            Number of matches.
        """
        result = 0
        for card in self.my_deck:
            if card.get_value() == my_value:
                result += 1
        
        return result

    def find_tercias(self):
        """
        Finds the number of tercias in a hand. By first checking if
            a value has already been looked for, it checks the
            number of occurrences of a card. If the number is three
            or greater, it is added to the tercias array. If it is
            only two, it adds it to a list of possible tercias.
        Parameters:
            None
        Returns:
            Two arrays:
                tercias: array of known tercias
                possibles: array of possible tercias (pairs)
        """
        already_passed = []
        tercias = []
        possibles = []

        for card in self.my_deck:
            my_value = card.get_value()
            if my_value in already_passed:
                continue
            already_passed.append(my_value)
            occurrences = self.get_values_count(my_value)
            if occurrences >= 3:
                tercias.append(my_value)
            elif occurrences == 2:
                possibles.append(my_value)
        return tercias, possibles