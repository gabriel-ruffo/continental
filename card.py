class Card():
    suits = ['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS', 'NONE']
    values = ['ACE', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'JACK', 'QUEEN', 'KING', 'JOKER']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value 