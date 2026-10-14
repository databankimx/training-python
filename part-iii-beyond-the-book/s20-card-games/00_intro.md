## Card Games

Card games are a good way to practice modeling real-world things as classes.
In this lesson we'll build a small playing-card library, then use it to play
a game of blackjack.

The code is in this folder:

* [`colors.py`](./colors.py) - the filled (black) or hollow (white) suit symbols
* [`suits.py`](./suits.py) - the four suits
* [`ranks.py`](./ranks.py) - the thirteen ranks, plus a "back" for face-down cards
* [`card.py`](./card.py) - a single card
* [`deck.py`](./deck.py) - a shuffled deck of cards
* [`hand.py`](./hand.py) - a hand of cards, with hidden cards
* [`blackjack.py`](./blackjack.py) - a complete game of blackjack
* [`test.py`](./test.py) - a demonstration of the deck and hand

The lessons in this section cover each file in turn:

* [Cards, Suits, and Ranks](./01_cards.md)
* [Decks and Hands](./02_deck_and_hand.md)
* [Playing Blackjack](./03_blackjack.md)

> Note: this section uses the `sm_utils` library for clearing the terminal
> and pausing. Install it with `python -m pip install sm_utils`.

---
