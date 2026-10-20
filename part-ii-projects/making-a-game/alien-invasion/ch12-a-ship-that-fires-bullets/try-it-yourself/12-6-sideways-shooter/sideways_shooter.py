"""
Chapter 12, exercise 12-6: Sideways Shooter.

Write a game that places a ship on the left side of the screen and allows the player to move the
ship up and down. Make the ship fire a bullet that travels right across the screen when the player
presses the spacebar. Make sure bullets are deleted once they disappear off the screen.
"""

import sys
import pygame

from missile import Missile
from rocket import Rocket
from settings import Settings


class SidewaysShooter: #pylint: disable=too-few-public-methods
    """Overall class to manage the game and its main loop."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Sideways Shooter")

        self.rocket = Rocket(self)
        self.missiles = pygame.sprite.Group()

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_missiles()
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
        """Move the rocket, fire a missile, or quit."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_missile()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        """Stop the rocket when an arrow key is released."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _fire_missile(self) -> None:
        """Create a new missile, if the limit allows one."""
        if len(self.missiles) < self.settings.missiles_allowed:
            new_missile = Missile(self)
            self.missiles.add(new_missile)

    def _update_missiles(self) -> None:
        """Move the missiles, and delete any that have left the screen."""
        self.missiles.update()

        # Loop over a copy, so the group can change inside the loop.
        for missile in self.missiles.copy():
            if missile.rect.left >= self.settings.screen_width:
                self.missiles.remove(missile)

    def _update_screen(self) -> None:
        """Redraw the screen, and make it visible."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    game = SidewaysShooter()
    game.run_game()
