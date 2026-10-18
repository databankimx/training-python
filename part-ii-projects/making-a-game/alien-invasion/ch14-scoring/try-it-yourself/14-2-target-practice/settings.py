"""
Chapter 14, exercise 14-2: Target Practice.

This module stores all the settings for the target practice game.
"""


class Settings: #pylint: disable=too-few-public-methods
    """A class to store all settings for Target Practice."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_width = 20
        self.ship_height = 60
        self.ship_color = (0, 0, 160)
        self.ship_speed = 2.0

        # Bullet settings
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullet_speed = 4.0
        self.bullets_allowed = 5

        # Target settings
        self.target_width = 20
        self.target_height = 80
        self.target_color = (0, 160, 0)
        self.target_speed = 1.5

        # The game ends when the player misses this many times.
        self.misses_allowed = 3
