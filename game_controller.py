from deck import Deck
from player import Player
from random import randint


def reset_deck(deck, discard_pile):
    deck.reinitialize()
    # empty the discard pile
    discard_pile = Deck()


def clear_player_hands(players):
        """
            Clears each player's downed hands at the end
                of the round.
            Parameters:
                None
            Returns:
                None
        """
        for player in players:
            player.set_downed_hand(None)


def get_next_worst_card(hand):
        # assumptions:
        #   have all tercias and possibles in hand
        tercias = hand.find_tercias()
        possibles = hand.get_possibles_values(tercias)

        value_to_toss = possibles[randint(0, len(possibles) - 1)]

        return value_to_toss


def get_unnecessary_cards(hand):
        """
            (Currently only works for tercia hands.) Finds
                the most unnecessary cards in the given
                hand. Does so by first getting the current
                tercias and possibles, then iterates through
                the hand to add all other cards to a list.
            Parameters:
                hand: Hand to check for unnecessary cards.
            Returns:
                None
        """
        tercias = hand.find_tercias()
        result = Deck()

        for card in hand.get_deck():
            if card.get_value() in tercias:
                continue
            else:
                result.add(card)

        # TODO:
        # if result is empty, all cards are necessary
        # in which case, get rid of one extra card of
        # tercias if tercia count is > 3 otherwise get
        # rid of a possible
        if len(result.get_deck()) == 0:
            value_to_toss = get_next_worst_card(hand)
            for card in hand.get_deck():
                if card.get_value() == value_to_toss:
                    result.add(card)
                    break

        return result


def get_highest_value_card(hand):
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


def check_discard_pile(players, discard_pile, deck, current_player):
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
        for player in players:
            if player == current_player or player.has_gone_down():
                continue

            # get list of possibles for the player
            deck = player.get_hand_in_play()
            tercias = deck.find_tercias()
            possibles = deck.get_possibles_values(tercias)

            top_card = discard_pile.peek()
            if not top_card:
                return
            elif top_card.get_value() in possibles:
                # top card could be useful for player
                player.get_hand_in_play().add(top_card)
                print(f"PLAYER {players.index(player) + 1} PICKED UP CARD FROM DISCARD PILE: {top_card.card_to_string()}")
                discard_pile.get_deck().remove(top_card)

                player_index = players.index(player)
                current_player_index = players.index(current_player)
                if abs(player_index - current_player_index) > 1:
                    # if player is not next, take penalty card
                    player.get_hand_in_play().add(deck.pop())
                else:
                    player.set_penalty(False)


def check_downed_hands(player, players, hand):
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
        for player_check in players:
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


def check_going_down(current_round, players, player, hand_in_play):
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
            if check_win_conditions(current_round, hand_in_play):
                player.go_down(current_round)
                print(f"PLAYER {players.index(player) + 1} HAS GONE DOWN")
                if player.has_won():
                    print(f"PLAYER {players.index(player) + 1} HAS WON!")
                    return True
                else:
                    return False


def check_win_conditions(current_round, hand):
        """
            Checks if the current hand matches the current
                round's win conditions.
            Parameters:
                hand: hand to check if it contains the
                    necessary cards to win the current
                    round.
            Returns:
                Boolean indicating whether or not that the
                    Player's hand fits the round's win
                    conditions.
        """
        if current_round == 6:
            # two tercias
            tercias = hand.find_tercias()
            tercia_count = hand.get_tercias_count(tercias)

            if tercia_count >= 2:
                return True
            return False
        elif current_round == 7:
            # one tercia, one run
            return False
        elif current_round == 8:
            # two runs
            return False
        elif current_round == 9:
            # three tercias
            return False
        elif current_round == 10:
            # two tercias, one run
            return False
        elif current_round == 11:
            # one tercia, two runs
            return False
        elif current_round == 12:
            # four tercias
            return False
        # second 12: three runs, no discard


def draw_card(deck, player, hand_in_play):
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
            draw_card = deck.pop()
            if draw_card:
                print(f"DRAW: {draw_card.card_to_string()}")
                hand_in_play.add(draw_card)
        else:
            print("PLAYER PICKED UP FROM DISCARD PILE.")
            # reset player's penalty for skipping a draw step
            player.set_penalty(True)


def deal(round, players, deck):
        """
            Deals out the cards to each player and sets their
                hands in play and beginning hands.
            Parameters:
                round: Current round to determine how many
                    cards to hand out
            Returns:
                None
        """
        # for each player in the game
        for player in players:
            temp_hand = Deck()
            # give each player a hand of round # of cards
            for _ in range(round):
                temp_hand.add(deck.pop())
            # give player random hand
            player.set_hand_in_play(temp_hand)
            player.add_to_beginning_hands(temp_hand)