---
files:
  - alien_invasion.py: snipped
---

# Refactoring: _check_events() and _update_screen()

## What this step does

`run_game()` has started to grow. This step moves its work into two helper methods, so the
main loop reads as three short steps: check events, update the screen, and tick the clock.

The window looks the same as in the last step. The change is in how the code is organized.

## The code

The code from the last step is unchanged except where shown below. `--snip--` marks code that
stays the same. The full file is in this step's folder, as `alien_invasion.py`.

```python
class AlienInvasion:
    --snip--

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self) -> None:
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        pygame.display.flip()
```

What changed:

- `_check_events()` is a new method. It holds the event loop that used to be in `run_game()`.
- `_update_screen()` is a new method. It fills the background, draws the ship, and flips the
  screen, all of which used to be in `run_game()`.
- `run_game()` now calls the two helpers, then ticks the clock.

## Walkthrough

**Helper methods.** A helper method does work inside a class, and code outside the class
doesn't need to call it. A single leading underscore in the name marks it as a helper.

**`_check_events()`.** Separating the event loop lets you handle events on their own. Later,
keypresses for moving the ship will go here.

**`_update_screen()`.** Drawing the screen is in one place. When the game gains bullets and
aliens, their drawing will go here too.

**Calling a method.** `self._check_events()` uses dot notation with `self`, the same way the
main program calls `self.ship.blitme()`.

**The main loop.** Read top to bottom, `run_game()` now says what happens on each pass: check
events, update the screen, and tick the clock.

## Running this step

From the `alien-invasion` folder, run:

```pwsh
python build_stage.py ch12 7 --run
```

## Output

The window and the ship look the same as in the last step.

![Gray Pygame window with the ship at the bottom center](../06-drawing-the-ship/lesson-images/ship-bottom-center.png)

The screenshot from the previous step is reused here.

## Changed files

- `alien_invasion.py`: `run_game()` calls two new helper methods, `_check_events()` and
  `_update_screen()`

---
