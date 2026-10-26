# Deleting Old Bullets

## What this step does

A bullet that leaves the top of the screen is still in the game. Its position keeps going
negative, and it keeps using memory and processing time. This step removes each bullet once its
bottom edge reaches the top of the screen.

## Running this step

From the `alien-invasion` folder, run:

```pwsh
python build_stage.py ch12 16 --run
```

## The code

`alien_invasion.py` changes only where shown below. `--snip--` marks code that stays the same.

```python
class AlienInvasion:
    --snip--

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

            self._update_screen()
            self.clock.tick(60)
    --snip--
```

What changed:

- `run_game()` loops over a copy of the bullet group after the bullets have moved.
- Any bullet whose `rect.bottom` is 0 or less has left the top of the screen, so it's removed.
- The rest of the file is unchanged.

## Walkthrough

**Why check `bottom`.** The top of the screen is at y = 0. A bullet is gone once its bottom edge
has reached that line, which is when `rect.bottom` is 0 or less.

**Why loop over a copy.** Python doesn't allow a list or group to change length while a loop is
using it. `copy()` gives the loop its own list, so the real group can be changed inside the loop.

**Where this runs.** The check comes after the bullets move, and before the screen is drawn. A
bullet that has just left the screen is removed before it can be drawn again.

**Why it matters.** Without this step, the bullets still exist, and the game keeps moving them.
Many bullets would slow the game down.

## Output

Fire several bullets. Each one disappears at the top of the screen, and the game keeps running
at the same speed.

The window looks the same as in the last step, so there's no separate screenshot. The bullets
from the last step's screenshot are the same here.

## Changed files

- `alien_invasion.py`: removes bullets once they have left the top of the screen

---
