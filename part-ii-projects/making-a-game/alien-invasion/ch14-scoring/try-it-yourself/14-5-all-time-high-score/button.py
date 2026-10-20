"""
Chapter 14, exercise 14-5: All-Time High Score.

This module defines the Button class, which draws a labeled rectangle the player can click.
"""

import pygame.font


class Button: #pylint: disable=too-few-public-methods, too-many-instance-attributes
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg: str, offset: int = 0) -> None:
        """Initialize button attributes. The offset moves the button up or down from the center."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button.
        self.width, self.height = 250, 50
        self.button_color = (4, 93, 93)
        self.text_color = (200, 200, 200)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.y += offset

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg: str) -> None:
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self) -> None:
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
