from deck import Deck
from card import Card
from player import Player
from collections import Counter

class Game:
    def __init__(self, players):
        self.deck = Deck()
        self.discard_pile = Deck()
        self.players = players
        self.current_round = 6

    def setup_next_round(self):
        # reset the deck
        self.deck.reinitialize()
        # empty the discard pile
        self.discard_pile = Deck()
        self.clear_player_hands()

        self.deal(self.current_round)
        # might have to change this incr to after the round
        # is over
        self.play()
        self.current_round += 1

    def clear_player_hands(self):
        for player in self.players:
            player.set_downed_hand(None)


    def check_win_conditions(self, hand):
        if self.current_round == 6:
            # two tercias
            tercias, _ = hand.find_tercias()
            if len(tercias) >= 2:
                print(tercias)
                return True
            return False
        elif self.current_round == 7:
            # one tercia, one run
            return False
        elif self.current_round == 8:
            # two runs
            return False
        elif self.current_round == 9:
            # three tercias
            return False
        elif self.current_round == 10:
            # two tercias, one run
            return False
        elif self.current_round == 11:
            # one tercia, two runs
            return False
        elif self.current_round == 12:
            # four tercias
            return False
        # second 12: three runs, no discard

    def get_unnecessary_cards(self, hand):
        tercias, possibles = hand.find_tercias()
        result = Deck()

        print("HAND     :", hand.deck_to_string())
        print("TERCIAS  :", tercias)
        print("POSSIBLES:", possibles)

        for card in hand.my_deck:
            if card.get_value() in tercias or card.get_value() in possibles:
                continue
            else:
                result.add(card)

        print("NEW HAND :", result.deck_to_string())
        return result


    def get_highest_value_card(self, hand):
        highest_card = hand.my_deck[0]
        for card in hand.my_deck[1:]:
            if highest_card.get_points() <= card.get_points():
                highest_card = card

        return highest_card

    def discard(self, hand):        
        hand_copy = self.get_unnecessary_cards(hand)
        print(hand_copy.deck_to_string())
        print("\n\n")

        discard = self.get_highest_value_card(hand_copy)
        print("DISCARD:", discard.card_to_string())


    def play(self):
        for player in self.players:
            hand_in_play = player.get_hand_in_play()
            # draw a card
            hand_in_play.add(self.deck.pop())

            # sort the current hand
            hand_in_play.deck_selection_sort()

            if self.check_win_conditions(hand_in_play):
                print("Implement go_down()")

            self.discard(hand_in_play)

            
    def deal(self, round):
        # for each player in the game
        for player in self.players:
            temp_hand = Deck()
            # give each player a hand of round # of cards
            for _ in range(round):
                temp_hand.add(self.deck.pop())
            # give player random hand
            player.set_hand_in_play(temp_hand)
            player.add_to_beginning_hands(temp_hand)


player1 = Player()
player2 = Player()
players = []
players.append(player1)
players.append(player2)

game = Game(players)
game.setup_next_round()