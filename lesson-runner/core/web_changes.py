"""Read-only change listings for web applications steps and exercises.

For a lesson step, the listing shows what the step adds or changes compared with the step before it. For an
exercise, it shows what the exercise adds or changes compared with the exercise it builds on. New files are shown
in full. Changed files are shown as a diff, with unchanged parts collapsed to --snip--.

The listings are made from the folders themselves, so they stay in step with the code.
"""

from __future__ import annotations

import difflib
import importlib.util
from functools import lru_cache
from pathlib import Path
from types import ModuleType

from core.web_run import WEB_ROOT

TEXT_SUFFIXES = {".py", ".html", ".txt", ".json", ".css", ".js"}
IGNORED_FOLDERS = {"__pycache__", "lesson-images"}


@lru_cache(maxsize=1)
def build_module() -> ModuleType:
    """The build script, loaded as a module, so the listings use the same rules as the build."""
    spec = importlib.util.spec_from_file_location("build_stage", WEB_ROOT / "build_stage.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def accumulated(sources: list[Path]) -> dict[str, str]:
    """The text files a build would contain, keyed by their path inside the project. Later sources win."""
    build = build_module()
    files: dict[str, str] = {}
    for source in sources:
        for path in source.rglob("*"):
            if not path.is_file() or path.suffix not in TEXT_SUFFIXES:
                continue
            relative = path.relative_to(source)
            if any(part in build.SKIPPED_NAMES or part in IGNORED_FOLDERS for part in relative.parts):
                continue
            try:
                files[relative.as_posix()] = path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
    return files


def changes_between(before: dict[str, str], after: dict[str, str]) -> dict[str, str]:
    """A read-only listing for each file that is new or changed. The keys are the file paths."""
    listing: dict[str, str] = {}
    for name in sorted(after):
        if name not in before:
            listing[name] = "# New file\n" + after[name]
        elif before[name] != after[name]:
            listing[name] = "# Changed file\n" + diff_text(before[name], after[name])
    return listing


def diff_text(old: str, new: str) -> str:
    """A unified diff, with the file header removed and each gap between changes shown as --snip--."""
    lines = difflib.unified_diff(old.splitlines(), new.splitlines(), n=2, lineterm="")
    out: list[str] = []
    hunks = 0
    for line in lines:
        if line.startswith(("---", "+++")):
            continue
        if line.startswith("@@"):
            if hunks:
                out.append("--snip--")
            hunks += 1
            continue
        out.append(line)
    return "\n".join(out)


def lesson_step_listing(step) -> dict[str, str]:
    """What a lesson step adds or changes, compared with the step before it."""
    build = build_module()
    chapter_prefix, number = step.web_build
    chapter = step.lesson_md.parent.parent.parent
    before = accumulated(build.build_sources(chapter, number - 1)) if number > 1 else {}
    after = accumulated(build.build_sources(chapter, number))
    return changes_between(before, after)


def exercise_listing(step) -> dict[str, str]:
    """What an exercise adds or changes, compared with the exercise it builds on."""
    build = build_module()
    folder = step.lesson_md.parent
    chapter = folder.parent.parent
    chain = build.exercise_chain(chapter, folder.name)
    before = accumulated(chain[:-1]) if len(chain) > 1 else {}
    after = accumulated(chain)
    return changes_between(before, after)


def changes_for_step(step) -> dict[str, str]:
    """The listing for a web step or exercise, keyed by file path. Empty when nothing changes."""
    _prefix, identifier = step.web_build
    if isinstance(identifier, str) and identifier.startswith("ex:"):
        return exercise_listing(step)
    return lesson_step_listing(step)
