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

class TestCardPoints(unittest.TestCase):
    def test_points(self):        
        self.assertEqual(ace.get_points(), 20)
        self.assertEqual(five.get_points(), 5)
        self.assertEqual(ten.get_points(), 10)

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
        deck.add(queen)
        deck.add(ten)
        deck.add(two)
        deck.add(four)
        deck.add(king)
        deck.add(nine)
        deck.add(seven)
        deck.add(six)
        deck.add(jack)
        deck.add(three)
        deck.add(eight)
        deck.add(five)
        self.assertEqual(deck.deck_to_string(), "QUEEN of HEARTS, 10 of HEARTS, 2 of HEARTS, 4 of HEARTS, KING of HEARTS, 9 of HEARTS, 7 of HEARTS, 6 of HEARTS, JACK of HEARTS, 3 of HEARTS, 8 of HEARTS, 5 of HEARTS")
        
        deck.deck_selection_sort()
        self.assertEqual(deck.deck_to_string(), "2 of HEARTS, 3 of HEARTS, 4 of HEARTS, 5 of HEARTS, 6 of HEARTS, 7 of HEARTS, 8 of HEARTS, 9 of HEARTS, 10 of HEARTS, JACK of HEARTS, QUEEN of HEARTS, KING of HEARTS")

class TestTercia(unittest.TestCase):
    def test_empty_deck(self):
        deck = Deck()
        self.assertFalse(deck.is_tercia())

    def test_less_than_three(self):
        deck = Deck()
        deck.add(two)
        deck.add(two)
        self.assertFalse(deck.is_tercia())

    def test_aces(self):
        tdeck = Deck()
        tdeck.add(ace)
        tdeck.add(ace)
        tdeck.add(ace)
        self.assertTrue(tdeck.is_tercia())

        fdeck = Deck()
        fdeck.add(ace)
        fdeck.add(ace)
        fdeck.add(two)
        self.assertFalse(fdeck.is_tercia())

    def test_faces(self):
        tdeck = Deck()
        tdeck.add(jack)
        tdeck.add(jack)
        tdeck.add(jack)
        self.assertTrue(tdeck.is_tercia())

        fdeck = Deck()
        fdeck.add(jack)
        fdeck.add(jack)
        fdeck.add(king)
        self.assertFalse(fdeck.is_tercia())

    def test_numbers(self):
        tdeck = Deck()
        tdeck.add(two)
        tdeck.add(two)
        tdeck.add(two)
        self.assertTrue(tdeck.is_tercia())

        fdeck = Deck()
        fdeck.add(two)
        fdeck.add(two)
        fdeck.add(three)
        self.assertFalse(fdeck.is_tercia())

        fdeck = Deck()
        fdeck.add(two)
        fdeck.add(four)
        fdeck.add(three)
        self.assertFalse(fdeck.is_tercia())

class TestPlayer(unittest.TestCase):
    def test_increase_wins(self):
        bhand = Deck()
        bhand.add(three)
        bhand.add(three)
        bhand.add(three)
        bhand.add(queen)
        bhand.add(queen)
        bhand.add(queen)

        fhand = Deck()
        fhand.add(two)
        fhand.add(two)
        fhand.add(two)
        fhand.add(queen)
        fhand.add(queen)
        fhand.add(queen)

        dhand = Deck()
        dhand.add(two)
        dhand.add(two)
        dhand.add(two)

        player = Player(bhand, bhand, fhand, dhand)

        self.assertEqual(player.get_wins(), 0)
        self.assertEqual(player.get_points(), 0)

        player.increase_points(player.get_hand_in_play())
        self.assertEqual(player.get_points(), 45)

class TestGame(unittest.TestCase):
    def test_game(self):
        # initialize players with empty hands
        player1 = Player(None, [], [], None)
        player2 = Player(None, [], [], None)
        players = []
        players.append(player1)
        players.append(player2)

        # initialize deck
        deck = Deck()
        deck.make_deck()
        deck.shuffle()

        game = Game(deck, players)

        game.setup_next_round()

class TestFindTercias(unittest.TestCase):
    def test_basic_find_tercias(self):
        deck = Deck()
        deck.add(two)
        deck.add(two)
        deck.add(two)
        deck.add(three)
        deck.add(three)
        deck.add(four)
        deck.add(four)
        deck.add(five)
        deck.add(five)
        deck.add(five)
        deck.add(five)
        tercias, possibles = deck.find_tercias()
        self.assertEqual(tercias, [2, 5])
        self.assertEqual(possibles, [3, 4])

if __name__ == '__main__': 
    unittest.main() 