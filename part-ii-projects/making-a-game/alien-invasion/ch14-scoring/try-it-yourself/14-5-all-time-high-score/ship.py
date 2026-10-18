"""
Chapter 14, exercise 14-5: All-Time High Score.

This module defines the Ship class, which manages the player's ship.
"""

import os

import pygame
from pygame.sprite import Sprite


class Ship(Sprite): #pylint: disable=too-few-public-methods
    """A class to manage the ship."""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.settings = ai_game.settings
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image from the images folder next to this file.
        root_dir = os.path.dirname(__file__)
        file_name = "ship.bmp"
        file_path = os.path.join(root_dir, "images", file_name)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def update(self, *args, **kwargs) -> None:
        """Update the ship's position based on movement flags."""
        # Update the decimal x value, so fractional speeds are kept.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed

        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect from the decimal position.
        self.rect.x = self.x

    def blitme(self) -> None:
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self) -> None:
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
