import unittest
from card import Card
from deck import Deck
from player import Player
from game import Game

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

class TestCardCreation(unittest.TestCase):
    def test_suits(self):        
        self.assertEqual(heart.get_suit(), "HEARTS")
        self.assertEqual(diamond.get_suit(), "DIAMONDS")
        self.assertEqual(spade.get_suit(), "SPADES")
        self.assertEqual(club.get_suit(), "CLUBS")
    
    def test_values(self):
        self.assertEqual(ace.get_value(), "ACE")
        self.assertEqual(two.get_value(), 2)
        self.assertEqual(three.get_value(), 3)
        self.assertEqual(four.get_value(), 4)
        self.assertEqual(five.get_value(), 5)
        self.assertEqual(six.get_value(), 6)
        self.assertEqual(seven.get_value(), 7)
        self.assertEqual(eight.get_value(), 8)
        self.assertEqual(nine.get_value(), 9)
        self.assertEqual(ten.get_value(), 10)
        self.assertEqual(jack.get_value(), "JACK")
        self.assertEqual(queen.get_value(), "QUEEN")
        self.assertEqual(king.get_value(), "KING")

class TestCardPoints(unittest.TestCase):
    def test_points(self):        
        self.assertEqual(ace.get_points(), 20)
        self.assertEqual(two.get_points(), 5)
        self.assertEqual(three.get_points(), 5)
        self.assertEqual(four.get_points(), 5)
        self.assertEqual(five.get_points(), 5)
        self.assertEqual(six.get_points(), 5)
        self.assertEqual(seven.get_points(), 5)
        self.assertEqual(eight.get_points(), 10)
        self.assertEqual(nine.get_points(), 10)
        self.assertEqual(ten.get_points(), 10)
        self.assertEqual(jack.get_points(), 10)
        self.assertEqual(queen.get_points(), 10)
        self.assertEqual(king.get_points(), 10)

class TestCardCompare(unittest.TestCase):
    def test_card_compare(self):
        self.assertTrue(two.card_less_than(five))
        self.assertFalse(five.card_less_than(two))

        self.assertTrue(five.card_less_than(jack))
        self.assertFalse(jack.card_less_than(two))

        self.assertTrue(jack.card_less_than(queen))
        self.assertFalse(queen.card_less_than(jack))

        self.assertTrue(ace.card_less_than(queen))
        # fix high ace self.assertTrue(queen.card_less_than(ace))        

class TestDeck(unittest.TestCase):
    def test_deck(self):
        deck = Deck()
        deck.make_deck()
        test_card = Card(Card.suits[-1], Card.values[-1])
        deck_card = deck.pop()
        self.assertEqual(deck_card.card_to_string(), test_card.card_to_string())

class TestDeckSort(unittest.TestCase):
    def test_non_ace_deck_sort(self):
        deck = Deck()
        deck.set_deck([ queen, ten, two,
                        four, king, nine,
                        seven, six, jack,
                        three, eight, five])
        self.assertEqual(deck.deck_to_string(), "QUEEN of HEARTS, 10 of HEARTS, 2 of HEARTS, 4 of HEARTS, KING of HEARTS, 9 of HEARTS, 7 of HEARTS, 6 of HEARTS, JACK of HEARTS, 3 of HEARTS, 8 of HEARTS, 5 of HEARTS")
        
        deck.deck_selection_sort()
        self.assertEqual(deck.deck_to_string(), "2 of HEARTS, 3 of HEARTS, 4 of HEARTS, 5 of HEARTS, 6 of HEARTS, 7 of HEARTS, 8 of HEARTS, 9 of HEARTS, 10 of HEARTS, JACK of HEARTS, QUEEN of HEARTS, KING of HEARTS")

class TestPlayer(unittest.TestCase):
    def test_increase_wins(self):
        bhand = Deck()
        bhand.set_deck([three, three, three, queen, queen, queen])

        fhand = Deck()
        fhand.set_deck([two, two, two, queen, queen, queen])

        dhand = Deck()
        dhand.set_deck([two, two, two])

        player = Player()
        player.add_to_beginning_hands(bhand)
        player.set_hand_in_play(bhand)
        player.add_to_finishing_hands(fhand)
        player.set_downed_hand(dhand)

        self.assertEqual(player.get_wins(), 0)
        self.assertEqual(player.get_points(), 0)

        player.increase_points(player.get_hand_in_play())
        self.assertEqual(player.get_points(), 45)

class TestFindTercias(unittest.TestCase):
    def test_find_tercias_one_full_one_poss(self):
        deck = Deck()
        deck.set_deck([ queen, queen, queen, 
                        ten, ten])
        tercias = deck.find_tercias()
        self.assertEqual(tercias, {'QUEEN': 3, 10: 2})

    def test_find_tercias_none(self):
        deck = Deck()
        deck.set_deck([ two, four, five, seven])
        tercias = deck.find_tercias()
        self.assertEqual(tercias, {})

if __name__ == '__main__': 
    unittest.main() 