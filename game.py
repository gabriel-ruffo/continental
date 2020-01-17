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
        # might have to change this incr to after the round
        # is over
        self.play()
        self.current_round += 1

    def clear_player_hands(self):
        for player in self.players:
            player.set_downed_hand(None)


    def check_win_conditions(self, deck):
        if self.current_round == 6:
            # two tercias
            return
        elif self.current_round == 7:
            # one tercia, one run
            return
        elif self.current_round == 8:
            # two runs
            return
        elif self.current_round == 9:
            # three tercias
            return
        elif self.current_round == 10:
            # two tercias, one run
            return
        elif self.current_round == 11:
            # one tercia, two runs
            return
        elif self.current_round == 12:
            # four tercias
            return
        # second 12: three runs, no discard

    def play(self):
        for player in self.players:
            hand_in_play = player.get_hand_in_play()
            # draw a card
            hand_in_play.add(self.deck.pop())

            # sort the current hand
            hand_in_play.deck_selection_sort()

            self.check_win_conditions(hand_in_play)

            
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


player1 = Player(None, [], [], None)
player2 = Player(None, [], [], None)
players = []
players.append(player1)
players.append(player2)

game = Game(players)
game.setup_next_round()