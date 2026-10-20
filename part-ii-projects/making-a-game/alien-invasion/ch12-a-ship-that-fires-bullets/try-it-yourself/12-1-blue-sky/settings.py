"""
Alien Invasion Game - Try It Yourself 12-1: Blue Sky

This module contains the Settings class, which manages the settings for the blue sky window.
"""

class Settings: #pylint: disable=too-few-public-methods
    """A class to store the settings for the blue sky window."""

    def __init__(self) -> None:
        """Initialize the settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
