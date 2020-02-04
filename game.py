from deck import Deck
from card import Card
from player import Player
from collections import Counter
import sys
import game_controller as gc


class Game:
    def __init__(self, players):
        self.deck = Deck()
        self.discard_pile = Deck()
        if len(players) > 4: raise ValueError("Only max players of 4")
        self.players = players
        self.current_round = 6


    def setup_next_round(self):
        """
            Sets up the next round by reinitializing the
                deck, emptying the discard pile, clearing
                each player's hands, dealing them their new
                hands, and playing that round.
            Parameters:
                None
            Returns:
                None
        """
        # reset the deck
        gc.reset_deck(self.deck, self.discard_pile)
        # clear each player's hands
        gc.clear_player_hands(self.players)
        # deal out round's cards
        gc.deal(self.current_round, self.players, self.deck)

        self.play()
        self.current_round += 1


    def discard(self, hand, player):
        """
            Discards the least helpful card in the current
                live hand. Uses a helper method to determine
                the card with the highest point value. Later
                on, will have to implement which card is
                least useful if all cards are currently
                being used in a possible play.
            Parameters:
                hand: Hand from which to get the least
                    helpful card.
            Returns:
                None
        """
        if player.has_gone_down():
            gc.check_downed_hands(player, self.players, hand)

        if player.has_gone_down():
            hand_copy = hand
        else:
            hand_copy = gc.get_unnecessary_cards(hand)

        # TODO: need to make sure the hand returned has at
        #       least one card to discard
        discard = gc.get_highest_value_card(hand_copy)

        # add to the discard pile
        self.discard_pile.add(discard)
        # remove from hand in play
        hand.my_deck.remove(discard)
        print("DISCARDED:", discard.card_to_string())

        gc.check_discard_pile(self.players, self.discard_pile, self.deck, player)


    def play(self):
        """
            Performs a Player's basic turn:
                - Get current hand
                - Draw a card
                - Sort the hand
                - Check if can go down
                - Discard least helpful card
            Parameters:
                None
            Returns: 
                None
        """
        round_is_over = False
        turn = 1
        while not round_is_over:
            print(f"===============Round:{f'{turn:02}'}===============")
            for player in self.players:
                print("\n")
                print(f"PLAYER {self.players.index(player) + 1}:")
                # hand in play was set by deal()
                hand_in_play = player.get_hand_in_play()
                print(f"HAND: {hand_in_play.deck_to_string()}")

                # draw a card
                gc.draw_card(self.deck, player, hand_in_play)

                # sort the current hand
                hand_in_play.deck_selection_sort()
                print(f"HAND: {hand_in_play.deck_to_string()}")

                # call logic to see if player can go down/make player go down
                round_is_over = gc.check_going_down(self.current_round, self.players, player, hand_in_play)
                if round_is_over:
                    break
                
                # discard a card from hand
                self.discard(hand_in_play, player)

                # check if player won by discarding
                if player.has_won():
                    round_is_over = True
                    print(f"PLAYER {self.players.index(player) + 1} HAS WON!")
                    break
                    # self.setup_next_round()

                print("\n")
            turn += 1
            print("======================================\n\n")


players = [Player(), Player(), Player()]
game = Game(players)

game.setup_next_round()