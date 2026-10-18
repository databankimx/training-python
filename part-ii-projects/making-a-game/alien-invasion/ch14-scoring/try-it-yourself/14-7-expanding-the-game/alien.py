"""
Chapter 14, exercise 14-7: Expanding the Game.

This module defines the Alien class. Each alien is one color, and loops that color's
animation. It moves left and right with the fleet, and drops when the fleet reaches an edge.
"""

import pygame
from pygame.sprite import Sprite

from animation import Animation


class Alien(Sprite): #pylint: disable=too-few-public-methods
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game, colour: str) -> None:
        """Initialize the alien, its animation, and its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.colour = colour

        # The alien's animation loops, and the rect takes the size of its frames.
        self.animation = Animation(f"{colour}-anim")
        self.rect = self.animation.frames[0].get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)

    def update(self, *args: object, **kwargs: object) -> None:
        """Move the alien right or left, depending on the fleet's direction."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self) -> bool:
        """Return True if the alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return self.rect.right >= screen_rect.right or self.rect.left <= 0

    def blitme(self) -> None:
        """Draw the alien's frame that's due to be shown now."""
        self.screen.blit(self.animation.frame_at(pygame.time.get_ticks()), self.rect)
