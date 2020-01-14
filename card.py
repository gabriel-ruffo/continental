class Card():
    # TODO: Code out Joker functionality to make the base game work first
    suits = ['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS', 'NONE']
    values = ['ACE', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'JACK', 'QUEEN', 'KING', 'JOKER']

    def __init__(self, suit, value):
        """
        Constructor for Card class.
        Parameters:
            suit (str):     The suit value of a card -- 'NONE' reserved for 'JOKER' cards.
            value (str):    The value of a card.
        """
        self.suit = suit
        self.value = value

    def card_to_string(self):
        """
        Returns string representation of card in 'VALUE of SUIT' format.
        Parameters:
            None
        Returns:
            String representation of card.
        """
        return "{} of {}".format(self.value, self.suit)

    def get_suit(self):
        """
        Returns suit value of card object.
        Parameters:
            None
        Returns:
            Suit value of card object.
        """
        return self.suit

    def get_value(self):
        """
        Returns value of card object.
        Parameters:
            None
        Returns:
            Value of card object.
        """
        return self.value
    
    def get_points(self):
        """
        Returns point value of card using conventional
            Continental rules.
        Parameters:
            None
        Returns:
            Point value in int.
        """
        face_values = self.values[10: 13]
        value = self.get_value()
        if isinstance(value, str):
            if value == 'ACE':
                return 20
            elif value in face_values:
                return 10
            else:
                return 50
        elif 2 <= value <= 7:
            return 5
        else:
             return 10

    def card_less_than(self, other):
        """
        Compares two cards based on their index (with
            a couple special cases described below:
            Special Cases:
                A < 2 - KING
                A > 2 - KING
            syntax:   self.card_less_than(other)
            ie:       four.card_less_than(seven) -> true
        Parameters:
            Self object and card to be compared to.
        Returns:
            Whether or not the self value is less than
            the other value as bool.
        """
        # maybe if context cards are high -> high ace
        # vice versa for low ace
        # ie if hand is:
        #   'K' '10' 'J' 'A' then ace is high
        #   '4' '2' '3' 'A' then ace is low
        # TODO: implement ^
        my_value = self.get_value()
        other_value = other.get_value()
        # low ace case
        if my_value == "ACE" and other_value != "ACE":
            return True
        
        # high ace case
        # if my_value != "ACE" and other_value == "ACE":
        #     return True

        # index of values already has the order of cards
        my_value_index = self.values.index(my_value)
        other_value_index = self.values.index(other_value)
        
        return my_value_index < other_value_index