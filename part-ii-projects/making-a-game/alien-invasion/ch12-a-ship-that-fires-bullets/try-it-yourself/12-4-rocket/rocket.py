"""A class to manage the rocket, which the player can move in all four directions."""

import os

import pygame


class Rocket: #pylint: disable=too-few-public-methods
    """A class to manage the rocket."""

    def __init__(self, game) -> None:
        """Initialize the rocket and set its starting position."""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load the image from the images folder next to this file.
        folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
        self.image = pygame.image.load(os.path.join(folder, "rocket.bmp"))
        self.rect = self.image.get_rect()

        # Start the rocket at the center of the screen.
        self.rect.center = self.screen_rect.center

        # Store decimal values for the rocket's position.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self) -> None:
        """Move the rocket, and keep it inside the edges of the screen."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.rocket_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.rocket_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.rocket_speed

        # Update the rect from the decimal position.
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self) -> None:
        """Draw the rocket at its current location."""
        self.screen.blit(self.image, self.rect)
