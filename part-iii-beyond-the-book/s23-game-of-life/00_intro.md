## Conway's Game of Life

Conway's Game of Life is a grid of cells that are either alive or dead. Each
turn, every cell follows four rules based on its eight neighbors. Simple rules
like these can produce surprisingly complex patterns, such as gliders that
travel across the grid and guns that keep producing them.

The code is in this folder:

* [`main.py`](./main.py) - creates the game and starts it
* [`game.py`](./game.py) - the grid, the rules, and the drawing
* [`settings.json`](./settings.json) - the grid size, colors, and speed
* [`preloads.json`](./preloads.json) - patterns you can start from

This lesson needs the `pygame` library. Install it with:

```pwsh
python -m pip install pygame
```

Run the game:

```pwsh
python main.py
```

---

### The Rules

* A living cell with fewer than two living neighbors dies.
* A living cell with two or three living neighbors lives on.
* A living cell with more than three living neighbors dies.
* A dead cell with exactly three living neighbors comes alive.

---

### Counting Neighbors

`count_neighbors()` checks the eight cells around a position. At the edge of
the grid, it either skips the missing cells or, if `wraparound` is set in the
settings, wraps around to the opposite edge:

```python
def count_neighbors(grid, r, c, wrap):
    """Count the living cells around grid[r][c]"""
    rows, cols = len(grid), len(grid[0])
    count = 0
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0:
                continue
            y, x = r + dr, c + dc
            if wrap:
                y, x = y % rows, x % cols
            if 0 <= y < rows and 0 <= x < cols and grid[y][x]:
                count += 1
    return count
```

The `dr == dc == 0` check skips the cell itself. Chained comparisons like this
read naturally and save a line.

---

### One Generation at a Time

`next_generation()` builds a new grid from the current one. Every cell's new
state is decided from the old grid, so all the cells change at the same time:

```python
def next_generation(self):
    """Apply the rules to every cell at once"""
    return [[self.survives(alive, count_neighbors(self.grid, r, c, self.settings["wraparound"]))
             for c, alive in enumerate(row)]
            for r, row in enumerate(self.grid)]

@staticmethod
def survives(alive, neighbors):
    """Return whether a cell is alive in the next generation"""
    return neighbors == 3 or (alive and neighbors == 2)
```

`survives()` puts all four rules in one expression. A cell is alive in the next
generation if it has exactly three neighbors, or if it is already alive and has
exactly two.

---

### Starting Patterns

If the `preload` setting names a pattern in `preloads.json`, the game starts
from that pattern. Otherwise it creates a random grid, where each cell has a
1-in-`onein` chance of starting alive. Try changing `preload` to `"pulsar"`,
`"cross"`, or `"figure-eight"`, or set it to `"none"` for a random start.

---

### Try It

Change `framerate` in `settings.json` to speed the game up or slow it down.
Set `debug` to `true` to see each cell's neighbor count.

---
