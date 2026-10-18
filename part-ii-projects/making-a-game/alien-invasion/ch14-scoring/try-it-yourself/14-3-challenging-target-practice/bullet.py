"""
Chapter 14, exercise 14-3: Challenging Target Practice.

This module defines the Bullet class, which travels right from the ship toward the target.
"""

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite): #pylint: disable=too-few-public-methods
    """A class to manage bullets fired from the ship."""

    def __init__(self, tp_game) -> None:
        """Create a bullet at the ship's right edge."""
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.color = self.settings.bullet_color

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midleft = tp_game.ship.rect.midright

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move the bullet to the right."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
