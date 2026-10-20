"""
Chapter 13, exercise 13-5: Sideways Shooter, Part 2.

Develop the sideways shooter to the same point as Alien Invasion. Every five seconds a new alien
appears at a random height on the right side of the screen, rotated to face the rocket. The alien
moves toward the rocket, and bounces up or down off the top and bottom edges of the screen. Missiles
destroy aliens they hit.
"""

import sys

import pygame

from settings import Settings
from rocket import Rocket
from missile import Missile
from alien import Alien


class SidewaysShooter: #pylint: disable=too-few-public-methods
    """Overall class to manage the sideways shooter and its main loop."""

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
        self.aliens = pygame.sprite.Group()

        # The time of the last alien, in milliseconds since Pygame started.
        self.last_alien_time = pygame.time.get_ticks()

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.rocket.update()
            self._update_missiles()
            self._update_aliens()
            self._spawn_alien()
            self._update_screen()
            self.clock.tick(60)

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
        """Respond to keypresses: move the rocket, fire, or quit."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key in (pygame.K_q, pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_missile()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        """Stop the rocket when an arrow key is released."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _fire_missile(self) -> None:
        """Create a new missile and add it to the missiles group."""
        if len(self.missiles) < self.settings.missiles_allowed:
            new_missile = Missile(self)
            self.missiles.add(new_missile)

    def _spawn_alien(self) -> None:
        """Add a new alien once the spawn interval has passed."""
        now = pygame.time.get_ticks()
        if now - self.last_alien_time >= self.settings.alien_spawn_interval:
            self.aliens.add(Alien(self))
            self.last_alien_time = now

    def _update_missiles(self) -> None:
        """Update missiles, remove those that leave the screen, and destroy any aliens they hit."""
        self.missiles.update()

        # Get rid of missiles that have left the right side of the screen.
        for missile in self.missiles.copy():
            if missile.rect.left >= self.settings.screen_width:
                self.missiles.remove(missile)

        # Remove any missiles and aliens that have collided.
        pygame.sprite.groupcollide(self.missiles, self.aliens, True, True)

    def _update_aliens(self) -> None:
        """Move the aliens, and remove any that leave the screen or collide with the rocket."""
        self.aliens.update()

        for alien in self.aliens.copy():
            if alien.has_left_screen() or alien.rect.colliderect(self.rocket.rect):
                # The alien hits the rocket or leaves the screen, and is removed.
                self.aliens.remove(alien)

    def _update_screen(self) -> None:
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()
        for alien in self.aliens.sprites():
            alien.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()
