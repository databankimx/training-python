"""
Chapter 12, exercise 13-3: Raindrops.

This module defines the Raindrop class, one drop in the rain shower.
"""

import os
from random import randint

import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite): #pylint: disable=too-few-public-methods
    """A class to represent a raindrop in the rain shower."""

    def __init__(self, rs_game, at_top: bool = False) -> None:
        """Initialize a raindrop, and set its size and starting position."""
        super().__init__()
        self.screen = rs_game.screen
        self.settings = rs_game.settings

        self.size = randint(0, 3)
        self.speed = randint(1, 6)
        root_dir = os.path.dirname(__file__)
        file_name = None
        if self.size == 0:
            file_name = self.settings.rain_img_lg
        elif self.size == 1:
            file_name = self.settings.rain_img_med
        else:
            file_name = self.settings.rain_img_sm
        file_path = os.path.join(root_dir, "images", file_name)
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect()

        self.x = float(randint(0, self.screen.get_rect().width - self.rect.width))
        self.y = float(randint(0, self.screen.get_rect().height - self.rect.height))
        if at_top:
            self.y = 0

        self.rect.x = self.x
        self.rect.y = self.y

    def update(self, *args, **kwargs) -> None:
        """Move the raindrop down the screen."""
        self.y += self.speed
        self.rect.y = self.y
