"""Models a deck of playing cards"""

from random import shuffle
from colors import Colors
from suits import Suits
from ranks import Ranks
from card import Card
from hand import Hand

class Deck(object):
    """Models a deck of playing cards"""
    # pylint: disable=fixme
    # TODO: Add support for jokers

    def __init__(self, game: str=None, color: Colors=Colors.WHITE) -> None:
        """Initialize the deck"""
        self.game = game
        self.back: Card = Card(back=True)
        self.cards: list[Card] = []
        self.used: list[Card] = []
        for suit in Suits:
            for rank in [r for r in Ranks if r.value > 0]:
                self.cards.append(Card(game, suit, rank, color))
        shuffle(self.cards)

    def deal(self, hand: Hand, num_cards: int=1) -> None:
        """Deal cards"""
        for _ in range(num_cards):
            card = self.cards.pop(0)
            self.used.append(card)
            hand.cards.append(card)

    def deal_hand(self, num_cards: int=1) -> Hand:
        """Deal a hand of cards"""
        hand = Hand(self.game)
        self.deal(hand, num_cards)
        return hand
