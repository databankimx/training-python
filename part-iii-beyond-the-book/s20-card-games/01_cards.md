## Cards, Suits, and Ranks

A playing card is made of three pieces of information: a suit, a rank, and
a color for the suit symbol. Python's `Enum` class is a good fit for values
like these, because each choice is one of a fixed set of named options.

---

### Suits and Colors

[`suits.py`](./suits.py) defines the four suits as an `Enum`. Each suit has
a number, and the `glyph()` method returns the matching Unicode symbol.

```python
from enum import Enum
from colors import Colors

class Suits(Enum):
    """Defines the suits in a deck of card"""
    SPADES = 0
    HEARTS = 1
    DIAMONDS = 2
    CLUBS = 3
```

Unicode has separate symbols for hollow (white) and filled (black) suits. The
`Colors` enum chooses between them.

---

### Ranks

[`ranks.py`](./ranks.py) defines the thirteen ranks from `ACE` to `KING`, plus
`BACK` for the face-down side of a card.

```python
class Ranks(Enum):
    """Defines the ranks in a deck of cards"""
    BACK = 0
    ACE = 1
    TWO = 2
    # ... THREE through TEN ...
    JACK = 11
    QUEEN = 12
    KING = 13
```

The classmethods `name()` and `initial()` return the full name and the
abbreviation of a rank. They read the member's name from `_name_`. The
classmethod `name()` hides the `.name` attribute that Enum provides, so
`_name_` is the way to get the underlying name:

```python
Ranks.name(Ranks.QUEEN)      # "Queen"
Ranks.initial(Ranks.QUEEN)   # "Q"
Ranks.initial(Ranks.TEN)     # "10"
```

---

### A Single Card

[`card.py`](./card.py) combines these pieces into a `Card`. The constructor
accepts a suit, a rank, and a color, and it also builds the values the card
needs to display itself: a short string, a Unicode glyph, and ASCII art.

```python
from card import Card
from suits import Suits
from ranks import Ranks

card = Card(suit=Suits.HEARTS, rank=Ranks.QUEEN)
print(card)           # Q♡ (white, hollow suit symbol)
print(card.name)      # Queen of Hearts
print(card.value)     # 12
```

The `back` argument builds a face-down card, which is used to hide cards in
a hand:

```python
back = Card(back=True)
print(back.name)      # Back
```

---
