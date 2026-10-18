"""
Chapter 14, exercise 14-8: Sideways Shooter, Final Version.

This module defines the AlienBullet class. An alien bullet is a zig-zag line that travels left, from the alien
toward the rocket.
"""

import pygame
from pygame.sprite import Sprite


class AlienBullet(Sprite): #pylint: disable=too-few-public-methods
    """A class to manage the zig-zag bullets fired by the aliens."""

    def __init__(self, ss_game, source) -> None:
        """Create a bullet at the front of the alien that fired it."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings

        # The alien that fired this bullet. The alien can't fire again while the bullet is on screen.
        self.source = source
        self.color = self.settings.alien_bullet_color

        # The rect is the size of the zig-zag. The zig-zag is drawn inside it.
        self.rect = pygame.Rect(0, 0, self.settings.alien_bullet_width,
                                self.settings.alien_bullet_height)
        self.rect.midright = source.rect.midleft

        # Store the bullet's position as a decimal value.
        self.x = float(self.rect.x)

    def update(self) -> None:
        """Move the bullet to the left."""
        self.x -= self.settings.alien_bullet_speed
        self.rect.x = self.x

    def has_left_screen(self) -> bool:
        """Return True once the bullet has moved past the left edge of the screen."""
        return self.rect.right <= 0

    def draw_bullet(self) -> None:
        """Draw the zig-zag bullet to the screen."""
        width = self.rect.width
        height = self.rect.height
        step = width // 4
        # Points alternate between the top and bottom of the rect, to make the zig-zag.
        points = [
            (self.rect.left + i * step, self.rect.top if i % 2 == 0 else self.rect.bottom)
            for i in range(5)
        ]
        pygame.draw.lines(self.screen, self.color, False, points, max(2, height // 6))
