## Playing Blackjack

[`blackjack.py`](./blackjack.py) puts the card classes together into a
playable game. The player starts with $5,000 and places a bet on each hand.

---

### The Rules

Try to get a hand as close to 21 as possible without going over.

* Kings, queens, and jacks are worth 10. Aces are worth 1 or 11, whichever
  helps the hand more. Other cards are worth their face value.
* A two-card 21 is a **blackjack**. It pays 3 to 2.
* On your first two cards, you can **double down**: double your bet, take
  exactly one more card, and then stop.
* A tie is a **push**, and your bet is returned.
* The dealer reveals their hidden card, then hits until reaching 17.

---

### The Game Loop

`Blackjack.play()` runs the game. Each hand follows the same steps:

```python
def play(self) -> None:
    """Play hands until the player runs out of money or quits"""
    self.show_rules()
    pause()
    while True:
        if self.player_bankroll < 1:
            self.game_over(True)
        bet = self.place_bet()
        self.deal_hand()
        self.play_hand(bet)
```

1. `place_bet()` asks for a bet, or lets the player quit.
2. `deal_hand()` gives two cards to each side. The dealer's second card is
   hidden.
3. `play_hand()` plays the hand and settles the bet.

---

### Naturals Come First

Before the player acts, `play_hand()` checks for a blackjack on either side.
A natural blackjack ends the hand immediately:

```python
if self.is_blackjack(player) or self.is_blackjack(self.dealer_hand):
    ...
```

`is_blackjack()` counts every card, including the hidden one. Otherwise a
hidden ace and a face card would go unnoticed.

---

### The Player's Turn

`player_turn()` shows the hands and asks for a choice. The loop ends when the
hand reaches 21 or the player stands:

```python
def player_turn(self, bet: int) -> int:
    """Let the player hit, stand, or double down; return the final bet"""
    player = self.player_hands[0]
    while True:
        self.show_hands()
        if self.hand_value(player) >= 21:
            return bet
        can_double = len(player.cards) == 2 and self.player_bankroll >= 2 * bet
        ...
```

The `draw()` helper deals one card. If the deck has run out during a long
game, it starts a new shuffled deck first.

---

### The Dealer's Turn and Settling

If the player has not busted, the dealer reveals the hidden card and hits
until reaching 17. Then `play_hand()` compares totals and calls `settle()`:

```python
if dealer_total > 21 or player_total > dealer_total:
    return self.settle("win", bet)
if player_total < dealer_total:
    return self.settle("lose", bet)
return self.settle("push", bet)
```

`settle()` changes the bankroll by the bet, or by 3 to 2 for a blackjack, and
then pauses so the player can read the result.

---

### Try It

Run the game from the folder:

```pwsh
python blackjack.py
```

Play a few hands to see each rule in action, including a double down and a
dealer who busts.

---
