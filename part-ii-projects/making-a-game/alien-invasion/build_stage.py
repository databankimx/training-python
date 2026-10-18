"""Build the Alien Invasion project as it stands after a given chapter step, and optionally run it.

Layout: each chapter folder (ch12-..., ch13-..., and so on) holds numbered step folders
directly. Each step folder holds the files that step adds or changes, plus lesson.md.

Two kinds of files are never copied into a build:
    lesson.md           the lesson text
    lesson-images/      screenshots shown in the lesson

Building to a chapter and step copies every earlier chapter, then the steps of this
chapter up to and including the one named. Later steps overwrite earlier ones. Images
from earlier steps (such as ship.bmp) are kept, so the build has every asset it needs.

A step folder on its own is not a runnable project. Use this script to build one.

Usage:
    python build_stage.py ch12 7                 build into build\\ch12-step-07
    python build_stage.py ch12 7 --run           build, then run the game
    python build_stage.py ch12 7 build\\mine     build into a folder of your choosing
    python build_stage.py --list
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHAPTER_FOLDER = re.compile(r"^ch(\d+)-")
STEP_FOLDER = re.compile(r"^\d+-")
LESSON_ONLY_FILES = {"lesson.md"}
LESSON_ONLY_FOLDERS = {"lesson-images"}


def chapter_folders() -> list[Path]:
    """Chapter folders in book order."""
    chapters = [p for p in HERE.iterdir() if p.is_dir() and CHAPTER_FOLDER.match(p.name)]
    return sorted(chapters, key=lambda p: int(CHAPTER_FOLDER.match(p.name).group(1)))


def step_folders(chapter: Path) -> list[Path]:
    """Step folders for one chapter, in order. Steps live in the chapter's lessons folder."""
    lessons = chapter / "lessons"
    if not lessons.is_dir():
        return []
    steps = [p for p in lessons.iterdir() if p.is_dir() and STEP_FOLDER.match(p.name)]
    return sorted(steps, key=lambda p: p.name)


def find_chapter(name: str) -> Path:
    """Find a chapter folder from 'ch12' or '12'."""
    number = int(re.sub(r"\D", "", name))
    for chapter in chapter_folders():
        if int(CHAPTER_FOLDER.match(chapter.name).group(1)) == number:
            return chapter
    raise SystemExit(f"No chapter folder found for {name}")


def is_build_file(path: Path, step: Path) -> bool:
    """True when a file belongs in a build, not just in the lesson."""
    if not path.is_file() or path.name in LESSON_ONLY_FILES:
        return False
    relative_parts = path.relative_to(step).parts
    return not any(part in LESSON_ONLY_FOLDERS for part in relative_parts)


def build(chapter_name: str, step_number: int, target: Path) -> None:
    """Copy the files for every step up to and including step_number of the chapter."""
    chapter = find_chapter(chapter_name)
    steps = step_folders(chapter)
    if not 1 <= step_number <= len(steps):
        raise SystemExit(f"{chapter.name} has steps 1 to {len(steps)}")

    sources: list[Path] = []
    for earlier in chapter_folders():
        if earlier == chapter:
            break
        # Optional steps (folder names ending in -optional) are not carried into later chapters.
        sources.extend(p for p in step_folders(earlier) if not p.name.endswith("-optional"))
    sources.extend(steps[:step_number])

    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    for step in sources:
        for source in step.rglob("*"):
            if is_build_file(source, step):
                destination = target / source.relative_to(step)
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(source, destination)


def list_steps() -> None:
    """Print every chapter and its steps."""
    for chapter in chapter_folders():
        print(chapter.name)
        for index, folder in enumerate(step_folders(chapter), start=1):
            print(f"  {index:2d}  {folder.name}")


def main(argv: list[str]) -> None:
    """Command-line entry point."""
    if argv[1:] == ["--list"]:
        list_steps()
        return
    if len(argv) < 3:
        raise SystemExit(__doc__)

    chapter_name, step_text = argv[1], argv[2]
    run = "--run" in argv[3:]
    targets = [arg for arg in argv[3:] if arg != "--run"]
    step_number = int(step_text)

    if targets:
        target = Path(targets[0]).resolve()
    else:
        target = HERE / "build" / f"{find_chapter(chapter_name).name.split('-')[0]}-step-{step_number:02d}"

    build(chapter_name, step_number, target)
    print(f"Built {chapter_name} step {step_number} into {target}")

    if run:
        subprocess.run([sys.executable, "alien_invasion.py"], cwd=target, check=False)


if __name__ == "__main__":
    main(sys.argv)
