"""
Chapter 14, exercise 14-8: Sideways Shooter, Final Version.

This module stores all the settings for the sideways shooter. Static settings stay the same for the whole
run, and dynamic settings change during play and are reset at the start of each game.
"""


class Settings: #pylint: disable=too-few-public-methods
    """A class to store all settings for the sideways shooter."""

    def __init__(self) -> None:
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (135, 206, 235)
        self.text_color = (30, 30, 30)

        # Rocket settings
        # The game ends when an alien hits the rocket this many times.
        self.rocket_limit = 3

        # Missile settings
        self.missile_width = 15
        self.missile_height = 3
        self.missile_color = (0, 143, 17)
        self.missiles_allowed = 5

        # Alien settings
        self.alien_spawn_interval = 5000  # milliseconds between new aliens

        # Alien bullet settings
        # Every this many milliseconds, each alien without a bullet on screen rolls the shoot chance.
        self.alien_shoot_interval = 1000
        # The chance that an alien fires on each roll.
        self.alien_shoot_chance = 0.05
        self.alien_bullet_width = 24
        self.alien_bullet_height = 6
        self.alien_bullet_color = (160, 0, 0)

        # Scoring and speed settings
        self.aliens_per_level = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self) -> None:
        """Set the settings that change during the game, back to their starting values."""
        self.rocket_speed = 2.5
        self.missile_speed = 3.0
        self.alien_speed = 1.0
        self.alien_vertical_speed = 1.0
        self.alien_points = 10
        self.alien_bullet_speed = 2.0
        self.max_aliens = 5

    def increase_speed(self) -> None:
        """Speed up the aliens, and make them worth more, when the player reaches a new level."""
        self.alien_speed *= self.speedup_scale
        self.alien_vertical_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        self.alien_bullet_speed *= self.speedup_scale
        self.max_aliens += 1
