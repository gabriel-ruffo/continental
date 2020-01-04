class Card():
    suits = ['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS', 'NONE']
    values = ['ACE', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'JACK', 'QUEEN', 'KING', 'JOKER']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def card_to_string(self):
        return "{} of {}".format(self.value, self.suit)

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value
    
    def get_points(self):
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
        Method:     Compares two cards based on their index (with
                    a couple special cases described below:
                    Special Cases:
                        A < 2 - KING
                        A > 2 - KING
                    syntax:   self.card_less_than(other)
                    ie:       four.card_less_than(seven) -> true
        Parameters: Self object and card to be compared to.
        Returns:    
        """
        my_value = self.get_value()
        other_value = other.get_value()
        # low ace case
        if my_value == "ACE" and other_value != "ACE":
            return True
        
        # high ace case
        if my_value != "ACE" and other_value == "ACE":
            return True

        # index of values already has the order of cards
        my_value_index = self.values.index(my_value)
        other_value_index = self.values.index(other_value)
        
        return my_value_index <= other_value_index