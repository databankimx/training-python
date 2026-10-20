"""
Chapter 12, exercise 13-1: Stars.

This module stores the settings for the star field.
"""

import os


class Settings: #pylint: disable=too-few-public-methods
    """A class to store the settings for the star field."""

    def __init__(self) -> None:
        """Initialize the settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Star settings
        root_dir = os.path.dirname(__file__)
        file_name = "star.bmp"
        self.star_file_path = os.path.join(root_dir, "images", file_name)
