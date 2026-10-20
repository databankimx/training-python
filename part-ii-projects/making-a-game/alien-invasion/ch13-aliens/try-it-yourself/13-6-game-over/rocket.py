"""
Chapter 13, exercise 13-6: Game Over.

This module defines the Rocket class, which moves up and down the left side of the screen.
"""

import os

import pygame


class Rocket: #pylint: disable=too-few-public-methods
    """A class to manage the rocket."""

    def __init__(self, ss_game) -> None:
        """Initialize the rocket and set its starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()

        # Load the rocket image from the images folder next to this file.
        root_dir = os.path.dirname(os.path.abspath(__file__))
        file_name = "rocket.bmp"
        file_path = os.path.join(root_dir, "images", file_name)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()

        # Start the rocket at the middle of the left edge.
        self.rect.midleft = self.screen_rect.midleft

        # Store a decimal value for the rocket's vertical position.
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_up = False
        self.moving_down = False

    def update(self) -> None:
        """Move the rocket up or down, and keep it inside the screen."""
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed

        # Update the rect from the decimal position.
        self.rect.y = self.y

    def blitme(self) -> None:
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
