"""
Chapter 14, exercise 14-4: Difficulty Levels.

This module stores all the settings for the game, including the speeds for each difficulty level.
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
        self.fleet_drop_speed = 10

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (180, 0, 0)
        self.bullets_allowed = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # Easy = 0.5 | Medium = 1.0 | Hard = 1.5
        self.difficulty_level = 1.0
        self.difficulty_modifier = 0.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self, difficulty_level: float = 1.0) -> None:
        """Set the settings that change during the game, for the chosen difficulty level."""
        self.difficulty_level = difficulty_level

        self.ship_speed = 1.0
        if self.difficulty_level < 1:
            self.ship_speed /= self.difficulty_level
        self.bullet_speed = 3.0 / self.difficulty_level
        self.alien_speed = 0.5 * self.difficulty_level

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self) -> None:
        """Make the game faster each time a new fleet is created."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
