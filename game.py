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
        if len(players) > 4:
            raise ValueError("Only max players of 4")
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


    def get_highest_value_card(self, hand):
        """
            Get's the highest valued card from the given hand.
                Does so by setting the first card as the
                highest, then iterates through the rest of the
                hand to see if any other is higher.
            Parameter:
                hand: Hand to check which card has the highest
                    point value.
            Returns:
                Highest point valued card.
        """
        highest_card = hand.get_deck()[0]
        for card in hand.get_deck()[1:]:
            if highest_card.get_points() <= card.get_points():
                highest_card = card

        return highest_card

    def check_downed_hands(self, player, hand):
        """
            Checks all players' downed hands to see if the
                current player can discard an extra card there.
                Does so by getting all the discarded cards in
                a list. Then for each card in player's hand,
                check against all downed hands to see if they
                can add to them. Then gets rid of those cards
                from the hand.
            Parameters:
                player: Player looking to discard cards.
                hand: Player's current hand.
            Returns:
                None
        """
        downed_hands = []
        for player_check in self.players:
            if player_check.get_downed_hand() != None:
                downed_hands.extend(player_check.get_downed_hand().get_deck())

        discarded_cards = []
        add_to_downed_hand = []

        for card in downed_hands:
            if card in hand.get_deck():
                discarded_cards.append(card)
                add_to_downed_hand.append(card)

        for card in discarded_cards:
            hand.get_deck().remove(card)
                
        return

    def check_discard_pile(self, current_player):
        """
            For each player that is not the current player,
                get a list of their possibles. If the top
                card of the 
            Parameters:
                current_player: Player not checking the 
                                    discard pile.
            Returns:
                None
        """
        for player in self.players:
            if player == current_player or player.has_gone_down():
                continue

            # get list of possibles for the player
            deck = player.get_hand_in_play()
            tercias = deck.find_tercias()
            possibles = deck.get_possibles_values(tercias)

            top_card = self.discard_pile.peek()
            if not top_card:
                return
            elif top_card.get_value() in possibles:
                # top card could be useful for player
                player.get_hand_in_play().add(top_card)
                print(f"PLAYER {self.players.index(player) + 1} PICKED UP CARD FROM DISCARD PILE: {top_card.card_to_string()}")
                self.discard_pile.get_deck().remove(top_card)

                player_index = self.players.index(player)
                current_player_index = self.players.index(current_player)
                if abs(player_index - current_player_index) > 1:
                    # if player is not next, take penalty card
                    player.get_hand_in_play().add(self.deck.pop())
                else:
                    player.set_penalty(False)

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
            self.check_downed_hands(player, hand)

        if player.has_gone_down():
            hand_copy = hand
        else:
            hand_copy = gc.get_unnecessary_cards(hand)

        # TODO: need to make sure the hand returned has at
        #       least one card to discard
        discard = self.get_highest_value_card(hand_copy)

        # add to the discard pile
        self.discard_pile.add(discard)
        # remove from hand in play
        hand.my_deck.remove(discard)
        print("DISCARDED:", discard.card_to_string())

        self.check_discard_pile(player)

    def draw_card(self, player, hand_in_play):
        """
            If the player hasn't drawn from the discard pile,
                player draws from the deck. Resets the player's
                penalty if did draw from the discard pile.
            Parameters:
                player: Player to draw a card.
                hand_in_play: Player's current hand.
            Returns:
                None
        """
        if player.get_penalty():
            draw_card = self.deck.pop()
            if draw_card:
                print(f"DRAW: {draw_card.card_to_string()}")
                hand_in_play.add(draw_card)
        else:
            print("PLAYER PICKED UP FROM DISCARD PILE.")
            # reset player's penalty for skipping a draw step
            player.set_penalty(True)

    def check_going_down(self, player, hand_in_play):
        """
            Checks if the current player can do down with his/her
                current hand. If their hand meets the round's win
                condition, they go down. If going down makes the
                player win, returns as such.
            Parameters:
                player: Player to be checked.
                hand_in_play: Player's current hand.
            Returns:
                Bool containing whether or not round is over
                    from player going down.
        """
        if not player.has_gone_down():
            if gc.check_win_conditions(self.current_round, hand_in_play):
                player.go_down(self.current_round)
                print(f"PLAYER {self.players.index(player) + 1} HAS GONE DOWN")
                if player.has_won():
                    print(f"PLAYER {self.players.index(player) + 1} HAS WON!")
                    return True
                else:
                    return False

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
                self.draw_card(player, hand_in_play)

                # sort the current hand
                hand_in_play.deck_selection_sort()
                print(f"HAND: {hand_in_play.deck_to_string()}")

                # call logic to see if player can go down/make player go down
                round_is_over = self.check_going_down(player, hand_in_play)
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