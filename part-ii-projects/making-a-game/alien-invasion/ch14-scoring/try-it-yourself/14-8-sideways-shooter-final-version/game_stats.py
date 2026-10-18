"""
Chapter 14, exercise 14-8: Sideways Shooter, Final Version.

This module tracks the statistics for the sideways shooter: the score, the level, the number of hits on
the rocket, and the high score. The high score is never reset.
"""


class GameStats: #pylint: disable=too-few-public-methods
    """Track statistics for the sideways shooter."""

    def __init__(self, ss_game) -> None:
        """Initialize statistics, and start the game in an inactive state."""
        self.settings = ss_game.settings
        self.game_active = False
        self.reset_stats()

        # The high score should never be reset.
        self.high_score = 0

    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""
        self.rocket_hits = 0
        self.score = 0
        self.level = 1
        self.aliens_destroyed = 0
