"""Stages for the Alien Invasion project: chapters of numbered step folders, built on demand.

The project lives in part-ii-projects/making-a-game/alien-invasion. Each chapter folder
(ch12-..., ch13-...) holds numbered step folders. A step folder holds lesson.md and the
files that step adds or changes.

A lesson starts with a front matter block that lists the step's files, in order, and says
whether the lesson shows each one in full or snipped:

    ---
    files:
      - alien_invasion.py: snipped
    ---

The lesson's python code blocks follow the same order, one per file.

Building a stage copies every earlier chapter, then the steps of this chapter up to and
including the step named. This matches alien-invasion/build_stage.py, which students use
from a terminal.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path

CHAPTER_FOLDER = re.compile(r"^ch(\d+)-")
STEP_FOLDER = re.compile(r"^\d+-")
LESSON_ONLY_FILES = {"lesson.md"}
LESSON_ONLY_FOLDERS = {"lesson-images"}

FILE_LINE = re.compile(r"^\s*-\s*([\w.\-]+):\s*(full|snipped)\s*$")
CODE_BLOCK = re.compile(r"```python\n(.*?)```", re.DOTALL)


@dataclass
class StageFile:
    """One file a step adds or changes, and what the lesson shows for it."""
    name: str
    path: Path
    snipped: bool
    snippet: str | None

    @property
    def editable(self) -> bool:
        """Snipped code can't be edited, because the lesson shows only part of the file."""
        return not self.snipped


@dataclass
class StageInfo:
    """One step of a chapter, as the runner sees it."""
    chapter_folder: Path
    number: int
    folder: Path
    lesson_md: Path | None
    files: list[StageFile] = field(default_factory=list)

    def file_named(self, name: str) -> StageFile | None:
        """The stage file with this name, if the step has it."""
        return next((f for f in self.files if f.name == name), None)


def read_front_matter(text: str) -> tuple[list[tuple[str, bool]], str]:
    """Split a lesson into (declared files, body). Each file is (name, snipped)."""
    if not text.startswith("---"):
        return [], text
    lines = text.split("\n")
    end = next((i for i in range(1, len(lines)) if lines[i].strip() == "---"), None)
    if end is None:
        return [], text
    declared = []
    for line in lines[1:end]:
        match = FILE_LINE.match(line)
        if match:
            declared.append((match.group(1), match.group(2) == "snipped"))
    return declared, "\n".join(lines[end + 1:])


def strip_front_matter(text: str) -> str:
    """The lesson text without its front matter block, ready to show."""
    return read_front_matter(text)[1]


def chapter_folders(root: Path) -> list[Path]:
    """Chapter folders under the project root, in book order."""
    chapters = [p for p in root.iterdir() if p.is_dir() and CHAPTER_FOLDER.match(p.name)]
    return sorted(chapters, key=lambda p: int(CHAPTER_FOLDER.match(p.name).group(1)))


def chapter_number(chapter: Path) -> int:
    """The chapter number from a folder name such as ch12-a-ship-that-fires-bullets."""
    return int(CHAPTER_FOLDER.match(chapter.name).group(1))


def step_folders(chapter: Path) -> list[Path]:
    """Numbered step folders inside one chapter's lessons folder, in order."""
    lessons = chapter / "lessons"
    if not lessons.is_dir():
        return []
    steps = [p for p in lessons.iterdir() if p.is_dir() and STEP_FOLDER.match(p.name)]
    return sorted(steps, key=lambda p: p.name)


def load_stage(chapter: Path, number: int, folder: Path) -> StageInfo:
    """Read one step's lesson and the files it lists."""
    md = folder / "lesson.md"
    text = md.read_text(encoding="utf-8") if md.exists() else ""
    declared, body = read_front_matter(text)
    blocks = CODE_BLOCK.findall(body)

    files = []
    for index, (name, snipped) in enumerate(declared):
        path = folder / name
        snippet = blocks[index] if index < len(blocks) else None
        files.append(StageFile(name=name, path=path, snipped=snipped,
                               snippet=snippet if snipped else None))
    return StageInfo(chapter_folder=chapter, number=number, folder=folder,
                     lesson_md=md if md.exists() else None, files=files)


def load_chapter(chapter: Path) -> list[StageInfo]:
    """Every step of one chapter, in order."""
    return [load_stage(chapter, index, folder)
            for index, folder in enumerate(step_folders(chapter), start=1)]


def build_stage_into(chapter: Path, number: int, target: Path) -> None:
    """Copy the files for every step up to and including number of the chapter into target."""
    steps = step_folders(chapter)
    if not 1 <= number <= len(steps):
        raise ValueError(f"{chapter.name} has steps 1 to {len(steps)}")

    root = chapter.parent
    sources: list[Path] = []
    for earlier in chapter_folders(root):
        if earlier == chapter:
            break
        sources.extend(p for p in step_folders(earlier) if not p.name.endswith("-optional"))
    sources.extend(steps[:number])

    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    for step in sources:
        for source in step.rglob("*"):
            if not source.is_file() or source.name in LESSON_ONLY_FILES:
                continue
            relative = source.relative_to(step)
            if any(part in LESSON_ONLY_FOLDERS for part in relative.parts):
                continue
            destination = target / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)


def build_with_script(stage: StageInfo, target: Path) -> None:
    """Build a stage with alien-invasion/build_stage.py, the same script students run from a terminal.

    Using the script keeps the runner and the terminal on one copy of the build logic.
    """
    script = stage.chapter_folder.parent / "build_stage.py"
    chapter = stage.chapter_folder.name.split("-")[0]
    result = subprocess.run(
        [sys.executable, str(script), chapter, str(stage.number), str(target)],
        cwd=script.parent, capture_output=True, text=True, encoding="utf-8", check=False)
    if result.returncode != 0:
        raise RuntimeError(result.stderr or result.stdout or "build_stage.py failed")


def stage_files(stage: StageInfo) -> dict[str, str]:
    """The project's Python files as they stand after this step: name -> full text.

    Every file of the project is included, not only the ones this step changed.
    """
    with tempfile.TemporaryDirectory(prefix="alien_files_") as scratch:
        target = Path(scratch) / "project"
        build_with_script(stage, target)
        return {path.name: path.read_text(encoding="utf-8") for path in sorted(target.glob("*.py"))}
