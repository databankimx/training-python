"""A class to manage the rocket, which moves up and down the left side of the screen."""

import os

import pygame


class Rocket: #pylint: disable=too-few-public-methods, too-many-instance-attributes
    """A class to manage the rocket."""

    def __init__(self, game) -> None:
        """Initialize the rocket and place it on the left side of the screen."""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load the image from the images folder next to this file.
        folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")
        self.image = pygame.image.load(os.path.join(folder, "rocket.bmp"))
        # Turn the rocket to face right, so it fires across the screen.
        self.image = pygame.transform.rotate(self.image, -90)
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
