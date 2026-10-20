# Refactoring the Key Handling, and Pressing Q to Quit

## What this step does

Two changes to how the game reads the keyboard. First, `_check_events()` is split into two
helper methods, one for key presses and one for key releases. Second, pressing Q now ends the
game, which saves clicking the window's close button while testing.

## Running this step

From the `alien-invasion` folder, run:

```pwsh
python build_stage.py ch12 13 --run
```

Press Q to close the game.

## The code

`alien_invasion.py` changes only where shown below. `--snip--` marks code that stays the same.

```python
class AlienInvasion:
    --snip--

    def _check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    --snip--
```

What changed:

- `_check_events()` passes each key press to `_check_keydown_events()`, and each key release to
  `_check_keyup_events()`. Its own code is shorter now.
- The two new helper methods take the `event` as a parameter, and hold the key checks that were
  in `_check_events()`.
- `_check_keydown_events()` has a new `elif` block. It calls `sys.exit()` when Q is pressed.
- `ship.py` is unchanged.

## Walkthrough

**Why split the method.** `_check_events()` grows with every new key. Keeping key presses and
key releases in their own methods keeps each one easy to read.

**Helper methods.** Both helpers are used only inside the class, so they start with an underscore.
Each takes `self` and the `event`, because it needs the ship and the event's key.

**Quitting with Q.** `pygame.K_q` is the Q key. `sys.exit()` ends the program, the same way the
window's close button does.

## Output

Run the game. Hold the arrow keys to move the ship as before, then press Q to close the window.

The game looks the same as in the last step, so there's no screenshot for this step.

## Changed files

- `alien_invasion.py`: splits key handling into `_check_keydown_events()` and
  `_check_keyup_events()`, and adds Q to quit
