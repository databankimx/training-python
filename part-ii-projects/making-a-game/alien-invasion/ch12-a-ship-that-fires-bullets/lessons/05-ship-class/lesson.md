---
files:
  - ship.py: full
---

# Creating the Ship Class

## What this step does

The player's ship gets its own module, `ship.py`, with a class called `Ship`. The class loads
the ship image, works out where the ship belongs, and draws it when asked.

This step only adds the class. The ship doesn't appear on screen until the next step, which
creates a `Ship` in the main program.

## The code

`ship.py` is new, so it's shown in full:

```python
"""
Alien Invasion Game - Chapter 12: A Ship That Fires Bullets

This module contains the Ship class, which manages the player's ship.
"""

import os

import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image from the images folder next to this file.
        folder = os.path.dirname(os.path.abspath(__file__))
        self.image = pygame.image.load(os.path.join(folder, "images", "ship.bmp"))
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self) -> None:
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
```

What changed:

- `ship.py` is new. It defines the `Ship` class.
- No other file changes in this step.

## Walkthrough

**The image.** `pygame.image.load()` reads the file and returns a surface, which holds the
picture. We store it in `self.image`.

**Finding the image.** The path is built from this file's own location, not from the folder the
game was started in. `__file__` is the path of `ship.py`, and `os.path.abspath()` makes it
complete. That way `images/ship.bmp` is found however the game is started.

**Rects.** Pygame treats each game element as a rectangle, called a `rect`, even when the
element isn't a rectangle. A rect has a position and a size, and it makes collision checks
simple later on. `self.image.get_rect()` gives the ship's rect, the same size as the picture.

**Positioning the ship.** `self.screen.get_rect()` gives the rect of the whole window. Setting
`self.rect.midbottom` to the window's `midbottom` puts the ship at the bottom center of the
screen. Rects have other position attributes too, such as `top`, `left`, `center`, and
`midtop`, which you'll use as the game grows.

**Drawing.** `blitme()` draws the image onto the screen at the position of `self.rect`. It is
called from the main program, once for each pass through the loop.

**The `__init__()` arguments.** `Ship` receives the game object, `ai_game`, so it can reach the
screen. This means the ship doesn't need the screen passed to it separately.

## Running this step

From the `alien-invasion` folder, run:

```pwsh
python build_stage.py ch12 5 --run
```

## Output

No output yet. The ship appears in the next step.

## Changed files

- `ship.py` (new)
- `images/ship.bmp` (added to this step's `images` folder, from the book's resources)
