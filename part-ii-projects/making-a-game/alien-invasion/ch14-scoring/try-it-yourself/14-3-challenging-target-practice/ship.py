"""
Chapter 14, exercise 14-3: Challenging Target Practice.

This module defines the Ship class, a rectangle on the left side of the screen that the player moves
up and down.
"""

import pygame


class Ship: #pylint: disable=too-few-public-methods
    """A class to manage the ship."""

    def __init__(self, tp_game) -> None:
        """Create the ship on the left side of the screen, at the vertical centre."""
        self.screen = tp_game.screen
        self.settings = tp_game.settings
        self.screen_rect = self.screen.get_rect()

        self.rect = pygame.Rect(0, 0, self.settings.ship_width, self.settings.ship_height)
        self.rect.left = 40
        self.rect.centery = self.screen_rect.centery

        # Store a decimal value for the ship's vertical position.
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_up = False
        self.moving_down = False

    def update(self) -> None:
        """Move the ship up or down, and keep it on the screen."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed

        # Update the rect from the decimal position.
        self.rect.y = self.y

    def center_ship(self) -> None:
        """Move the ship back to the vertical centre of the screen."""
        self.rect.centery = self.screen_rect.centery
        self.y = float(self.rect.y)

    def blitme(self) -> None:
        """Draw the ship at its current location."""
        pygame.draw.rect(self.screen, self.settings.ship_color, self.rect)
