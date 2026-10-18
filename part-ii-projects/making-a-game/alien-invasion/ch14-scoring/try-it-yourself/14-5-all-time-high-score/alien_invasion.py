"""
Chapter 14, exercise 14-5: All-Time High Score.

The high score is reset every time a player closes and restarts Alien Invasion. Fix this by writing
the high score to a file before calling sys.exit() and reading in the high score when initializing
its value in GameStats.
"""

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button


class AlienInvasion: #pylint: disable=too-few-public-methods
    """Overall class to manage game assets and behavior."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics, and create a scoreboard.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Make the Play buttons.
        self.play_button_easy = Button(self, "PLAY - EASY", -75)
        self.play_button_medium = Button(self, "PLAY - MEDIUM")
        self.play_button_hard = Button(self, "PLAY - HARD", 75)

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

    def _quit_game(self) -> None:
        """Save the high score, then close the game."""
        self.stats.set_high_score()
        pygame.quit()
        sys.exit()

    def _check_aliens_bottom(self) -> None:
        """Check if any aliens have reached the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Treat this the same as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self) -> None:
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left.
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            self.stats.set_high_score()
            pygame.mouse.set_visible(True)

    def _update_aliens(self) -> None:
        """Update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_bottom()

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
        """Create the fleet of aliens."""
        # Make an alien and calculate the number of aliens.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width)
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        # One column and one row are removed, so the fleet moves further before dropping.
        number_rows = available_space_y // (2 * alien_height) - 1
        number_aliens_x = available_space_x // (2 * alien_width) - 1

        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number: int, row_number: int) -> None:
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size #pylint: disable=unused-variable #NOSONAR
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    def _check_events(self) -> None:
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._quit_game()

            # Handle mouse clicks.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_buttons(mouse_pos)

            # Handle keypresses.
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
            # Reset the game settings for the chosen difficulty.
            self.settings.initialize_dynamic_settings(difficulty_level)
            self._start_game()

    def _start_game(self) -> None:
        """Reset the game and start a new one."""
        # Reset the game statistics.
        self.stats.reset_stats()
        self.stats.game_active = True

        # Refresh the scoreboard now that the statistics have been reset.
        self.sb.prep_score()
        self.sb.prep_level()
        self.sb.prep_ships()

        # Get rid of any remaining aliens and bullets.
        self.aliens.empty()
        self.bullets.empty()

        # Create a new fleet and center the ship.
        self._create_fleet()
        self.ship.center_ship()

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
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p and not self.stats.game_active:
            self._start_game()

    def _fire_bullet(self) -> None:
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self) -> None:
        """Update position of bullets and get rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self) -> None:
        """Respond to collisions between bullets and aliens."""
        # Remove any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        # Recreate the fleet when all aliens are destroyed.
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # Increase the level.
            self.stats.level += 1
            self.sb.prep_level()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self) -> None:
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Draw the score information.
        self.sb.show_score()

        # Draw the play buttons if the game is inactive.
        if not self.stats.game_active:
            self.play_button_easy.draw_button()
            self.play_button_medium.draw_button()
            self.play_button_hard.draw_button()

        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
