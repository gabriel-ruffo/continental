import unittest
from card import Card
from deck import Deck

class TestCardCreation(unittest.TestCase):
    def test_suits(self):
        card_h = Card(Card.suits[0], Card.values[0])
        card_d = Card(Card.suits[1], Card.values[0])
        card_s = Card(Card.suits[2], Card.values[0])
        card_c = Card(Card.suits[3], Card.values[0])
        
        self.assertEqual(card_h.get_suit(), "HEARTS")
        self.assertEqual(card_d.get_suit(), "DIAMONDS")
        self.assertEqual(card_s.get_suit(), "SPADES")
        self.assertEqual(card_c.get_suit(), "CLUBS")

class TestCardPoints(unittest.TestCase):
    def test_points(self):
        ace = Card(Card.suits[0], Card.values[0])
        five_card = Card(Card.suits[0], Card.values[1])
        ten_card = Card(Card.suits[0], Card.values[7])
        joker = Card(Card.suits[-1], Card.values[-1])
        
        self.assertEqual(ace.get_points(), 20)
        self.assertEqual(five_card.get_points(), 5)
        self.assertEqual(ten_card.get_points(), 10)
        self.assertEqual(joker.get_points(), 50)

class TestCardCompare(unittest.TestCase):
    def test_num_compare(self):
        ace = Card(Card.suits[0], Card.values[0])
        two = Card(Card.suits[0], Card.values[1])
        five = Card(Card.suits[0], Card.values[4])
        jack = Card(Card.suits[0], Card.values[10])
        queen = Card(Card.suits[0], Card.values[11])

        self.assertTrue(two.card_less_than(five))
        self.assertFalse(five.card_less_than(two))

        self.assertTrue(five.card_less_than(jack))
        self.assertFalse(jack.card_less_than(two))

        self.assertTrue(jack.card_less_than(queen))
        self.assertFalse(queen.card_less_than(jack))

class TestDeck(unittest.TestCase):
    def test_deck(self):
        deck = Deck()
        deck.make_deck()
        test_card = Card(Card.suits[-1], Card.values[-1])
        deck_card = deck.pop()
        self.assertEqual(deck_card.__str__(), test_card.__str__())

class TestTercia(unittest.TestCase):
    def test_aces(self):
        print("TODO")

    def test_faces(self):
        print("TODO")

    def test_numbers(self):
        print("TODO")

    def test_one_joker(self):
        print("TODO")

    def test_more_than_two_jokers(self):
        print("TODO")
    

if __name__ == '__main__': 
    unittest.main() 