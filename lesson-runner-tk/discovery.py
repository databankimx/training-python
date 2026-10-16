"""Discover chapters and steps in the Python training repo.

Part I: a chapter is a folder with runnable scripts, and each script is a step.

Part III: a chapter is a folder with any lesson files. Every lesson file (.md)
is a step, in file-name order. The step's code comes from the matching script
(.py) when there is one. A lesson with no script gets a placeholder. A C code
sample (.c) with the same name is shown as read-only code, because the runner
cannot run it.

A Python script is a step when its name is numbered (``01_command_args.py``),
it is ``main.py``, or it has an ``if __name__ == "__main__":`` guard. Support
modules such as ``utilities.py`` and ``trie.py`` are not steps.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# (display name, folder, include lesson-only steps)
SCOPES = (
    ("Part I - Basics", REPO_ROOT / "part-i-basics", False),
    ("Part III - Beyond the Book", REPO_ROOT / "part-iii-beyond-the-book", True),
)

# Folders that never hold lesson steps.
SKIP_DIRS = {"__pycache__", "data", "images", "config", "old", "resources",
             ".venv", "venv", "textbook-downloads"}

NO_SOURCE_TEXT = "# No source script for this lesson\n"

GUARD = re.compile(r"""if\s+__name__\s*==\s*["']__main__["']""")
NUMBERED = re.compile(r"^\d")
HEADING = re.compile(r"^#{1,3}\s+(.+?)\s*$", re.MULTILINE)
CHAPTER_FOLDER = re.compile(r"^(ch|s)(\d+)[-_]?(.*)$", re.IGNORECASE)


@dataclass
class Step:
    """One lesson step.

    kind is "script" (runnable Python), "lesson" (lesson text only), or
    "source" (read-only code sample such as C).
    """
    title: str
    number: int | None
    kind: str
    lesson_md: Path | None
    code_path: Path | None

    @property
    def runnable(self) -> bool:
        """True when Run is available for this step."""
        return self.kind == "script"


@dataclass
class Chapter:
    """A folder of steps, shown as one entry in the chapter tree."""
    name: str
    folder: Path
    steps: list[Step]
    intro_md: Path | None = None


@dataclass
class Scope:
    """A top-level group in the chapter tree (Part I, Part III)."""
    name: str
    chapters: list[Chapter] = field(default_factory=list)


def is_step(path: Path) -> bool:
    """Return True when a .py file is a runnable step rather than a support module."""
    name = path.name
    if name.startswith("_"):
        return False
    if name == "main.py" or NUMBERED.match(name):
        return True
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return False
    return GUARD.search(text) is not None


def clean_heading(text: str) -> str:
    """Plain text for a heading: drop closing hashes and inline markup such as `code` or **bold**."""
    text = re.sub(r"\s+#+\s*$", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    return text.strip()


def first_heading(md_path: Path) -> str | None:
    """Return the first heading in a Markdown file as plain text, or None."""
    try:
        text = md_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None
    match = HEADING.search(text)
    return clean_heading(match.group(1)) if match else None


def prettify(stem: str) -> str:
    """Turn a file stem such as '01_command_args' into 'Command args'."""
    text = re.sub(r"^\d+[_\s-]*", "", stem)
    text = text.replace("_", " ").replace("-", " ").strip()
    if not text:
        text = stem
    return text[:1].upper() + text[1:]


def pretty_folder(name: str) -> str:
    """Format one folder name for display, for example 'ch10-files' -> 'Ch10 · Files'."""
    match = CHAPTER_FOLDER.match(name)
    if match:
        prefix = match.group(1).capitalize() + match.group(2)
        rest = prettify(match.group(3)) if match.group(3) else ""
        return f"{prefix} · {rest}" if rest else prefix
    return prettify(name)


def natural_key(text: str) -> list:
    """Sort key that orders numbers numerically inside a name."""
    parts = re.split(r"(\d+)", text.lower())
    return [int(part) if index % 2 else part for index, part in enumerate(parts)]


def step_title(stem: str, lesson_md: Path | None) -> str:
    """Use the lesson's first heading when there is one, else the file name."""
    return (first_heading(lesson_md) if lesson_md else None) or prettify(stem)


def number_of(stem: str) -> int | None:
    """The leading number of a file name, or None."""
    match = re.match(r"^(\d+)", stem)
    return int(match.group(1)) if match else None


def folder_steps(folder: Path, include_lessons: bool) -> list[Step]:
    """All steps in one folder, in file-name order."""
    scripts = {p.stem: p for p in folder.glob("*.py") if is_step(p)}
    lessons = {p.stem: p for p in folder.glob("*.md")} if include_lessons else {}
    samples = {p.stem: p for p in folder.glob("*.c")} if include_lessons else {}

    stems = sorted(set(scripts) | set(lessons) | set(samples), key=natural_key)
    steps: list[Step] = []
    for stem in stems:
        lesson_md = lessons.get(stem)
        if stem in scripts:
            steps.append(Step(title=step_title(stem, lesson_md), number=number_of(stem),
                              kind="script", lesson_md=lesson_md, code_path=scripts[stem]))
        elif stem in samples:
            steps.append(Step(title=step_title(stem, lesson_md), number=number_of(stem),
                              kind="source", lesson_md=lesson_md, code_path=samples[stem]))
        else:
            steps.append(Step(title=step_title(stem, lesson_md), number=number_of(stem),
                              kind="lesson", lesson_md=lesson_md, code_path=None))
    return steps


def intro_for(folder: Path) -> Path | None:
    """Pick the chapter-level Markdown: 00_intro.md if present, else the first .md."""
    candidates = sorted(folder.glob("*.md"))
    for md in candidates:
        if "intro" in md.stem.lower():
            return md
    return candidates[0] if candidates else None


def discover() -> list[Scope]:
    """Return the Part I and Part III scopes with their chapters and steps."""
    scopes: list[Scope] = []
    for scope_name, root, include_lessons in SCOPES:
        folders = [root] + [p for p in root.rglob("*") if p.is_dir()]
        scope = Scope(name=scope_name)
        for folder in sorted(folders, key=lambda f: natural_key(f.relative_to(root).as_posix())):
            if folder == root:
                continue
            if any(part in SKIP_DIRS for part in folder.relative_to(root).parts):
                continue
            steps = folder_steps(folder, include_lessons)
            if not steps:
                continue
            relative = folder.relative_to(root)
            display = " / ".join(pretty_folder(part) for part in relative.parts)
            scope.chapters.append(Chapter(name=display, folder=folder, steps=steps,
                                          intro_md=intro_for(folder)))
        scopes.append(scope)
    return scopes
