"""Models a hand of cards"""

import json
from card import Card
from ranks import Ranks

class Hand():
    """Models a hand of cards"""

    def __init__(self, game: str=None, cards: list[Card]|None=None,
                 hidden: list[int]|None=None) -> None:
        """Initialize"""
        if cards is None:
            cards = []
        if hidden is None:
            hidden = []
        self.game: str = game
        self.cards: list[Card] = cards
        self._hidden: list[int] = hidden
        self._value: int = self._get_value()

    def _get_hidden(self) -> list[int]:
        """Get the indices for the hidden cards"""
        return self._hidden

    def _set_hidden(self, hidden: list[int]) -> None:
        """Set the indices for the hidden cards"""
        self._hidden = hidden

    hidden = property(
        fget=_get_hidden,
        fset=_set_hidden,
        doc="Indices for hidden cards"
    )

    def _get_value(self) -> int:
        """Get the value for the hand"""
        self._set_value()
        return self._value

    def _set_value(self) -> None:
        """Set the value for the hand"""
        # pylint: disable=consider-using-generator
        self._value = sum([card.value for card in self.cards \
                           if self.cards.index(card) not in self._hidden])

    value = property(
        fget=_get_value,
        fset=_set_value,
        doc="Hand total value"
    )

    def __str__(self) -> str:
        """Return a string representation of the hand"""
        return " ".join([str(self.cards[i]) if i not in self._hidden else "##" for i in range(len(self.cards))])

    def __repr__(self) -> str:
        """Return a string for replication of the hand"""
        cards = []
        for i, card in enumerate(self.cards):
            desc = json.loads(repr(card))
            desc["hidden"] = i in self._hidden
            cards.append(desc)
        return json.dumps({
            "cards": cards,
            "value": self.value,
            "game": self.game
        }, indent=4)

    def show(self, use_glyph: bool=False) -> None:
        """Display the hand as ASCII art or glyphs"""
        back = Card(back=True)
        if use_glyph:
            print(" ".join([self.cards[i].glyph if i not in self._hidden \
                            else back.glyph for i in range(len(self.cards))]))
            return
        for r in range(4):
            print(" ".join([self.cards[i].ascii[r] if i not in self._hidden \
                            else back.ascii[r] for i in range(len(self.cards))]))

    def count(self, rank: Ranks) -> int:
        """Returns the number of cards of a specific rank in the hand"""
        return len([c for c in self.cards if c.rank == rank \
                    and self.cards.index(c) not in self._hidden])
