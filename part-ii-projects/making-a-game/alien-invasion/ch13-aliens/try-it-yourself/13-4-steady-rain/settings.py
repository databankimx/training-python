"""
Chapter 12, exercise 13-4: Steady Rain.

This module stores the settings for the steady rain.
"""

from random import uniform


class Settings: #pylint: disable=too-few-public-methods
    """A class to store the settings for the steady rain."""

    def __init__(self) -> None:
        """Initialize the settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)

        # Raindrop settings
        self.rain_img_lg = "rain_l.png"
        self.rain_img_med = "rain_m.png"
        self.rain_img_sm = "rain_s.png"
        self.num_raindrops = 200

        # Rain settings
        self.wind_speed = uniform(-4.01, 4.01)
