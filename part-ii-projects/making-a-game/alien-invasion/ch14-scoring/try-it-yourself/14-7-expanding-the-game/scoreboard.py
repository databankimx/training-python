"""
Chapter 14, exercise 14-7: Expanding the Game.

This module defines the Scoreboard class, which shows the score, the high score,
the level, and the ships left.
"""

#pylint: disable=line-too-long, attribute-defined-outside-init

import pygame.font
from pygame.sprite import Group, Sprite

from animation import load_frames


class Scoreboard: #pylint: disable=too-few-public-methods
    """A class to report scoring information."""

    def __init__(self, ai_game) -> None:
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        self.text_color = self.settings.text_color
        self.font = pygame.font.SysFont(None, 48)

        self.prep_images()

    def prep_images(self) -> None:
        """Prepare every score image, so the scoreboard is ready to draw."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

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

    def prep_ships(self) -> None:
        """Show how many ships are left, as half-size ship images in the top left corner."""
        # The resting ship (frame 0), shrunk to half size.
        resting = load_frames("ship-anim")[0]
        icon_size = (resting.get_width() // 2, resting.get_height() // 2)
        icon_image = pygame.transform.smoothscale(resting, icon_size)

        gap = 8
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            icon = Sprite()
            icon.image = icon_image
            icon.rect = icon_image.get_rect()
            icon.rect.x = 10 + ship_number * (icon.rect.width + gap)
            icon.rect.y = 10
            self.ships.add(icon)

    def check_high_score(self) -> None:
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self) -> None:
        """Draw the score, high score, level, and ships to the screen."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
