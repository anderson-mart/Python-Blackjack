
""" 
    File name: blackjack.py
    Author: Anderson Martinez
    Date last modified: 8-14-2018
    Python Version: 2.7
"""

from random import shuffle

class Deck():
    """A representation of a deck of cards"""
    def __init__(self):
        self.cards_types = ['Spades', 'Hearts ', 'Diamonds', 'Claws']
        self.cards_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']

    def generate_deck(self):
        """Generates the deck of cards, 52 in total. Returns a list"""
        lst = []
        for rank in self.cards_values:
            for suit in self.cards_types:
                lst.append([rank, suit])
        return lst


class Player():
    """A representation of cardgames player"""
    def __init__(self):
        self.player_in = True
        self.player_hand = [deck.pop(), deck.pop()]
        self.player_score_label, self.player_score = Hand().hand_value(self.player_hand)

    def play(self):
        """Lets the user play. Does not return any value"""
        while self.player_in:
            print Hand().translate_hand(self)

            if Hand().hand_value(self.player_hand)[1] == 0:
                break

            if self.player_in:
                play_move = int(raw_input('What will your next move be? (Hit: 1, Stand: 0)\n>>  '))
                if play_move:
                    self.player_in = True
                    self.draw_card(self)
                else:
                    self.player_in = False
        self.player_score_label, self.player_score = Hand().hand_value(self.player_hand)

    def draw_card(self, player):
        """Draws cards from deck to player/dealer hand. Does not return any value."""
        player_str = "You"
        if isinstance(player, Dealer):
            player_str = "Dealer"

        self.player_in = True
        new_player_card = deck.pop()
        self.player_hand.append(new_player_card)
        print "{0} drew a {1} of {2}".format(player_str, new_player_card[0], new_player_card[1])


class Dealer(Player):
    """Represents the dealer, which as a Player, has score,
       hand of cards, and a play method
    """
    def play(self, player):
        """Automatically plays for dealer. Does not return any value"""
        if player.player_score <= 21:
            print Hand().translate_hand(self)

        while Hand().hand_value(self.player_hand)[1] < 17 and player.player_score <= 21:
            if Hand().hand_value(self.player_hand)[1] == 0:
                break
            self.draw_card(self)
        self.player_score_label, self.player_score = Hand().hand_value(self.player_hand)


class Hand():
    """Representation of a Hand of cards"""
    def __init__(self):
        pass

    def hand_value(self, hand):
        """Calculates the value of a given hand. Returns a list"""

        raw_value = 0
        for card in hand:
            raw_value = raw_value + self.calculate_card_value(card)

        num_aces = 0
        for card in hand:
            if card[0] is 'A':
                num_aces = num_aces + 1
        
        while num_aces > 0:
            if raw_value > 21 and 'A' in a.cards_values:
                raw_value = raw_value - 10
                num_aces = num_aces - 1
            else:
                break

        if raw_value < 21:
            return [str(raw_value), raw_value]
        elif raw_value == 21:
            return ['Blackjack!', 21]
        else:
            return ['Bust!', 0]

    def translate_hand(self, player):
        """Translates the hand into a readable sentence. Returns a string"""
        translated_cards = ""
        card_status = str(Hand().hand_value(player.player_hand)[0])
        blackjack = "You are on Blackjack!"
        bust = "You are on a bust!"
        has = "You have: "
        points = " points"
        if isinstance(player, Dealer):
            blackjack = "Dealer is on Blackjack!"
            bust = "Dealer is on a bust!"
            has =  "Dealer has: "

        if card_status == "Blackjack!":
            print blackjack
            points = ""
        elif card_status == "Bust!":
            print bust
            points = ""
    
        for card in player.player_hand:
            translated_cards = "{0} {1} of {2}, ".format(translated_cards,
                                                         card[0], card[1])
        return "{0}{1} which makes {2}{3}".format(has, translated_cards , card_status, points)

    def calculate_card_value(self, card):
        """Gets value in deck of card. Returns an int value"""
        card_value = card[0]
        if card_value in a.cards_values[0:-4]:
            return int(card_value)
        elif card_value is 'A':
            return 11
        else:
            return 10

def calculate_scores():
    """Calculates the final score of the game"""
    if pl.player_score > dealer.player_score:
        print 'You won!'
    elif pl.player_score == dealer.player_score:
        print 'You tied.\nNeither of you win.'
    elif pl.player_score < dealer.player_score:
        print "You lose!"

a = Deck()
deck = a.generate_deck()
shuffle(deck)

pl = Player()
dealer = Dealer()
pl.play()

dealer.play(pl)
calculate_scores()

