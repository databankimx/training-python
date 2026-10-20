"""
Chapter 13, exercise 13-6: Game Over.

In the sideways shooter, keep track of the number of times the rocket is hit by an alien and the
number of times an alien is hit by a missile. End the game when the rocket has been hit three times,
then show the game over message and the final counts.
"""

import sys

import pygame

from settings import Settings
from game_stats import GameStats
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

        self.stats = GameStats(self)
        self.rocket = Rocket(self)
        self.missiles = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # The time of the last alien, in milliseconds since Pygame started.
        self.last_alien_time = pygame.time.get_ticks()

        # Fonts for the game over message.
        self.title_font = pygame.font.SysFont(None, 120)
        self.info_font = pygame.font.SysFont(None, 48)

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
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
        elif event.key == pygame.K_SPACE and self.stats.game_active:
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
        """Update missiles, remove those that leave the screen, and count the aliens they hit."""
        self.missiles.update()

        # Get rid of missiles that have left the right side of the screen.
        for missile in self.missiles.copy():
            if missile.rect.left >= self.settings.screen_width:
                self.missiles.remove(missile)

        # Remove any missiles and aliens that have collided, and count the alien hits.
        hits = pygame.sprite.groupcollide(self.missiles, self.aliens, True, True)
        self.stats.alien_hits += len(hits)

    def _update_aliens(self) -> None:
        """Move the aliens, and handle aliens that leave the screen or hit the rocket."""
        self.aliens.update()

        for alien in self.aliens.copy():
            if alien.has_left_screen():
                self.aliens.remove(alien)
            elif alien.rect.colliderect(self.rocket.rect):
                # The alien hits the rocket, and is removed.
                self.aliens.remove(alien)
                self.stats.rocket_hits += 1
                if self.stats.rocket_hits >= self.settings.rocket_limit:
                    self._end_game()
                    return

    def _end_game(self) -> None:
        """Stop the game and print the final counts."""
        self.stats.game_active = False
        print(f"Game over. Aliens hit: {self.stats.alien_hits}. "
              f"Rocket hits: {self.stats.rocket_hits}.")

    def _update_screen(self) -> None:
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()
        for alien in self.aliens.sprites():
            alien.blitme()

        if not self.stats.game_active:
            self._draw_game_over()

        pygame.display.flip()

    def _draw_game_over(self) -> None:
        """Draw the game over message and the final counts, in the middle of the screen."""
        color = self.settings.text_color
        title = self.title_font.render("GAME OVER", True, color)
        title_rect = title.get_rect(center=self.screen.get_rect().center)
        self.screen.blit(title, title_rect)

        info = self.info_font.render(
            f"Aliens hit: {self.stats.alien_hits}    Rocket hits: {self.stats.rocket_hits}",
            True, color)
        info_rect = info.get_rect(center=(title_rect.centerx, title_rect.bottom + 40))
        self.screen.blit(info, info_rect)


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()
