"""
Chapter 13, exercise 13-6: Game Over.

This module tracks the statistics for the sideways shooter: how many times an alien has hit the
rocket, and how many times the rocket has destroyed an alien.
"""


class GameStats: #pylint: disable=too-few-public-methods
    """Track statistics for the sideways shooter."""

    def __init__(self, ss_game) -> None:
        """Initialize statistics."""
        self.settings = ss_game.settings
        self.reset_stats()

    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""
        self.rocket_hits = 0
        self.alien_hits = 0
        self.game_active = True
