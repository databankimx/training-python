"""
Chapter 12, exercise 12-5: Keys.

Make a Pygame file that creates an empty screen. In the event loop, print the event.key attribute
whenever a pygame.KEYDOWN event is detected. Run the program and press various keys to see how
Pygame responds.

Extension: also show the name of the last key pressed in the window.
"""

import sys
import pygame


def run_keys() -> None:
    """Open an empty window, print the key code of each key press, and show the last key's name."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Keys")
    font = pygame.font.Font(None, 72)
    last_key = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                print(event.key)
                last_key = pygame.key.name(event.key)

        screen.fill((230, 230, 230))
        if last_key:
            text = font.render(last_key, True, (30, 30, 30))
            screen.blit(text, text.get_rect(center=screen.get_rect().center))
        pygame.display.flip()


if __name__ == "__main__":
    run_keys()
