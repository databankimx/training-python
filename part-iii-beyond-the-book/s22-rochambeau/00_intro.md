## Rochambeau (Rock, Paper, Scissors)

Rock, paper, scissors is a simple game, but a computer opponent can play it
in more than one way. This lesson builds a game that plays random moves or
follows a simple strategy.

The code is in this folder:

* [`main.py`](./main.py) - asks whether the computer should use a strategy, then starts the game
* [`rock_paper_scissors.py`](./rock_paper_scissors.py) - the game itself

Run the game:

```pwsh
python main.py
```

Enter `r`, `p`, or `s` to play, or `q` to quit.

---

### Who Beats Whom

The game stores each action's rules in a dictionary. `BEATS` maps each action
to the one it beats, and `BEATEN_BY` is the reverse of that table:

```python
BEATS = {"r": "s", "p": "r", "s": "p"}
BEATEN_BY = {beaten: beater for beater, beaten in BEATS.items()}
```

So `BEATS["r"]` is `"s"`, because rock beats scissors. And `BEATEN_BY["r"]` is
`"p"`, because paper beats rock. Deriving one table from the other means the
rules are written only once.

---

### Turns

`turn()` asks the computer for an action, decides who won, and reports the
result:

```python
if computer == player:
    self.last_result = "ties"
elif BEATS[computer] == player:
    self.last_result = "wins"
else:
    self.last_result = "loses"
```

The result is from the computer's point of view. "wins" means the computer
won the turn.

---

### Strategy: Win-Stay, Lose-Shift

Without a strategy, the computer picks at random. With a strategy, it uses
what happened on the last turn:

* **After the computer wins**, the player probably loses and will switch to the
  action that beats the computer's last move. The computer picks the action
  that beats that switch: `BEATEN_BY[BEATEN_BY[last_computer]]`.
* **After the computer loses**, the player probably sticks with the move that
  won. The computer picks the action that beats the player's last move:
  `BEATEN_BY[last_player]`.
* **After a tie**, or on the first turn, the computer picks at random.

```python
def computer_choice(self):
    """Choose the computer's action, using win-stay/lose-shift if active"""
    if self.use_strategy and self.last_result == "wins":
        return BEATEN_BY[BEATEN_BY[self.last_computer]]
    if self.use_strategy and self.last_result == "loses":
        return BEATEN_BY[self.last_player]
    return choice(list(BEATS))
```

---

### Try It

Play a few games with and without a strategy. The strategy is built around a
player who stays with a winning move and shifts after losing, so it should
win more often against a player who plays that way.

---
