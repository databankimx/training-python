"""
Chapter 14, exercise 14-7: Expanding the Game.

This module plays the sounds: the martial background music, which loops for as long
as the game runs, and the sound effects for explosions and for game over.
"""

import os

import pygame

# The sound files sit in the sounds folder next to this file.
SOUNDS_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")

# Sound effects are loaded the first time they're played, and then kept.
_effects: dict[str, pygame.mixer.Sound] = {}


def start_background_music() -> None:
    """Start the background music, looping for as long as the game is running."""
    pygame.mixer.music.load(os.path.join(SOUNDS_FOLDER, "background.wav"))
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1)


def pause_music() -> None:
    """Pause the background music, for example on the start screen."""
    pygame.mixer.music.pause()


def resume_music() -> None:
    """Carry on with the background music from where it was paused."""
    pygame.mixer.music.unpause()


def _effect(name: str) -> pygame.mixer.Sound:
    """Return a sound effect, loading it from the sounds folder the first time it's needed."""
    if name not in _effects:
        _effects[name] = pygame.mixer.Sound(os.path.join(SOUNDS_FOLDER, f"{name}.wav"))
    return _effects[name]


def play_explosion() -> None:
    """Play the explosion sound, used for an alien's boom and the ship's kaboom."""
    _effect("explosion").play()


def play_womp() -> None:
    """Play the womp womp sound, used when the game is over."""
    _effect("womp").play()
