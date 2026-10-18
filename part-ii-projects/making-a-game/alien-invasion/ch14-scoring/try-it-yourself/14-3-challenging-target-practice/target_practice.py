"""
Chapter 14, exercise 14-3: Challenging Target Practice.

Start with your work from exercise 14-2 (page 283). Make the target move faster as the
game progresses, and restart the target at the original speed when the player clicks Play.
"""

import sys

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
from target import Target
from bullet import Bullet
from button import Button


class TargetPractice: #pylint: disable=too-few-public-methods, too-many-instance-attributes
    """Overall class to manage the target practice game and its main loop."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Challenging Target Practice")

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.target = Target(self)
        self.bullets = pygame.sprite.Group()

        self.play_button = Button(self, "Play")

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self.target.update()
                self._update_bullets()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses: move the ship, fire, or quit."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_bullet()
        elif event.key in (pygame.K_q, pygame.K_ESCAPE):
            sys.exit()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        """Stop the ship when an arrow key is released."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_play_button(self, mouse_pos: tuple[int, int]) -> None:
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset the target speed to its original value, then the other game parts.
            self.settings.initialize_dynamic_settings()
            self.stats.reset_stats()
            self.stats.game_active = True
            self.ship.center_ship()
            self.target.reset()
            self.bullets.empty()

            # Hide the mouse cursor.
            pygame.mouse.set_visible(False)

    def _fire_bullet(self) -> None:
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.bullets.add(Bullet(self))

    def _update_bullets(self) -> None:
        """
        Update the bullets, count hits and misses, and remove bullets that reach the target
        or the edge.
        """
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.colliderect(self.target.rect):
                # A hit: remove the bullet, count it, and speed the target up.
                self.bullets.remove(bullet)
                self.stats.hits += 1
                self.settings.increase_speed()
            elif bullet.rect.left >= self.settings.screen_width:
                # The bullet has reached the right edge, so it's a miss.
                self.bullets.remove(bullet)
                self.stats.misses += 1
                if self.stats.misses >= self.settings.misses_allowed:
                    self._end_game()
                    return

    def _end_game(self) -> None:
        """End the game, and show the Play button again."""
        self.stats.game_active = False
        pygame.mouse.set_visible(True)

    def _update_screen(self) -> None:
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.target.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw the Play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    tp = TargetPractice()
    tp.run_game()
