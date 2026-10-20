"""
Chapter 14, exercise 14-7: Expanding the Game.

This module loads the animation frames and plays them. An Animation loops forever, such as
an alien flying, and an Explosion plays once and then removes itself, such as an alien or
the ship blowing up.
"""

import os
import re

import pygame
from pygame.sprite import Sprite

# Each frame is shown for this many milliseconds (the 0.08 s delay in the frame file names).
FRAME_DELAY = 80

# The animation folders sit in the images folder next to this file.
IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "images")

# Frame files are named like frame_3_delay-0.08s.gif. The number after "frame_" is the frame order.
_FRAME_NAME = re.compile(r"frame_(\d+)_")

# Frames are loaded once, and then kept, so each animation is only read from disk one time.
_frame_cache: dict[str, list[pygame.Surface]] = {}


def load_frames(folder_name: str) -> list[pygame.Surface]:
    """Load the frames of one animation folder, in frame order."""
    if folder_name not in _frame_cache:
        folder = os.path.join(IMAGES_FOLDER, folder_name)
        numbered_files = []
        for file_name in os.listdir(folder):
            match = _FRAME_NAME.match(file_name)
            if match:
                numbered_files.append((int(match.group(1)), file_name))
        numbered_files.sort()

        _frame_cache[folder_name] = [
            pygame.image.load(os.path.join(folder, file_name)).convert_alpha()
            for _, file_name in numbered_files
        ]
    return _frame_cache[folder_name]


class Animation: #pylint: disable=too-few-public-methods
    """
    An animation that loops forever. Every object using it shares the same clock,
    so they stay in step.
    """

    def __init__(self, folder_name: str) -> None:
        """Load the frames for this animation."""
        self.frames = load_frames(folder_name)

    def frame_at(self, now: int) -> pygame.Surface:
        """Return the frame to show at the given time, in milliseconds."""
        index = (now // FRAME_DELAY) % len(self.frames)
        return self.frames[index]


class Explosion(Sprite): #pylint: disable=too-few-public-methods
    """An animation that plays once, centred on a point, and then removes itself."""

    def __init__(self, screen: pygame.Surface, folder_name: str, center: tuple[int, int]) -> None:
        """Start the explosion now, centred on the given point."""
        super().__init__()
        self.screen = screen
        self.frames = load_frames(folder_name)
        self.start_time = pygame.time.get_ticks()
        self.rect = self.frames[0].get_rect(center=center)

    def update(self, *args: object, **kwargs: object) -> None:
        """Remove the explosion once every frame has been shown."""
        elapsed = pygame.time.get_ticks() - self.start_time
        if elapsed >= len(self.frames) * FRAME_DELAY:
            self.kill()

    def blitme(self) -> None:
        """Draw the frame that's due to be shown now."""
        elapsed = pygame.time.get_ticks() - self.start_time
        index = min(elapsed // FRAME_DELAY, len(self.frames) - 1)
        self.screen.blit(self.frames[index], self.rect)
