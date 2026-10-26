# Building the Alien Fleet

## What this step does

The fleet fills the upper part of the screen. The game places aliens in rows, from left to right,
until no room is left for another alien. Then it starts a new row below, and keeps going until the
fleet reaches the bottom third of the screen.

The rows are made with nested loops, and each alien is placed by a helper method, `_create_alien()`.

## Running this step

From the `alien-invasion` folder, run:

```pwsh
python build_stage.py ch13 2 --run
```

Press Q to quit.

## The code

`alien.py` is unchanged from the last step. `alien_invasion.py` changes only where shown below.
`--snip--` marks code that stays the same.

```python
class AlienInvasion:
    --snip--

    def _create_fleet(self) -> None:
        """Create the fleet of aliens."""
        # Create an alien and keep adding aliens until there's no room left.
        # Spacing between aliens is one alien width and one alien height.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position: float, y_position: float) -> None:
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    --snip--
```

What changed:

- `_create_fleet()` now has two nested loops. The inner loop fills one row, and the outer loop adds
  rows.
- `_create_alien()` is a new method. It places one alien at a given x and y position.
- The rest of the file is unchanged.

## Walkthrough

**Measuring the alien.** The first alien is made only to find its size. Its width and height set
the spacing: one alien width between aliens across a row, and one alien height between rows.

**The inner loop.** `current_x` is the horizontal position of the next alien. The loop keeps going
while there's room for another alien, with a margin of two alien widths at the right edge. Each
time an alien is added, `current_x` moves two alien widths to the right: one for the alien, and one
for the space after it.

**The outer loop.** When the inner loop finishes a row, `current_x` goes back to the left edge.
`current_y` moves down two alien heights, so the next row sits below the last one. The stop
condition leaves room at the bottom for the ship.

**Indentation.** The last two lines of the outer loop belong to the outer loop, not the inner one.
They run once after each row. If the fleet looks wrong, check the indentation first.

## Output

The screen fills with rows of aliens in the upper part of the window, with the ship and bullets
below them.

![Full fleet of aliens](lesson-images/full-fleet.png)

## Changed files

- `alien_invasion.py`: builds the fleet with nested loops, and adds `_create_alien()`

---
