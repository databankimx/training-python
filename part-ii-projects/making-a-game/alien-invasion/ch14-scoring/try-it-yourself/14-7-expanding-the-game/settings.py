"""
Chapter 14, exercise 14-7: Expanding the Game.

This module stores all the settings for the game. Static settings stay the same
for the whole run, and dynamic settings change during play and are reset at the
start of each game.
"""


class Settings: #pylint: disable=too-few-public-methods
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's static settings."""
        # Screen settings: a window, not fullscreen.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (45, 50, 60)
        self.text_color = (220, 220, 220)

        # Ship settings
        self.ship_limit = 3

        # Ship bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (0, 160, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_colours = ["blue", "green", "pink", "yellow"]
        self.fleet_drop_speed = 10
        # Aliens rolled for a shot every this many milliseconds.
        self.alien_shoot_interval = 1000
        # The chance that an alien without a bullet fires on each roll.
        self.alien_shoot_chance = 0.05

        # Alien bullet settings: red zigzags.
        self.alien_bullet_width = 6
        self.alien_bullet_height = 24
        self.alien_bullet_color = (200, 0, 0)
        self.alien_bullets_allowed = 3

        # How quickly the game speeds up, and how much the alien points grow.
        self.speedup_scale = 1.1
        self.score_scale = 1.5

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
        self.alien_bullet_speed = 2.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # The fleet's size depends on the difficulty: Easy 4 x 6, Medium 5 x 6, Hard 6 x 7.
        if self.difficulty_level < 1:
            self.fleet_rows, self.fleet_columns = 4, 6
        elif self.difficulty_level > 1:
            self.fleet_rows, self.fleet_columns = 6, 7
        else:
            self.fleet_rows, self.fleet_columns = 5, 6

        # Scoring
        self.alien_points = int(50 * self.difficulty_level)

    def increase_speed(self) -> None:
        """Speed up the game, and make the aliens worth more, when a fleet is cleared."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_bullet_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale) #pylint: disable=attribute-defined-outside-init
