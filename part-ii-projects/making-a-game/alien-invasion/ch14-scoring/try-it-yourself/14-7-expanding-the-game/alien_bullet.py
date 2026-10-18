"""
Chapter 14, exercise 14-7: Expanding the Game.

This module defines the AlienBullet class. An alien bullet is a red zigzag that falls 
straight down, from the alien toward the ship at the bottom of the screen.
"""

#pylint: disable=line-too-long

import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite): #pylint: disable=too-few-public-methods
    """A class to manage the zigzag bullets fired by the aliens."""

    def __init__(self, ai_game, source) -> None:
        """Create a bullet just below the alien that fired it."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.alien_bullet_color

        # The alien that fired this bullet. The alien can't fire again while the bullet is on screen.
        self.source = source

        # The rect is the size of the zigzag, and the zigzag is drawn inside it.
        self.rect = pygame.Rect(0, 0, self.settings.alien_bullet_width,
                                self.settings.alien_bullet_height)
        self.rect.midtop = source.rect.midbottom

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

    def update(self, *args: object, **kwargs: object) -> None:
        """Move the bullet down the screen."""
        self.y += self.settings.alien_bullet_speed
        self.rect.y = self.y

    def has_passed_bottom(self) -> bool:
        """Return True once the bullet has moved past the bottom of the screen."""
        return self.rect.top >= self.settings.screen_height

    def draw_bullet(self) -> None:
        """Draw the zigzag bullet to the screen, as a line that swings from side to side as it falls."""
        step = self.rect.height // 4
        # Points alternate between the left and right of the rect, so the line zigzags downward.
        points = [
            (self.rect.left if i % 2 == 0 else self.rect.right, self.rect.top + i * step)
            for i in range(5)
        ]
        pygame.draw.lines(self.screen, self.color, False, points, max(2, self.rect.width // 2))
