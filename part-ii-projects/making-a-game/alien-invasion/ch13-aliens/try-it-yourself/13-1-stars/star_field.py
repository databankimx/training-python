"""
Chapter 12, exercise 13-1: Stars.

Find an image of a star, and make a grid of stars appear on the screen.
"""

import sys
import pygame

from settings import Settings
from star import Star


class StarField: #pylint: disable=too-few-public-methods
    """Overall class to manage the star field and its main loop."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Star Field")

        self.stars = pygame.sprite.Group()
        self._create_star_field()

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses. Q and Escape quit the game."""
        if event.key in (pygame.K_q, pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        """Respond to key releases."""

    def _create_star_field(self) -> None:
        """Create the field of stars."""
        star = Star(self)
        star_width, star_height = star.rect.size
        max_width_x = self.settings.screen_width - (2 * star_width)
        max_height_y = self.settings.screen_height - (2 * star_height)
        num_cols = max_width_x // (2 * star_width)
        num_rows = max_height_y // (2 * star_height)
        for row_num in range(num_rows):
            for col_num in range(num_cols):
                self._create_star(row_num, col_num)

    def _create_star(self, row_num: int, col_num: int) -> None:
        """Create a star and place it in its row and column."""
        star = Star(self)
        star_width, star_height = star.rect.size #pylint: disable=unused-variable #NOSONAR
        star.x = star_width + 2 * star_width * col_num
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_num
        self.stars.add(star)

    def _update_screen(self) -> None:
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    sf = StarField()
    sf.run_game()
