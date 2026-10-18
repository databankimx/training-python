"""
Chapter 14, exercise 14-8: Sideways Shooter, Final Version.

This module defines the Scoreboard class, which shows the score, high score, level, and the hits left
before the game ends.
"""

import pygame.font


class Scoreboard: #pylint: disable=too-few-public-methods
    """A class to report scoring information."""

    def __init__(self, ss_game) -> None:
        """Initialize scorekeeping attributes."""
        self.screen = ss_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ss_game.settings
        self.stats = ss_game.stats

        self.text_color = self.settings.text_color
        self.font = pygame.font.SysFont(None, 48)

        self.prep_images()

    def prep_images(self) -> None:
        """Prepare all the score images, so the scoreboard is ready to draw."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_hits_left()

    def _render(self, text: str) -> pygame.Surface:
        """Render a piece of text in the scoreboard colours."""
        return self.font.render(text, True, self.text_color, self.settings.bg_color)

    def prep_score(self) -> None:
        """Turn the score into a rendered image, in the top right corner."""
        rounded_score = round(self.stats.score, -1)
        self.score_image = self._render(f"{rounded_score:,}")
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self) -> None:
        """Turn the high score into a rendered image, at the top centre."""
        high_score = round(self.stats.high_score, -1)
        self.high_score_image = self._render(f"{high_score:,}")
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self) -> None:
        """Turn the level into a rendered image, under the score."""
        self.level_image = self._render(str(self.stats.level))
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_hits_left(self) -> None:
        """Turn the hits left before the game ends into a rendered image, in the top left corner."""
        hits_left = self.settings.rocket_limit - self.stats.rocket_hits
        self.hits_image = self._render(f"Hits left: {hits_left}")
        self.hits_rect = self.hits_image.get_rect()
        self.hits_rect.left = 20
        self.hits_rect.top = 20

    def check_high_score(self) -> None:
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self) -> None:
        """Draw the score, high score, level, and hits left to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.screen.blit(self.hits_image, self.hits_rect)
