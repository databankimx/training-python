"""Implements Conway's Game of Life"""

import json
import os
from random import randrange

import pygame

ROOT_DIR = os.path.dirname(__file__)

# Rules:
# * A living cell with fewer than two living neighbors dies.
# * A living cell with two or three living neighbors lives on.
# * A living cell with more than three living neighbors dies.
# * A dead cell with exactly three living neighbors is revived.

def load_json(name: str) -> dict:
    """Load a JSON file stored alongside this module"""
    with open(os.path.join(ROOT_DIR, name), encoding="utf-8") as f:
        return json.load(f)

def count_neighbors(grid: list[list[bool]], r: int, c: int, wrap: bool) -> int:
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

class GameOfLife:
    """Implements Conway's Game of Life"""

    def __init__(self) -> None:
        self.settings = load_json("settings.json")
        if self.settings["debug"]:
            print(self.settings)
        self.preload = self.settings["preload"]
        self.grid = self.create_grid()
        self.screen = None
        self.clock = pygame.time.Clock()

    def create_grid(self) -> list[list[bool]]:
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

    def next_generation(self) -> list[list[bool]]:
        """Apply the rules to every cell at once"""
        return [[self.survives(alive, count_neighbors(self.grid, r, c, self.settings["wraparound"]))
                 for c, alive in enumerate(row)]
                for r, row in enumerate(self.grid)]

    @staticmethod
    def survives(alive: bool, neighbors: int) -> bool:
        """Return whether a cell is alive in the next generation"""
        return neighbors == 3 or (alive and neighbors == 2)

    def draw(self) -> None:
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

    def play(self) -> None:
        """Run the game until the window is closed"""
        s = self.settings
        pygame.init()
        self.screen = pygame.display.set_mode((s["width"], s["height"]))
        name = self.preload if self.preload != "none" else f"random 1/{s['onein']}"
        pygame.display.set_caption(f"Conway's Game of Life ({name})")
        self.screen.fill(tuple(s["grid"]))
        self.draw()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            self.grid = self.next_generation()
            self.draw()
            self.clock.tick(s["framerate"])
