"""
Chapter 14, exercise 14-3: Challenging Target Practice.

This module tracks the statistics for the game, such as the number of hits and misses, and whether the game
is active.
"""


class GameStats: #pylint: disable=too-few-public-methods
    """Track statistics for Challenging Target Practice."""

    def __init__(self, tp_game) -> None:
        """Initialize statistics, and start the game in an inactive state."""
        self.settings = tp_game.settings
        self.game_active = False
        self.reset_stats()

    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""
        self.hits = 0
        self.misses = 0
