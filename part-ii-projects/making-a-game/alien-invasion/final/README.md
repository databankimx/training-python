# Alien Invasion (Final)

This is the finished Alien Invasion game from *Python Crash Course* (3rd edition), chapters 12 to 14. It's the
baseline for exercise 14-7, which expands the game.

## Requirements

Pygame. Install it once with:

```pwsh
python -m pip install pygame
```

## Running the game

From this folder, run:

```pwsh
python alien_invasion.py
```

Click Play to start. Use the left and right arrow keys to move the ship, and the space bar to fire. Press Q to
quit.

## What's in this folder

- `alien_invasion.py`: the main game, and the game loop
- `settings.py`: all the settings, including the speeds and the speed-up
- `ship.py`, `bullet.py`, `alien.py`: the moving parts of the game
- `game_stats.py`: the score, the ships left, the level and the high score
- `scoreboard.py`: the score, high score, level and ships left on screen
- `button.py`: the Play button
- `images/`: the ship and alien pictures

## Notes

The high score is kept while the game runs. It isn't saved between runs. Exercise 14-5 adds that.
