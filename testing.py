import unittest
from card import Card
from deck import Deck

class TestCardCreation(unittest.TestCase):
    def testSuits(self):
        card_h = Card(Card.suits[0], Card.values[0])
        card_d = Card(Card.suits[1], Card.values[0])
        card_s = Card(Card.suits[2], Card.values[0])
        card_c = Card(Card.suits[3], Card.values[0])
        self.assertEqual(card_h.get_suit(), "HEARTS")
        self.assertEqual(card_d.get_suit(), "DIAMONDS")
        self.assertEqual(card_s.get_suit(), "SPADES")
        self.assertEqual(card_c.get_suit(), "CLUBS")

class TestDeck(unittest.TestCase):
    def testDeck(self):
        deck = Deck([])
        deck.make_deck()
        test_card = Card(Card.suits[-1], Card.values[-1])
        deck_card = deck.pop()
        self.assertEqual(deck_card.__str__(), test_card.__str__())
    

if __name__ == '__main__': 
    unittest.main() 