import unittest
from card import Card
from deck import Deck

# suit examples
heart =     Card(Card.suits[0], Card.values[0])
diamond =   Card(Card.suits[1], Card.values[0])
spade =     Card(Card.suits[2], Card.values[0])
club =      Card(Card.suits[3], Card.values[0])

# value examples
ace =       Card(Card.suits[0], Card.values[0])
two =       Card(Card.suits[0], Card.values[1])
three =     Card(Card.suits[0], Card.values[2])
four =      Card(Card.suits[0], Card.values[3])
five =      Card(Card.suits[0], Card.values[4])
six =       Card(Card.suits[0], Card.values[5])
seven =     Card(Card.suits[0], Card.values[6])
eight =     Card(Card.suits[0], Card.values[7])
nine =      Card(Card.suits[0], Card.values[8])
ten =       Card(Card.suits[0], Card.values[9])
jack =      Card(Card.suits[0], Card.values[10])
queen =     Card(Card.suits[0], Card.values[11])
king =      Card(Card.suits[0], Card.values[12])
joker =     Card(Card.suits[4], Card.values[13])

class TestCardCreation(unittest.TestCase):
    def test_suits(self):        
        self.assertEqual(heart.get_suit(), "HEARTS")
        self.assertEqual(diamond.get_suit(), "DIAMONDS")
        self.assertEqual(spade.get_suit(), "SPADES")
        self.assertEqual(club.get_suit(), "CLUBS")

class TestCardPoints(unittest.TestCase):
    def test_points(self):        
        self.assertEqual(ace.get_points(), 20)
        self.assertEqual(five.get_points(), 5)
        self.assertEqual(ten.get_points(), 10)
        self.assertEqual(joker.get_points(), 50)

class TestCardCompare(unittest.TestCase):
    def test_card_compare(self):
        self.assertTrue(two.card_less_than(five))
        self.assertFalse(five.card_less_than(two))

        self.assertTrue(five.card_less_than(jack))
        self.assertFalse(jack.card_less_than(two))

        self.assertTrue(jack.card_less_than(queen))
        self.assertFalse(queen.card_less_than(jack))

        self.assertTrue(ace.card_less_than(queen))
        self.assertTrue(queen.card_less_than(ace))        

class TestDeck(unittest.TestCase):
    def test_deck(self):
        deck = Deck()
        deck.make_deck()
        test_card = Card(Card.suits[-1], Card.values[-1])
        deck_card = deck.pop()
        self.assertEqual(deck_card.card_to_string(), test_card.card_to_string())

class TestDeckSort(unittest.TestCase):
    def test_deck_sort(self):
        deck = Deck()
        deck.add(four)
        deck.add(two)
        deck.add(three)
        print(deck.deck_to_string())

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