# Exercise 14-5: All-Time High Score

## The exercise

The high score is reset every time a player closes and restarts Alien Invasion. Fix this by writing the high
score to a file before calling `sys.exit()` and reading in the high score when initializing its value in
`GameStats`.

## Running this exercise

From this folder, run:

```pwsh
python alien_invasion.py
```

Play a game, then press Q or Escape, or close the window. Start the game again, and the high score is still
there.

## Solution

`game_stats.py` reads the high score from `hi_score.json` when the statistics are created. If the file is
missing or can't be read, the high score is 0:

```python
class GameStats:
    --snip--

    def __init__(self, ai_game) -> None:
        """Initialize statistics."""
        --snip--
        # The high score is read from the file, so it's kept between runs.
        self.high_score = self.get_high_score()

    def get_high_score(self) -> int:
        """Read the high score from the JSON file, or return 0 if there isn't one."""
        try:
            with open(self.hi_score_file, encoding="utf-8") as file:
                return int(json.load(file))
        except (OSError, ValueError):
            return 0

    def set_high_score(self) -> None:
        """Write the high score to the JSON file."""
        with open(self.hi_score_file, "w", encoding="utf-8") as file:
            json.dump(str(self.high_score), file)
```

`alien_invasion.py` writes the high score before the game exits. Every way of closing the game goes through
`_quit_game()`, so the score is never lost:

```python
class AlienInvasion:
    --snip--

    def _quit_game(self) -> None:
        """Save the high score, then close the game."""
        self.stats.set_high_score()
        pygame.quit()
        sys.exit()
```

`_quit_game()` is called from the window's close button, and from the Q and Escape keys. The high score is
also saved when the last ship is lost, so it survives a crash after a game ends.

Other fixes were made while cleaning up this exercise. Setting `fleet_drop_speed` to 200 was a test value,
so it's back to 10. The speed-up and the point values no longer depend on the difficulty level, and the
scoreboard is refreshed after each reset, so the old score doesn't stay on screen.

## Walkthrough

**Reading on start.** `GameStats` loads the file in `__init__()`, so the high score is known before the game
starts. A missing file is not an error for the first run, so the score starts at 0.

**Saving on exit.** The save happens before `sys.exit()`, because `sys.exit()` ends the program at once, and
nothing after it runs.

**One exit path.** Routing every quit through `_quit_game()` means the save can't be skipped.

**Why the file is JSON.** JSON is a simple text format that Python reads and writes directly. The file is kept
next to the code, so the game finds it wherever it's started.

## Output

Play a game and score some points, then close the game. Start it again: the high score is still shown at the
top centre.

![High score kept between games](lesson-images/all-time-high-score.png)

## Changed files

- `game_stats.py`: reads the high score from the file, and writes it back
- `alien_invasion.py`: saves the high score on every exit
- `settings.py`: fleet drop speed back to 10, and the speed-up on every level
- `ship.py`: keeps the decimal position for smooth movement

---
