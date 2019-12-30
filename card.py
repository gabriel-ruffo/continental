class Card():
    suits = ['HEARTS', 'DIAMONDS', 'SPADES', 'CLUBS']
    values = ['ACE', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'JACK', 'QUEEN', 'KING']

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return "{} of {}".format(self.value, self.suit)

    def get_suit(self):
        return self.suit

    def get_value(self):
        return self.value 
        

# card = Card(Card.suits[0], Card.values[0])
# print(card.get_suit())

# deck = []
# for suit in Card.suits:
#     for value in Card.values:
#         deck.append(Card(suit, value))


# count = 0
# for card in deck:
#     count = count + 1
#     print(card)

# print("{} cards in the deck.".format(count))
