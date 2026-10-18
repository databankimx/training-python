"""
Chapter 14, exercise 14-8: Sideways Shooter, Final Version.

Continue developing Sideways Shooter, using everything we've done in this project. Add a Play button, make the
game speed up at appropriate points, and develop a scoring system. Be sure to refactor your code as you work,
and look for opportunities to customize the game beyond what was shown in this chapter.

In this version, a new alien appears every five seconds at a random height and moves toward the rocket. Each
alien shot down is worth points. Every ten aliens destroyed starts a new level, and the aliens speed up. The
game ends when three aliens have hit the rocket.
"""

import random
import sys

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from rocket import Rocket
from missile import Missile
from alien import Alien
from alien_bullet import AlienBullet
from button import Button


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
        self.sb = Scoreboard(self)
        self.rocket = Rocket(self)
        self.missiles = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()

        # The time of the last alien, in milliseconds since Pygame started.
        self.last_alien_time = pygame.time.get_ticks()

        # The time of the last round of alien shooting rolls.
        self.last_shot_roll = pygame.time.get_ticks()

        self.play_button = Button(self, "Play")
        self.game_over_font = pygame.font.SysFont(None, 120)

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.rocket.update()
                self._update_missiles()
                self._update_aliens()
                self._update_alien_bullets()
                self._spawn_alien()

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
        """Respond to keypresses: move the rocket, fire, or quit."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE and self.stats.game_active:
            self._fire_missile()
        elif event.key in (pygame.K_q, pygame.K_ESCAPE):
            sys.exit()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        """Stop the rocket when an arrow key is released."""
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False

    def _check_play_button(self, mouse_pos: tuple[int, int]) -> None:
        """Start a new game when the player clicks Play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self._start_game()

    def _start_game(self) -> None:
        """Reset the settings, statistics and objects, and start a new game."""
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.sb.prep_images()
        self.rocket.center_rocket()
        self.missiles.empty()
        self.aliens.empty()
        self.alien_bullets.empty()
        self.last_alien_time = pygame.time.get_ticks()
        self.last_shot_roll = pygame.time.get_ticks()
        self.stats.game_active = True

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _fire_missile(self) -> None:
        """Create a new missile and add it to the missiles group."""
        if len(self.missiles) < self.settings.missiles_allowed:
            self.missiles.add(Missile(self))

    def _spawn_alien(self) -> None:
        """Add a new alien once the spawn interval has passed."""
        now = pygame.time.get_ticks()
        if now - self.last_alien_time >= self.settings.alien_spawn_interval:
            if len(self.aliens) < self.settings.max_aliens:
                self.aliens.add(Alien(self))
                self.last_alien_time = now

    def _update_missiles(self) -> None:
        """Update missiles, remove those that leave the screen, and score the aliens they hit."""
        self.missiles.update()

        for missile in self.missiles.copy():
            if missile.rect.left >= self.settings.screen_width:
                self.missiles.remove(missile)

        hits = pygame.sprite.groupcollide(self.missiles, self.aliens, True, True)
        for aliens in hits.values():
            self._score_aliens(len(aliens))

    def _score_aliens(self, number_of_aliens: int) -> None:
        """Add the points for the aliens destroyed, and check for a new level or high score."""
        self.stats.aliens_destroyed += number_of_aliens
        self.stats.score += self.settings.alien_points * number_of_aliens
        self.sb.prep_score()
        self.sb.check_high_score()
        self._check_level()

    def _check_level(self) -> None:
        """Start a new level after every fixed number of aliens destroyed."""
        new_level = 1 + self.stats.aliens_destroyed // self.settings.aliens_per_level
        if new_level > self.stats.level:
            self.stats.level = new_level
            self.settings.increase_speed()
            self.sb.prep_level()

    def _update_aliens(self) -> None:
        """Move the aliens, and handle aliens that leave the screen or hit the rocket."""
        self.aliens.update()
        self._alien_shoot()

        for alien in self.aliens.copy():
            if alien.has_left_screen():
                self.aliens.remove(alien)
            elif alien.rect.colliderect(self.rocket.rect):
                # The alien hits the rocket, and is removed.
                self.aliens.remove(alien)
                self._rocket_hit()
                if not self.stats.game_active:
                    return

    def _rocket_hit(self) -> None:
        """Count a hit on the rocket, and end the game when there are none left."""
        self.stats.rocket_hits += 1
        self.sb.prep_hits_left()
        if self.stats.rocket_hits >= self.settings.rocket_limit:
            self._end_game()

    def _end_game(self) -> None:
        """Stop the game, and show the Play button again."""
        self.stats.game_active = False
        pygame.mouse.set_visible(True)

    def _alien_shoot(self) -> None:
        """Every two seconds, give each alien a chance to fire, if it has no bullet on screen."""
        now = pygame.time.get_ticks()
        if now - self.last_shot_roll < self.settings.alien_shoot_interval:
            return
        self.last_shot_roll = now

        for alien in self.aliens.sprites():
            fires = random.random() < self.settings.alien_shoot_chance
            if fires and not self._alien_has_bullet(alien):
                self.alien_bullets.add(AlienBullet(self, alien))

    def _alien_has_bullet(self, alien: Alien) -> bool:
        """Return True if this alien's last bullet is still on screen."""
        return any(bullet.source is alien for bullet in self.alien_bullets)

    def _update_alien_bullets(self) -> None:
        """Move the alien bullets, and handle those that leave the screen or hit the rocket."""
        self.alien_bullets.update()

        for bullet in self.alien_bullets.copy():
            if bullet.has_left_screen():
                self.alien_bullets.remove(bullet)
            elif bullet.rect.colliderect(self.rocket.rect):
                # The bullet hits the rocket, and is removed.
                self.alien_bullets.remove(bullet)
                self._rocket_hit()
                if not self.stats.game_active:
                    return

    def _update_screen(self) -> None:
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for missile in self.missiles.sprites():
            missile.draw_missile()
        for alien in self.aliens.sprites():
            alien.blitme()
        for bullet in self.alien_bullets.sprites():
            bullet.draw_bullet()

        self.sb.show_score()

        if not self.stats.game_active:
            if self.stats.rocket_hits >= self.settings.rocket_limit:
                self._draw_game_over()
            self.play_button.draw_button()

        pygame.display.flip()

    def _draw_game_over(self) -> None:
        """Draw the game over message in the middle of the screen."""
        title = self.game_over_font.render("GAME OVER", True, self.settings.text_color)
        title_rect = title.get_rect(center=(self.screen.get_rect().centerx,
                                            self.screen.get_rect().centery - 120))
        self.screen.blit(title, title_rect)


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ss = SidewaysShooter()
    ss.run_game()
