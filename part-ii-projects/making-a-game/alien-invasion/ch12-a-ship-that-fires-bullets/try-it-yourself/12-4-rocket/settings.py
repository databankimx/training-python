"""
Alien Invasion Game - Try It Yourself 12-4: Rocket

This module contains the Settings class, which manages the settings for the rocket game window.
"""

class Settings: #pylint: disable=too-few-public-methods
    """A class to store the settings for the rocket game."""

    def __init__(self) -> None:
        """Initialize the settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)

        # Rocket settings
        self.rocket_speed = 1.0
