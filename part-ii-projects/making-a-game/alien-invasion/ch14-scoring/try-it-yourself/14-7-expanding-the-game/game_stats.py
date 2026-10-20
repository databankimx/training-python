"""
Chapter 14, exercise 14-7: Expanding the Game.

This module tracks the statistics for the game: the ships left, the score, the level,
and the all-time high score. The high score is saved to a file, so it's kept between runs.
"""

import json
import os


class GameStats: #pylint: disable=too-few-public-methods
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game) -> None:
        """Initialize statistics, and load the high score."""
        self.settings = ai_game.settings
        self.game_active = False
        self.reset_stats()

        # Locate the high score file, next to this file.
        root_dir = os.path.dirname(os.path.abspath(__file__))
        self.hi_score_file = os.path.join(root_dir, "hi_score.json")

        # The high score is never reset during a game, and is loaded from the file.
        self.high_score = self.get_high_score()

    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def get_high_score(self) -> int:
        """Read the high score from the JSON file, or return 0 if there isn't one."""
        try:
            with open(self.hi_score_file, encoding="utf-8") as file:
                return int(json.load(file))
        except (OSError, ValueError):
            return 0

    def set_high_score(self) -> None:
        """Write the high score to the JSON file."""
        with open(self.hi_score_file, "w", encoding="utf-8") as file:
            json.dump(str(self.high_score), file)
