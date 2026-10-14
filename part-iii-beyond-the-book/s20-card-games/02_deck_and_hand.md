## Decks and Hands

A `Deck` holds all fifty-two cards, shuffled, and deals them out. A `Hand`
holds the cards a player or dealer is holding.

---

### Building a Deck

[`deck.py`](./deck.py) creates one card for every suit and rank (skipping
`BACK`), then shuffles the list:

```python
from deck import Deck

deck = Deck()
print(len(deck.cards))    # 52
```

Dealing removes the top card from the deck and adds it to the hand:

```python
hand = deck.deal_hand(2)  # a new Hand with two cards
print(len(deck.cards))    # 50
```

The `game` argument affects card values. Passing `"blackjack"` makes the
face cards worth 10, and passing `"poker"` makes aces high.

---

### Hands and Hidden Cards

[`hand.py`](./hand.py) stores a list of cards. Some cards in a hand can be
hidden, which is how the dealer keeps one card face-down in blackjack. A
hidden card is listed by index, and it is left out of the hand's value:

```python
from hand import Hand

hand = deck.deal_hand(3)
hand.hidden = [2]                # hide the third card
print(hand)                      # shows "##" for the hidden card
print(hand.value)                # total of the visible cards only
hand.show()                      # ASCII art, with hidden cards drawn face-down
hand.show(use_glyph=True)        # the same hand as Unicode symbols
```

The `hidden` property is a setter and a getter, so you can assign a new list
at any time. The `value` property is recalculated each time you read it.

---

### Printing a Hand as Data

`repr(hand)` returns the hand as JSON, showing each card and whether it is
hidden. Each card's `repr()` provides its rank and suit.

```python
print(repr(hand))
```

---

### Trying the Deck and Hand

[`test.py`](./test.py) is a short demonstration of this section. It creates a
poker deck, shows all fifty-two cards in a grid, deals a hand of five cards,
hides three of them, and prints the hand both ways:

```pwsh
python test.py
```

The script pauses between screens, so you can read each one before it clears.
It also prints the hand's value, counting only the visible cards.

---
