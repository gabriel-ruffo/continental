from deck import Deck
from player import Player

class Game:
    def __init__(self, players):
        self.deck = Deck()
        self.players = players
        self.current_round = 6

    def setup_next_round(self):
        self.deck.reinitialize()
        self.clear_player_hands()

        self.deal(self.current_round)
        self.current_round += 1
        self.play()

    def clear_player_hands(self):
        for player in self.players:
            player.set_downed_hand(None)

    def play(self):
        for player in self.players:
            player.get_hand_in_play().deck_selection_sort()
            print(player.get_hand_in_play().deck_to_string())
            tercias, possibles = player.get_hand_in_play().find_tercias()
            print("\nfor player {}:".format(self.players.index(player)))
            print(tercias)
            print(possibles)

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