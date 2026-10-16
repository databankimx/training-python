## Test

[`test.py`](./test.py) is a manual check of the `Deck` and `Hand` classes. It
has no pass or fail checks. It prints what the classes produce, so you can
look at the output and confirm it's right.

Run it with the step's Run button, or from this folder:

```pwsh
python test.py
```

---

### What It Shows

The script has two screens. It clears the terminal between them, and the deck
screen waits for you before it moves on:

1. **The deck:** all 52 cards, in four rows of thirteen, drawn with each card's
   ASCII art. The script pauses here.
2. **A hand:** five cards dealt from a poker deck, shown as text and then as
   glyphs. The hand is then shown again with its last three cards hidden. The
   blackjack lesson uses hidden cards for the dealer.
3. **Game and value:** the game the hand belongs to, and its value.

---

### Viewing a Hand as Data

The end of the script has a commented-out section that prints the hand's
`repr()`. Remove the `#` characters to see it. This is handy when you want to
check the object's data rather than its display.

---
