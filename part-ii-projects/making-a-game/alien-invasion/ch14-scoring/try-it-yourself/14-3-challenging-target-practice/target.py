"""
Chapter 14, exercise 14-3: Challenging Target Practice.

This module defines the Target class, a rectangle on the right edge of the screen that moves up and down,
bouncing off the top and bottom edges. Its speed is set in the settings, so it can change during the game.
"""

import pygame
from pygame.sprite import Sprite


class Target(Sprite): #pylint: disable=too-few-public-methods
    """A class to manage the moving target."""

    def __init__(self, tp_game) -> None:
        """Create the target at the top of the right edge of the screen."""
        super().__init__()
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, self.settings.target_width, self.settings.target_height)
        self.reset()

    def reset(self) -> None:
        """Put the target back at the top of the right edge, moving down."""
        self.rect.right = self.screen_rect.right - 20
        self.rect.top = 0
        self.y = float(self.rect.y)
        self.vertical_direction = 1

    def update(self) -> None:
        """Move the target up or down at the current target speed, and bounce it off the edges."""
        self.y += self.settings.target_speed * self.vertical_direction
        self.rect.y = int(self.y)

        if self.rect.top <= 0:
            self.vertical_direction = 1
            self.rect.top = 0
        elif self.rect.bottom >= self.screen_rect.bottom:
            self.vertical_direction = -1
            self.rect.bottom = self.screen_rect.bottom

        self.y = float(self.rect.y)

    def blitme(self) -> None:
        """Draw the target to the screen."""
        pygame.draw.rect(self.screen, self.settings.target_color, self.rect)
