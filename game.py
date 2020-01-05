from deck import Deck
from player import Player

class Game:
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
        self.current_round = 6

    def play_next_round(self):
        self.deck.reinitialize()
        self.clear_player_hands()

        self.deal(self.current_round)
        self.current_round += 1

    def clear_player_hands(self):
        for player in self.players:
            player.set_downed_hand(None)

    def deal(self, round):
        for player in self.players:
            temp_hand = Deck()
            for _ in range(round):
                temp_hand.add(self.deck.pop())
            # DEBUG: print("\nPlayer: {}\nHand: {}\n".format(player, temp_hand.deck_to_string()))
            player.set_hand_in_play(temp_hand)
            player.add_to_beginning_hands(temp_hand)