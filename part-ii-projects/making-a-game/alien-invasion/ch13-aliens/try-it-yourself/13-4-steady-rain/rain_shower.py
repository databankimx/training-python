"""
Chapter 12, exercise 13-4: Steady Rain.

Modify the code in exercise 13-3 so that when a row of raindrops disappears off the bottom of the
screen, a new row appears at the top of the screen and begins to fall.
"""

import sys

import pygame

from raindrop import Raindrop
from settings import Settings


class RainShower: #pylint: disable=too-few-public-methods
    """Overall class to manage the steady rain and its main loop."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rain Shower")

        self.raindrops = pygame.sprite.Group()
        self._create_rain()

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self._update_raindrops()
            self._update_screen()

    def _update_raindrops(self) -> None:
        """Update the positions of all raindrops."""
        self._check_rain_bottom()
        self.raindrops.update()

    def _check_rain_bottom(self) -> None:
        """Replace any raindrop that has left the screen with a new one at the top."""
        for drop in self.raindrops.sprites():
            if drop.check_edge():
                self.raindrops.remove(drop)
                self._create_raindrop(True)

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

    def _create_rain(self) -> None:
        """Create the field of raindrops."""
        for _ in range(self.settings.num_raindrops):
            self._create_raindrop()

    def _create_raindrop(self, new_drop: bool = False) -> None:
        """Create a raindrop and add it to the group."""
        raindrop = Raindrop(self, new_drop)
        self.raindrops.add(raindrop)

    def _update_screen(self) -> None:
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.raindrops.draw(self.screen)

        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    rs = RainShower()
    rs.run_game()
