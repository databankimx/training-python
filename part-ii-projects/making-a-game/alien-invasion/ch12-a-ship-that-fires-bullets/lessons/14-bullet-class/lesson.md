# Creating the Bullet Class

## What this step does

Bullets get their own module, `bullet.py`, with a class called `Bullet`. A bullet is a small
rectangle that appears at the top of the ship and travels straight up the screen.

The bullet's settings, such as its size, color and speed, are stored in `settings.py`, the
same way the ship's settings are.

This step only adds the class and its settings. Nothing fires a bullet yet. The next step
connects the bullet to the space bar.

## Running this step

From the `alien-invasion` folder, run:

```pwsh
python build_stage.py ch12 14 --run
```

The window looks the same as in the last step.

## The code

`settings.py` changes only where shown below. `--snip--` marks code that stays the same.

```python
class Settings: #pylint: disable=too-few-public-methods
    --snip--

    def __init__(self) -> None:
        """Initialize the game's settings."""
        --snip--

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
```

`bullet.py` is new, so it's shown in full:

```python
"""
Alien Invasion Game - Chapter 12: A Ship That Fires Bullets

This module contains the Bullet class, which manages bullets fired from the ship.
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, ai_game) -> None:
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a float.
        self.y = float(self.rect.y)

    def update(self) -> None:
        """Move the bullet up the screen."""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update the rect position.
        self.rect.y = self.y

    def draw_bullet(self) -> None:
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
```

What changed:

- `settings.py` adds the bullet settings: speed, width, height and color.
- `bullet.py` is new. It defines the `Bullet` class.
- `alien_invasion.py` is unchanged.

## Walkthrough

**The sprite base class.** `Bullet` inherits from `Sprite`. Sprites can be kept in groups, and a
group can update or draw all its members in one call. The next step uses that.

**The rect.** The bullet has no image, so its rect is built from its width and height. It starts
at (0, 0), and then `midtop` is set to the ship's `midtop`. That makes the bullet appear at the
top middle of the ship.

**The float position.** `self.y` holds the exact height. Subtracting a speed of 2.0 each frame
moves the bullet by fractions of a pixel, which `rect.y` can't store. The rect is updated from
`self.y`, the same as the ship.

**Drawing.** `pygame.draw.rect()` fills the rectangle with the bullet's color.

## Output

No change yet. The next step fires bullets.

## Changed files

- `settings.py`: adds the bullet settings
- `bullet.py` (new): the `Bullet` class

---
