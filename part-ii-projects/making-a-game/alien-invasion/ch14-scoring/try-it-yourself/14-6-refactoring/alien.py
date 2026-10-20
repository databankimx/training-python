"""
Chapter 14, exercise 14-6: Refactoring.

This module defines the Alien class, one alien in the fleet.
"""

import os

import pygame
from pygame.sprite import Sprite


class Alien(Sprite): #pylint: disable=too-few-public-methods
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game) -> None:
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image from the images folder next to this file.
        root_dir = os.path.dirname(__file__)
        file_name = "alien.bmp"
        file_path = os.path.join(root_dir, "images", file_name)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self, *args, **kwargs) -> None:
        """Move the alien right or left, depending on the fleet's direction."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self) -> bool:
        """Return True if the alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False
