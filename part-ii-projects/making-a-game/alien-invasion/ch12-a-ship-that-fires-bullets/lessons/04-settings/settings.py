"""
Alien Invasion Game - Chapter 12: A Ship That Fires Bullets

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
