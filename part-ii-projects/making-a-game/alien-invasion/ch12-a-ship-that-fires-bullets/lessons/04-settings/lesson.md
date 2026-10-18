---
files:
  - settings.py: full
  - alien_invasion.py: snipped
---

# Creating a Settings Class

## What this step does

Each time the game gets a new feature, it usually needs new settings. Rather than scatter
values such as the screen size and colors through the code, this step moves them into one
class, `Settings`, in its own module, `settings.py`.

The main program creates one `Settings` object and reads its values through `self.settings`.
To change how the game looks or behaves, you edit `settings.py`.

The window looks the same as in the last step. This step changes where the values live, not
what they do.

## The code

`settings.py` is new, so it's shown in full:

```python
"""
Alien Invasion Game - Chapter 12: A Ship That Fires Bullets

This module stores all the settings for the game.
"""


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
```

`alien_invasion.py` changes only where shown below. `--snip--` marks code that stays the same.

```python
import sys
import pygame

from settings import Settings


class AlienInvasion:
    --snip--

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self) -> None:
        --snip--
            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)
            --snip--
```

What changed:

- `settings.py` is new. It holds the screen size and the background color.
- `alien_invasion.py` imports `Settings` with `from settings import Settings`.
- `__init__()` creates `self.settings = Settings()` after `pygame.init()`, and before the
  screen is created.
- `set_mode()` takes its size from `self.settings.screen_width` and `self.settings.screen_height`.
- `run_game()` fills the screen with `self.settings.bg_color`. The `self.bg_color` attribute is
  no longer used.

## Walkthrough

**`settings.py`.** The file has a module docstring, then one class with an `__init__()` method
that sets the values. Each value is an attribute, so the rest of the game reads it as
`self.settings.<name>`.

**`from settings import Settings`.** This import line brings the class into the main file.
Python looks for `settings.py` in the same folder.

**Creating the object.** `self.settings = Settings()` runs in `__init__()`. It comes after
`pygame.init()`, and before the screen is created, because the screen size is one of the
settings.

**The screen size.** The `set_mode()` call now reads its size from the settings, so changing
`screen_width` or `screen_height` changes the window.

**The background color.** `self.settings.bg_color` replaces the old `self.bg_color`. The
color now lives in `settings.py`, so it's changed in one place.

## Running this step

From the `alien-invasion` folder, run:

```pwsh
python build_stage.py ch12 4 --run
```

## Output

The window looks the same as in the last step, because only the location of the values has
changed.

![Light gray Pygame window](../03-background-color/lesson-images/gray-background.png)

The screenshot from the previous step is reused here.
