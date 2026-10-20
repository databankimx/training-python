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

### Setup and Settings

`game.py` starts by importing what it needs and finding its own folder. The
settings and patterns are stored as JSON files beside the module, so the
program reads them from that folder, whatever the current directory is:

```python
import json
import os
from random import randrange

import pygame

ROOT_DIR = os.path.dirname(__file__)

def load_json(name):
    """Load a JSON file stored alongside this module"""
    with open(os.path.join(ROOT_DIR, name), encoding="utf-8") as f:
        return json.load(f)
```

`load_json()` is used for both `settings.json` and `preloads.json`. The
settings are a dictionary, and the game reads these keys:

* `rows`, `cols`: the size of the grid, in cells
* `width`, `height`: the size of the window, in pixels
* `onein`: controls how dense a random starting grid is (see below)
* `preload`: the name of a pattern in `preloads.json`, or `"none"`
* `wraparound`: whether the edges of the grid connect to each other
* `alive`, `dead`, `grid`: the colors of living cells, dead cells, and the background
* `framerate`: how many generations are drawn each second
* `debug`: whether to print the settings and show each cell's neighbor count

The rules are written as comments at the top of the file, so they sit next to
the code that implements them.

---

### The `GameOfLife` Class

The game keeps its state in a `GameOfLife` object:

```python
class GameOfLife:
    """Implements Conway's Game of Life"""

    def __init__(self):
        self.settings = load_json("settings.json")
        if self.settings["debug"]:
            print(self.settings)
        self.preload = self.settings["preload"]
        self.grid = self.create_grid()
        self.screen = None
        self.clock = pygame.time.Clock()
```

* `self.settings` holds the dictionary loaded from `settings.json`.
* `self.grid` is the current generation, a list of rows, where each cell is
  `True` (alive) or `False` (dead).
* `self.screen` is `None` until `play()` opens the window.
* `self.clock` is a `pygame` clock. It is used later to control the speed.

---

### Creating the Grid

`create_grid()` builds the first generation. It uses a preloaded pattern when
one is named, and otherwise fills the grid at random:

```python
def create_grid(self):
    """Use a preloaded pattern if available, otherwise a random grid"""
    s = self.settings
    if self.preload.lower() != "none":
        preloads = load_json("preloads.json")
        pattern = preloads.get(self.preload)
        if pattern is not None:
            return [[cell == 1 for cell in row] for row in pattern]
        self.preload = "none"
    return [[randrange(s["onein"]) == 0 for _ in range(s["cols"])]
            for _ in range(s["rows"])]
```

* The patterns in `preloads.json` are lists of `0` and `1`. The comprehension
  converts each `1` to `True` and each `0` to `False`.
* If the name is not in `preloads.json`, the function falls back to a random
  grid and sets `preload` to `"none"`. The window caption then shows that the
  grid is random.
* `randrange(onein)` returns a number from `0` to `onein - 1`, so each cell
  starts alive with a 1-in-`onein` chance. A larger `onein` gives a sparser grid.

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

### The Rules

* A living cell with fewer than two living neighbors dies.
* A living cell with two or three living neighbors lives on.
* A living cell with more than three living neighbors dies.
* A dead cell with exactly three living neighbors comes alive.

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
exactly two. The `@staticmethod` decorator means `survives()` doesn't use
`self`, so it can be called without an object.

---

### Drawing the Grid

`draw()` turns the grid into pixels. It works out the size of each cell from the
window size and the grid size, leaving a one-pixel gap between cells. Each cell is
drawn as a filled rectangle in the alive or dead color from the settings:

```python
def draw(self):
    """Draw every cell in the grid"""
    s = self.settings
    rows, cols = len(self.grid), len(self.grid[0])
    cell_w = s["width"] // cols - 1
    cell_h = s["height"] // rows - 1
    font = pygame.font.SysFont("Arial", 16) if s["debug"] else None
    for r, row in enumerate(self.grid):
        for c, alive in enumerate(row):
            x, y = (cell_w + 1) * c + 1, (cell_h + 1) * r + 1
            color = tuple(s["alive"] if alive else s["dead"])
            pygame.draw.rect(self.screen, color, pygame.Rect(x, y, cell_w, cell_h))
            if font:
                neighbors = count_neighbors(self.grid, r, c, s["wraparound"])
                self.screen.blit(font.render(str(neighbors), True, (200, 0, 0)), (x + 1, y + 2))
    pygame.display.update()
```

* When `debug` is on, a small font is created and each cell's neighbor count
  is drawn in red at the top left of the cell. This is how the "Try It" section
  below shows the neighbor counts.
* `pygame.display.update()` shows the finished frame. Nothing appears on screen
  until it is called.

---

### Starting the Game

`play()` prepares the window before the main loop begins:

```python
def play(self):
    """Run the game until the window is closed"""
    s = self.settings
    pygame.init()
    self.screen = pygame.display.set_mode((s["width"], s["height"]))
    name = self.preload if self.preload != "none" else f"random 1/{s['onein']}"
    pygame.display.set_caption(f"Conway's Game of Life ({name})")
    self.screen.fill(tuple(s["grid"]))
    self.draw()
```

* `pygame.init()` starts the library.
* `set_mode()` opens a window of the size in the settings. The `screen` object
  is what the drawing code paints onto.
* The caption shows which pattern is running, or the random density when no
  pattern is loaded.
* The background is filled with the `grid` color, and the first generation is
  drawn.

---

### The Main Loop

After the window is set up, `play()` repeats three steps until the window is
closed:

1. Check the events. A close request stops the game.
2. Replace the grid with `next_generation()`.
3. Draw the new grid, then wait so the game runs at the speed set by `framerate`.

```python
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return
    self.grid = self.next_generation()
    self.draw()
    self.clock.tick(s["framerate"])
```

`clock.tick()` pauses just long enough to keep the frame rate steady, so a faster
computer does not run the game faster.

---

### Starting Patterns

If the `preload` setting names a pattern in `preloads.json`, the game starts
from that pattern. Otherwise `create_grid()` makes a random grid, as described
above. Try changing `preload` to `"pulsar"`, `"cross"`, or `"figure-eight"`, or
set it to `"none"` for a random start.

---

### Try It

Change `framerate` in `settings.json` to speed the game up or slow it down.
Set `debug` to `true` to see each cell's neighbor count.

---
