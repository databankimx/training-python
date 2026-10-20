"""
Chapter 12, exercise 12-2: Game Character.

Draw a game character at the center of the screen, with the background color of its image
matched to the background color of the screen.
"""

import sys
import pygame

from character import Character
from settings import Settings


class GameCharacter: #pylint: disable=too-few-public-methods
    """Overall class to manage the window and its main loop."""

    def __init__(self) -> None:
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Game Character")

        self.character = Character(self)

    def run_game(self) -> None:
        """Start the main loop for the game."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill(self.settings.bg_color)
            self.character.blitme()
            pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    game = GameCharacter()
    game.run_game()
