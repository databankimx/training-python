"""
Chapter 12, exercise 12-4: Rocket.

Make a game that begins with a rocket in the center of the screen. Allow the player to move the
rocket up, down, left, or right using the four arrow keys. Make sure the rocket never moves
beyond any edge of the screen.
"""

import sys
import pygame

from rocket import Rocket
from settings import Settings


class RocketGame: #pylint: disable=too-few-public-methods
    """Overall class to manage the game and its main loop."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Rocket")

        self.rocket = Rocket(self)

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self) -> None:
        """Respond to keypresses and key releases."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: pygame.event.Event) -> None:
        """Start the rocket moving when an arrow key goes down."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = True
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        """Stop the rocket when an arrow key is released."""
        if event.key == pygame.K_RIGHT:
            self.rocket.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.rocket.moving_left = False
        elif event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _update_screen(self) -> None:
        """Redraw the screen, and make it visible."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    game = RocketGame()
    game.run_game()
