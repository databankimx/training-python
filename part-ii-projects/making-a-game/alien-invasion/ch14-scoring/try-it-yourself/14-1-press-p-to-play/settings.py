"""
Chapter 14, exercise 14-1: Press P to Play.

This module stores all the settings for the game.
"""


class Settings: #pylint: disable=too-few-public-methods
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Alien settings
        self.alien_speed = 0.25
        self.fleet_drop_speed = 10
        # 1 = right | -1 = left
        self.fleet_direction = 1

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (180, 0, 0)
        self.bullets_allowed = 3
