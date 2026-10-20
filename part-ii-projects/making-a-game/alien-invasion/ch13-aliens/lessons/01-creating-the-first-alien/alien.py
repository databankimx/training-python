"""
Alien Invasion Game - Chapter 13: Aliens!

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

        # Load the alien image from the images folder next to this file.
        folder = os.path.dirname(os.path.abspath(__file__))
        self.image = pygame.image.load(os.path.join(folder, "images", "alien.bmp"))
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)
