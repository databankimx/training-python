"""
Chapter 14, exercise 14-1: Press P to Play.

This module tracks statistics for the game, such as the number of ships left.
"""


class GameStats: #pylint: disable=too-few-public-methods
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game) -> None:
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

    def reset_stats(self) -> None:
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
