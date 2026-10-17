"""Finds the files a step writes, so the window can offer to open them."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

SKIP_DIRS = {"__pycache__"}
# Files shown in the system's text editor, because Windows often has no default program for them.
TEXT_SUFFIXES = {".json", ".txt", ".csv", ".log", ".md", ".py"}


def snapshot(folder: Path) -> dict[str, float]:
    """Modification time of every file under folder, keyed by path. Caches are skipped."""
    seen: dict[str, float] = {}
    for root, dirs, files in os.walk(folder):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for name in files:
            path = os.path.join(root, name)
            try:
                seen[path] = os.path.getmtime(path)
            except OSError:
                pass
    return seen


def written_since(folder: Path, before: dict[str, float]) -> list[Path]:
    """Files under folder that are new or changed since the snapshot, newest first."""
    after = snapshot(folder)
    changed = [path for path, mtime in after.items() if before.get(path) != mtime]
    changed.sort(key=lambda path: after[path], reverse=True)
    return [Path(path) for path in changed]


def open_in_text_editor(path: Path) -> None:
    """Open a text file in the system's text editor: Notepad on Windows."""
    if sys.platform == "win32":
        subprocess.Popen(["notepad.exe", str(path)])
    elif sys.platform == "darwin":
        subprocess.Popen(["open", "-e", str(path)])
    else:
        subprocess.Popen(["xdg-open", str(path)])
