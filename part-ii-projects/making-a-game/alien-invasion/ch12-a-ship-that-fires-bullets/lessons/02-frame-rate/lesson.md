---
files:
  - alien_invasion.py: snipped
---

# Controlling the Frame Rate

## What this step does

Games should run at the same speed on every computer. A faster machine would otherwise run
the loop faster, so the game would move faster too. Pygame's clock fixes this.

The clock is created once in `__init__()`. At the end of each pass through the main loop,
`self.clock.tick(60)` pauses just long enough that the loop runs about 60 times per second.

## The code

The code from the last step is unchanged except where shown below. `--snip--` marks code that
stays the same. The full file is in this step's folder, as `alien_invasion.py`.

```python
class AlienInvasion:
    --snip--

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        --snip--

    def run_game(self) -> None:
        --snip--
            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)
```

What changed:

- `__init__()` creates the clock with `pygame.time.Clock()`, and keeps it in `self.clock`.
- `run_game()` calls `self.clock.tick(60)` at the end of each pass through the loop.
- The module docstring now also mentions frame rate control.

## Walkthrough

**The clock line in `__init__()`.** `pygame.time.Clock()` creates a clock object. We make it
once, and keep it in `self.clock` so the loop can use it.

**`self.clock.tick(60)`.** This is the last line of the loop. Each call pauses the loop for
whatever time is left in the current frame, so the loop runs no more than 60 times per
second. If the loop is already slow, the call returns straight away.

**Why 60?** It's the target frame rate. A higher number makes the motion smoother on a fast
machine, and a lower number makes the game lighter on a slow one.

**Where the tick goes.** Call `tick()` once per pass through the loop, after the screen has
been made visible. That way, each frame's timing covers all the work done in that frame.

## Running this step

From the `alien-invasion` folder, run:

```pwsh
python build_stage.py ch12 2 --run
```

## Output

The window looks the same as in the last step. The difference is that the loop now runs at a
steady rate, which you can't see here, but which matters once the game has moving parts.

![Empty Pygame window at a steady frame rate](../01-window-and-events/lesson-images/empty-game-window.png)

The screenshot from the first step is reused here, since the window looks the same.
