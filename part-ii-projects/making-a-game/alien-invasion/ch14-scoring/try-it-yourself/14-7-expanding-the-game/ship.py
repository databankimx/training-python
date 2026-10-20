"""
Chapter 14, exercise 14-7: Expanding the Game.

This module defines the Ship class. The ship is drawn from the ship-anim frames.
Frame 0 is the ship at rest, and frames 1 to 3 play each time the ship fires.
"""

import pygame
from pygame.sprite import Sprite

from animation import FRAME_DELAY, load_frames

#pylint: disable=line-too-long

class Ship(Sprite): #pylint: disable=too-few-public-methods, too-many-instance-attributes
    """A class to manage the ship."""

    def __init__(self, ai_game) -> None:
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # frame 0 is the resting ship. Frames 1 onward are the shooting animation.
        self.frames = load_frames("ship-anim")
        self.rect = self.frames[0].get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horizontal position.
        self.x = float(self.rect.x)

        # When the ship last fired. None means it hasn't fired yet.
        self.shot_time = None

        # Movement flags.
        self.moving_right = False
        self.moving_left = False

    def fire(self) -> None:
        """Start the shooting animation."""
        self.shot_time = pygame.time.get_ticks()

    def _current_frame(self) -> pygame.Surface:
        """Return the frame to show: the shooting frames while firing, otherwise the resting frame."""
        if self.shot_time is not None:
            elapsed = pygame.time.get_ticks() - self.shot_time
            shooting_frames = len(self.frames) - 1
            if elapsed < shooting_frames * FRAME_DELAY:
                return self.frames[1 + elapsed // FRAME_DELAY]
        return self.frames[0]

    @property
    def image(self) -> pygame.Surface:
        """The frame to draw now. Sprite groups read this when they draw the ship."""
        return self._current_frame()

    def update(self, *args: object, **kwargs: object) -> None:
        """Update the ship's position based on movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update the rect from the decimal position.
        self.rect.x = self.x

    def center_ship(self) -> None:
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def blitme(self) -> None:
        """Draw the ship at its current location, showing the right frame."""
        self.screen.blit(self._current_frame(), self.rect)
