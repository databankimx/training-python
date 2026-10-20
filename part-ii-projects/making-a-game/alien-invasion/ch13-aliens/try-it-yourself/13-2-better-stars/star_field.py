"""
Chapter 12, exercise 13-2: Better Stars.

Make a more realistic star pattern by introducing randomness when each star is placed. Use
randint(-10, 10) to adjust each star's position by a random amount, as in exercise 13-1.
"""

import sys
from random import randint

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
        """Create the field of stars, one at a time, at random positions."""
        star_num = 0
        while star_num < self.settings.num_stars:
            self._create_star()
            star_num += 1

    def _create_star(self) -> None:
        """Create a star and place it at a random position on the screen."""
        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = randint(0, self.settings.screen_width - star_width)
        star.rect.x = star.x
        star.y = randint(0, self.settings.screen_height - star_height)
        star.rect.y = star.y

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
