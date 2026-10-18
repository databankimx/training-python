"""
Chapter 13, exercise 13-6: Game Over.

This module stores the settings for the sideways shooter.
"""


class Settings: #pylint: disable=too-few-public-methods
    """A class to store the settings for the sideways shooter."""

    def __init__(self) -> None:
        """Initialize the game settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        self.text_color = (30, 30, 30)

        # Rocket settings
        self.rocket_speed = 2.5
        # The game ends when an alien hits the rocket this many times.
        self.rocket_limit = 3

        # Missile settings
        self.missile_speed = 3.0
        self.missile_width = 15
        self.missile_height = 3
        self.missile_color = (0, 143, 17)
        self.missiles_allowed = 5

        # Alien settings
        self.alien_speed = 1.0
        self.alien_vertical_speed = 1.0
        self.alien_spawn_interval = 5000  # milliseconds between new aliens
