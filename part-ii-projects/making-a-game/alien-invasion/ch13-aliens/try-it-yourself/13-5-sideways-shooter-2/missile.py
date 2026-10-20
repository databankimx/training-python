"""
Chapter 13, exercise 13-5: Sideways Shooter, Part 2.

This module defines the Missile class, which travels across the screen from the rocket.
"""

import pygame
from pygame.sprite import Sprite


class Missile(Sprite): #pylint: disable=too-few-public-methods
    """A class to manage missiles fired from the rocket."""

    def __init__(self, ss_game) -> None:
        """Create a missile at the rocket's current position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.missile_color

        # Create a missile rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.missile_width, self.settings.missile_height)
        self.rect.midleft = ss_game.rocket.rect.midright

        # Store the missile's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self, *args, **kwargs) -> None:
        """Move the missile across the screen."""
        self.x += self.settings.missile_speed
        self.rect.x = self.x

    def draw_missile(self) -> None:
        """Draw the missile to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
