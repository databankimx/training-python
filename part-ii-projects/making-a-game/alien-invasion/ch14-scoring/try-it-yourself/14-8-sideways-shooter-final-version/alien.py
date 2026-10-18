"""
Chapter 14, exercise 14-8: Sideways Shooter, Final Version.

This module defines the Alien class. Each alien is rotated to face the rocket, and it moves toward the
rocket, bouncing up and down off the top and bottom edges of the screen.
"""

import os
from random import choice, randint

import pygame
from pygame.sprite import Sprite


class Alien(Sprite): #pylint: disable=too-few-public-methods
    """A class to represent one alien moving toward the rocket."""

    def __init__(self, ss_game) -> None:
        """Create an alien just off the right edge, at a random height."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load the alien image from the images folder next to this file, and rotate it 90 degrees.
        folder = os.path.dirname(os.path.abspath(__file__))
        image = pygame.image.load(os.path.join(folder, "images", "alien.bmp"))
        self.image = pygame.transform.rotate(image, 90)
        self.rect = self.image.get_rect()

        # Start the alien just off the right edge, at a random height.
        self.rect.left = self.screen_rect.right
        self.rect.y = randint(0, self.screen_rect.height - self.rect.height)

        # Store decimal positions, so the speeds can be fractions.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # 1 means moving down, and -1 means moving up. The alien starts in a random direction.
        self.vertical_direction = choice([1, -1])

    def update(self) -> None:
        """Move the alien left, and bounce it off the top and bottom edges of the screen."""
        self.x -= self.settings.alien_speed
        self.y += self.settings.alien_vertical_speed * self.vertical_direction
        self.rect.x = int(self.x)
        self.rect.y = int(self.y)

        # Bounce off the top edge, and move down from now on.
        if self.rect.top <= 0:
            self.vertical_direction = 1
            self.rect.top = 0
        # Bounce off the bottom edge, and move up from now on.
        elif self.rect.bottom >= self.screen_rect.bottom:
            self.vertical_direction = -1
            self.rect.bottom = self.screen_rect.bottom

        # Keep the decimal position in step with the rect after any bounce.
        self.y = float(self.rect.y)

    def has_left_screen(self) -> bool:
        """Return True once the alien has moved past the left edge of the screen."""
        return self.rect.right <= 0

    def blitme(self) -> None:
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)
