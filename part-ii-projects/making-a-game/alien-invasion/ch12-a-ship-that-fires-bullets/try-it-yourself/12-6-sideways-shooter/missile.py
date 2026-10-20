"""A class to manage a missile fired from the rocket across the screen."""

import pygame
from pygame.sprite import Sprite


class Missile(Sprite): #pylint: disable=too-few-public-methods
    """A class to manage missiles fired from the rocket."""

    def __init__(self, game) -> None:
        """Create a missile at the rocket's current position."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.missile_color

        # Create a missile rect at (0, 0), then set its correct position.
        self.rect = pygame.Rect(0, 0, self.settings.missile_width, self.settings.missile_height)
        self.rect.midleft = game.rocket.rect.midright

        # Store the missile's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self, *args, **kwargs) -> None:
        """Move the missile to the right."""
        self.x += self.settings.missile_speed
        self.rect.x = self.x

    def draw_missile(self) -> None:
        """Draw the missile to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
