"""
Alien Invasion Game - Chapter 14: Scoring

This module tracks statistics for the game, such as the number of ships the player has left, the
score, the level, and the high score.
"""


class GameStats: #pylint: disable=too-few-public-methods
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game) -> None:
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # The high score should never be reset.
        self.high_score = 0

    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
