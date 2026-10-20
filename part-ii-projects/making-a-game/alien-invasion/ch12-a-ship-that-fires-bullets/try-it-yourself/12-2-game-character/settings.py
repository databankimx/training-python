"""
Alien Invasion Game - Try It Yourself 12-2: Game Character

This module contains the Settings class, which manages the settings for the game character window.
"""

class Settings: #pylint: disable=too-few-public-methods
    """A class to store the settings for the game character window."""

    def __init__(self) -> None:
        """Initialize the settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800

        # Match this to the background color of the character's image.
        self.bg_color = (135, 206, 235)
