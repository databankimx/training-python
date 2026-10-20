"""
Chapter 14, exercise 14-7: Expanding the Game.

This is the expanded Alien Invasion. Ideas used here:

- The fleet is four rows, one for each colour of alien, and any extra rows are a random
  mix at the top.
- The aliens, the ship and the explosions are animated from frame files.
- The ship plays its shooting animation each time it fires.
- An alien that's hit plays its explosion. A ship that's hit plays the kaboom, without
  pausing the game.
- Aliens fire red zigzag bullets, up to three on the screen at once.
- Easy, Medium and Hard buttons set the speed and the fleet size, and the high score is
  kept in a file.
"""

#pylint: disable=line-too-long

import random
import sys

import pygame

from animation import Explosion, FRAME_DELAY, load_frames
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from alien_bullet import AlienBullet
from button import Button
from sounds import pause_music, play_explosion, play_womp, resume_music, start_background_music


class AlienInvasion: #pylint: disable=too-many-instance-attributes
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        start_background_music()
        pause_music()  # the music waits for the first game
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.alien_bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self._create_fleet()

        # The time of the last round of alien shooting rolls.
        self.last_shot_roll = pygame.time.get_ticks()

        # The time until which the ship is down, showing its kaboom. The ship can't move or be hit until then.
        self.ship_down_until = 0

        # Make the Play buttons.
        self.play_button_easy = Button(self, "PLAY - EASY", -75)
        self.play_button_medium = Button(self, "PLAY - MEDIUM")
        self.play_button_hard = Button(self, "PLAY - HARD", 75)

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                if not self._ship_is_down():
                    self.ship.update()
                self._update_bullets()
                self._update_aliens()
                self._alien_shoot()
                self._update_alien_bullets()

            self.explosions.update()
            self._update_screen()
            self.clock.tick(60)

    def _quit_game(self) -> None:
        """Save the high score, then close the game."""
        self.stats.set_high_score()
        pygame.quit()
        sys.exit()

    def _check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_buttons(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_play_buttons(self, mouse_pos: tuple[int, int]) -> None:
        """Start a new game at the difficulty level of the Play button that was clicked."""
        easy_button_clicked = self.play_button_easy.rect.collidepoint(mouse_pos)
        medium_button_clicked = self.play_button_medium.rect.collidepoint(mouse_pos)
        hard_button_clicked = self.play_button_hard.rect.collidepoint(mouse_pos)

        difficulty_level = 1.0
        if easy_button_clicked:
            difficulty_level -= self.settings.difficulty_modifier
        if hard_button_clicked:
            difficulty_level += self.settings.difficulty_modifier

        go_play = easy_button_clicked or medium_button_clicked or hard_button_clicked
        if go_play and not self.stats.game_active:
            self.settings.initialize_dynamic_settings(difficulty_level)
            self._start_game()

    def _start_game(self) -> None:
        """Reset the statistics and the game objects, and start a new game."""
        self.stats.reset_stats()
        self.stats.game_active = True
        resume_music()
        self.sb.prep_images()

        self.bullets.empty()
        self.alien_bullets.empty()
        self.aliens.empty()
        self.explosions.empty()
        self._create_fleet()
        self.ship.center_ship()
        self.last_shot_roll = pygame.time.get_ticks()
        self.ship_down_until = 0

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event: pygame.event.Event) -> None:
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key in (pygame.K_q, pygame.K_ESCAPE):
            self._quit_game()
        elif event.key in (pygame.K_r, pygame.K_RETURN, pygame.K_KP_ENTER) and self.stats.game_active:
            self._return_to_start_screen()
        elif event.key == pygame.K_SPACE and self.stats.game_active and not self._ship_is_down():
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self.settings.initialize_dynamic_settings(self.settings.difficulty_level)
            self._start_game()

    def _return_to_start_screen(self) -> None:
        """Stop the current game, clear the field, and show the start screen. The game doesn't quit."""
        self._end_game()
        self.bullets.empty()
        self.alien_bullets.empty()
        self.aliens.empty()
        self.explosions.empty()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self) -> None:
        """Start the ship's shooting animation, and add a new bullet."""
        if len(self.bullets) < self.settings.bullets_allowed:
            self.ship.fire()
            self.bullets.add(Bullet(self))

    def _update_bullets(self) -> None:
        """Update the ship's bullets, and remove any that have left the screen."""
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self) -> None:
        """Respond to bullets hitting aliens. An alien that's hit explodes, and a new fleet starts when the
        last alien is gone."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            play_explosion()
            for hit_aliens in collisions.values():
                for alien in hit_aliens:
                    self.explosions.add(Explosion(self.screen, f"{alien.colour}-boom",
                                                  alien.rect.center))
                self.stats.score += self.settings.alien_points * len(hit_aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            self._start_next_fleet()

    def _start_next_fleet(self) -> None:
        """Clear the bullets, make a new fleet, speed the game up, and show the new level."""
        self.bullets.empty()
        self._create_fleet()
        self.settings.increase_speed()

        self.stats.level += 1
        self.sb.prep_level()

    def _update_aliens(self) -> None:
        """Check if the fleet is at an edge, then update the positions of all aliens."""
        self._check_fleet_edges()
        self.aliens.update()

        if not self._ship_is_down() and pygame.sprite.spritecollideany(self.ship, self.aliens):
            # An alien touching the ship starts a new fleet.
            self._ship_hit(new_fleet=True)

        self._check_aliens_bottom()

    def _alien_shoot(self) -> None:
        """Every second, give each alien a chance to fire. There are at most three alien bullets at once."""
        now = pygame.time.get_ticks()
        if now - self.last_shot_roll < self.settings.alien_shoot_interval:
            return
        self.last_shot_roll = now

        for alien in self.aliens.sprites():
            if len(self.alien_bullets) >= self.settings.alien_bullets_allowed:
                break
            fires = random.random() < self.settings.alien_shoot_chance
            if fires and not self._alien_has_bullet(alien):
                self.alien_bullets.add(AlienBullet(self, alien))

    def _alien_has_bullet(self, alien: Alien) -> bool:
        """Return True if this alien's last bullet is still on screen."""
        return any(bullet.source is alien for bullet in self.alien_bullets)

    def _update_alien_bullets(self) -> None:
        """Move the alien bullets, and handle those that leave the screen or hit the ship."""
        self.alien_bullets.update()

        for bullet in self.alien_bullets.copy():
            if bullet.has_passed_bottom():
                self.alien_bullets.remove(bullet)
            elif not self._ship_is_down() and bullet.rect.colliderect(self.ship.rect):
                # A bullet hit keeps the existing fleet going.
                self.alien_bullets.remove(bullet)
                self._ship_hit(new_fleet=False)
                if not self.stats.game_active:
                    return

    def _ship_is_down(self) -> bool:
        """Return True while the ship is showing its kaboom, and can't move, fire or be hit."""
        return pygame.time.get_ticks() < self.ship_down_until

    def _ship_hit(self, new_fleet: bool) -> None:
        """Start the kaboom, and lose a ship, without pausing the game.

        If new_fleet is True, the aliens are replaced with a new fleet. If it's False, the existing fleet carries on.
        Either way the ship returns to the centre once the kaboom has finished.
        """
        # The kaboom plays where the ship was hit.
        self.explosions.add(Explosion(self.screen, "kaboom", self.ship.rect.center))
        play_explosion()
        kaboom_duration = len(load_frames("kaboom")) * FRAME_DELAY
        self.ship_down_until = pygame.time.get_ticks() + kaboom_duration

        self.stats.ships_left -= 1
        self.sb.prep_ships()

        self.bullets.empty()
        self.alien_bullets.empty()
        self.ship.center_ship()

        if self.stats.ships_left > 0:
            if new_fleet:
                self.aliens.empty()
                self._create_fleet()
        else:
            play_womp()
            self._end_game()

    def _end_game(self) -> None:
        """Stop the game, save the high score, pause the music, and show the Play buttons again."""
        self.stats.game_active = False
        self.stats.set_high_score()
        pause_music()
        pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self) -> None:
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit(new_fleet=True)
                break

    def _check_fleet_edges(self) -> None:
        """Change direction and drop if the fleet reaches either edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self) -> None:
        """Change direction and drop the fleet."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self) -> None:
        """Create the fleet, with the number of rows and columns for the difficulty level."""
        for row_number in range(self.settings.fleet_rows):
            for alien_number in range(self.settings.fleet_columns):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number: int, row_number: int) -> None:
        """Create an alien of the row's colour, and place it in its row.

        The fleet has a row of each colour at the bottom of the fleet. Any extra rows are at the top, and are
        a random mix of colours.
        """
        colours = self.settings.alien_colours
        mixed_rows = max(0, self.settings.fleet_rows - len(colours))
        if row_number < mixed_rows:
            colour = random.choice(colours)
        else:
            colour = colours[row_number - mixed_rows]

        alien = Alien(self, colour)
        alien_width, alien_height = alien.rect.size #pylint: disable=unused-variable #NOSONAR
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _update_screen(self) -> None:
        """Draw the scene, and show it. The ship is hidden while it's showing its kaboom."""
        self.screen.fill(self.settings.bg_color)

        if not self._ship_is_down():
            self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.alien_bullets.sprites():
            bullet.draw_bullet()
        for alien in self.aliens.sprites():
            alien.blitme()
        for explosion in self.explosions.sprites():
            explosion.blitme()

        self.sb.show_score()

        if not self.stats.game_active:
            self.play_button_easy.draw_button()
            self.play_button_medium.draw_button()
            self.play_button_hard.draw_button()

        pygame.display.flip()


def main() -> None:
    """Make a game instance, and run the game."""
    ai = AlienInvasion()
    ai.run_game()


if __name__ == "__main__":
    main()
