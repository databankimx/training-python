"""
Shared settings for the lesson runner: paths, color palettes, fonts
and the visualization table.
"""

from __future__ import annotations
from pathlib import Path
from PySide6.QtCore import Qt #pylint: disable=no-name-in-module #NOSONAR

HERE = Path(__file__).resolve().parent
VENDOR = HERE / "vendor"

# Steps that have a step-through visualization, as "folder/stem" -> algorithm name.
# The player in each chapter's visualizations/ folder loads the matching algorithm script.
VISUALIZATIONS = {
    "s04-big-o-complexity/01_linear_search": "linear-search",
    "s04-big-o-complexity/02_binary_search": "binary-search",
    "s04-big-o-complexity/03_selection_sort": "selection-sort",
    "s04-big-o-complexity/04_bubble_sort": "bubble-sort",
    "s04-big-o-complexity/05_insertion_sort": "insertion-sort",
    "s04-big-o-complexity/06_quick_sort": "quick-sort",
    "s04-big-o-complexity/07_merge_sort": "merge-sort",
    "s04-big-o-complexity/08_heap_sort": "heap-sort",
    "s04-big-o-complexity/09_shell_sort": "shell-sort",
}

DARK = {
    "bg": "#1E1E1E", "panel": "#252526", "border": "#3F3F46", "fg": "#D4D4D4",
    "accent": "#007ACC", "accent_hover": "#1C97EA", "success": "#4EC9B0",
    "error": "#F44747", "muted": "#858585", "selection": "#264F78",
    "kw": "#569CD6", "ctl": "#C586C0", "str": "#CE9178", "com": "#6A9955", "num": "#B5CEA8",
    "typ": "#4EC9B0", "fn": "#DCDCAA", "var": "#9CDCFE",
    "badge": "#2D3B48", "warn": "#CCA700",
}
LIGHT = {
    "bg": "#FFFFFF", "panel": "#F3F3F3", "border": "#CCCEDB", "fg": "#1E1E1E",
    "accent": "#007ACC", "accent_hover": "#1C97EA", "success": "#007F5F",
    "error": "#CC0000", "muted": "#717171", "selection": "#ADD6FF",
    "kw": "#0000FF", "ctl": "#AF00DB", "str": "#A31515", "com": "#008000", "num": "#098658",
    "typ": "#267F99", "fn": "#795E26", "var": "#001080",
    "badge": "#DCE7F2", "warn": "#9A6700",
}

CODE_FAMILIES = ["Cascadia Mono", "Cascadia Code", "JetBrains Mono", "Consolas"]
UI_FAMILY = "Segoe UI"
FLUSH_ROLE = int(Qt.ItemDataRole.UserRole) + 1  # marks tree items to shift left to the arrow column
C_NOTE = "// Note: this runner does not support compiling or executing C code.\n"
