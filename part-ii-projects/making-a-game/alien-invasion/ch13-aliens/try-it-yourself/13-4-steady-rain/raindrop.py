"""
Chapter 12, exercise 13-4: Steady Rain.

This module defines the Raindrop class, one drop in the steady rain.
"""

import os
from random import randint, uniform

import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite): #pylint: disable=too-few-public-methods
    """A class to represent a raindrop in the steady rain."""

    def __init__(self, rs_game, new_drop: bool = False) -> None:
        """Initialize a raindrop, and set its size and starting position."""
        super().__init__()
        self.screen = rs_game.screen
        self.settings = rs_game.settings

        self.size = randint(0, 3)
        self.speed = uniform(2.100, 5.001)
        root_dir = os.path.dirname(__file__)
        file_name = None
        if self.size == 0:
            file_name = self.settings.rain_img_lg
        elif self.size == 1:
            file_name = self.settings.rain_img_med
        else:
            file_name = self.settings.rain_img_sm
        file_path = os.path.join(root_dir, "images", file_name)
        image = pygame.image.load(file_path)
        rotation = 0
        if self.settings.wind_speed != 0:
            rotation = self.settings.wind_speed // 1 * 15
        self.image = pygame.transform.rotate(image, rotation)
        self.rect = self.image.get_rect()

        self.x = float(randint(0, self.screen.get_rect().width - self.rect.width))
        self.y = float(randint(0, self.screen.get_rect().height - self.rect.height))

        if new_drop:
            # Start the drop just outside the screen: on the side the wind blows from, or above it.
            screen_rect = self.screen.get_rect()
            if randint(0, 2) == 0:
                if self.settings.wind_speed < 0:
                    self.x = float(screen_rect.width)
                else:
                    self.x = float(-self.rect.width)
            else:
                self.y = float(-self.rect.height)

        self.rect.x = self.x
        self.rect.y = self.y

    def update(self) -> None:
        """Move the raindrop down, and sideways with the wind."""
        self.y += self.speed
        self.rect.y = self.y
        self.x += self.settings.wind_speed
        self.rect.x = self.x

    def check_edge(self) -> bool:
        """Return True if the raindrop has passed the edge of the screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.top >= screen_rect.bottom or self.rect.right <= 0
                or self.rect.left >= screen_rect.right)
