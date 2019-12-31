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