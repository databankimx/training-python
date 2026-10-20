"""A class to draw the game character at the center of the screen."""

import os

import pygame


class Character: #pylint: disable=too-few-public-methods
    """A class to manage the game character."""

    def __init__(self, game) -> None:
        """Load the character's image and place it at the center of the screen."""
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Load the image from the images folder next to this file.
        folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
        self.image = pygame.image.load(os.path.join(folder, "character.bmp"))
        self.rect = self.image.get_rect()

        # Start the character at the center of the screen.
        self.rect.center = self.screen_rect.center

    def blitme(self) -> None:
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
