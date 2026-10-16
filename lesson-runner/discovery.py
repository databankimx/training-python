"""Discover chapters and steps in the Python training repo.

Part I: each chapter folder (for example ch02-fundamentals) is a tree node. Its
``lessons`` folder holds the chapter's steps, so those steps belong to the
chapter node itself. Subfolders of ``lessons`` (such as the chapter 11 editions)
become child nodes, and so does ``try-it-yourself``. A try-it folder that sits
under an edition (``try-it-yourself/2nd Edition (unittest)``) is nested under
that edition's node.

Part III: a chapter is a folder with any lesson files. Every lesson file (.md)
is a step, in file-name order. The step's code comes from the matching script
(.py) when there is one. A lesson with no script gets a placeholder. A C code
sample (.c) with the same name is shown as read-only code, because the runner
cannot run it.

A Python script is a step when its name is numbered (``01_command_args.py``),
it is ``main.py``, or it has an ``if __name__ == "__main__":`` guard. Support
modules such as ``utilities.py`` and ``trie.py`` are not steps.
"""
#pylint: disable=line-too-long

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

TRY_IT_NAME = "Try it Yourself"

# Steps hidden from the menu, as "folder/stem". These are helper scripts, not lesson steps:
# S10's main.py is the chapter's runner, S12's prep_tables.py only sets up the tables,
# S17's login.py is a shared connection helper, and S18's main.py is the interactive dictionary.
HIDDEN_STEPS = {
    "s10-web-scraping/main",
    "s12-mysql-databases/prep_tables",
    "s17-mongodb/login",
    "s18-trie/main",
}

GUARD = re.compile(r"""if\s+__name__\s*==\s*["']__main__["']""")
NUMBERED = re.compile(r"^\d")
HEADING = re.compile(r"^#{1,3}\s+(.+?)\s*$", re.MULTILINE) #NOSONAR
CHAPTER_FOLDER = re.compile(r"^(ch|s)(\d+)[-_]?(.*)$", re.IGNORECASE) #NOSONAR


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
    indented: bool = False

    @property
    def runnable(self) -> bool:
        """True when Run is available for this step."""
        return self.kind == "script"


@dataclass
class Chapter:
    """A folder of steps, shown as one entry in the chapter tree.

    In Part I, a chapter can have child nodes (Try it Yourself, editions).
    """
    name: str
    folder: Path
    steps: list[Step]
    intro_md: Path | None = None
    children: list[Chapter] = field(default_factory=list)


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
    text = re.sub(r"\s+#+\s*$", "", text) #NOSONAR
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
    """Turn a file stem such as '01_command_args' or '06a_importing_a_class' into 'Command args'."""
    text = re.sub(r"^\d+(?:[a-z](?=_))?[_\s-]*", "", stem)
    text = text.replace("_", " ").replace("-", " ").strip()
    if not text:
        text = stem
    return text[:1].upper() + text[1:]


def strip_order(name: str) -> str:
    """Drop a leading order number and dash, for example '00 - Both Editions' -> 'Both Editions'."""
    return re.sub(r"^\d+\s*-\s*", "", name)


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


def shared_lesson_for(stem: str, lessons: dict[str, Path]) -> Path | None:
    """A lesson shared by several scripts, such as 06_importing_classes.md for 06a, 06b and 06c."""
    match = re.match(r"^(\d+)[a-z]_", stem)
    if not match:
        return None
    candidates = [md for name, md in lessons.items() if name.startswith(match.group(1) + "_")]
    return candidates[0] if len(candidates) == 1 else None


def folder_steps(folder: Path, include_lessons: bool) -> list[Step]:
    """All steps in one folder, in file-name order."""
    lessons = {p.stem: p for p in folder.glob("*.md")}
    scripts = {p.stem: p for p in folder.glob("*.py") if is_step(p) or p.stem in lessons}
    samples = {p.stem: p for p in folder.glob("*.c")} if include_lessons else {}

    # Part I: lesson files are only attached to their scripts. Part III: lesson files are steps too.
    stems = set(scripts) | set(samples) | (set(lessons) if include_lessons else {s for s in lessons if "bonus" in s})
    stems = sorted(stems, key=natural_key)
    stems = [stem for stem in stems if f"{folder.name}/{stem}" not in HIDDEN_STEPS]
    steps: list[Step] = []
    for stem in stems:
        own_md = lessons.get(stem)
        lesson_md = own_md or shared_lesson_for(stem, lessons)
        if stem in scripts:
            steps.append(Step(title=step_title(stem, own_md), number=number_of(stem),
                              kind="script", lesson_md=lesson_md, code_path=scripts[stem]))
        elif stem in samples:
            steps.append(Step(title=step_title(stem, own_md), number=number_of(stem),
                              kind="source", lesson_md=lesson_md, code_path=samples[stem]))
        else:
            steps.append(Step(title=step_title(stem, own_md), number=number_of(stem),
                              kind="lesson", lesson_md=lesson_md, code_path=None))
    seen: set[Path] = set()
    for step in steps:
        # Steps that reuse a lesson file another step already uses are indented under the first one.
        if step.lesson_md is not None:
            step.indented = step.lesson_md in seen
            seen.add(step.lesson_md)
    return steps


def intro_for(folder: Path) -> Path | None:
    """Pick the chapter-level Markdown: 00_intro.md if present, else the first .md."""
    candidates = sorted(folder.glob("*.md"))
    for md in candidates:
        if "intro" in md.stem.lower():
            return md
    return candidates[0] if candidates else None


def child_named(parent: Chapter, name: str, folder: Path) -> Chapter:
    """The child node with this name, created if it doesn't exist yet."""
    for child in parent.children:
        if child.name == name:
            return child
    child = Chapter(name=name, folder=folder, steps=[])
    parent.children.append(child)
    return child


def sort_children(node: Chapter) -> None:
    """Order child nodes naturally, with Try it Yourself last among its siblings."""
    node.children.sort(key=lambda c: (c.name == TRY_IT_NAME, natural_key(c.folder.as_posix())))
    for child in node.children:
        sort_children(child)


def part_one_tree(root: Path, steps_by_folder: dict[Path, list[Step]]) -> list[Chapter]:
    """Build the Part I tree: chapter nodes, with editions and Try it Yourself as children."""
    chapters: dict[Path, Chapter] = {}
    ordered = sorted(steps_by_folder, key=lambda f: natural_key(f.relative_to(root).as_posix()))
    for folder in ordered:
        relative = folder.relative_to(root).parts
        chapter_folder = root / relative[0]
        if chapter_folder not in chapters:
            chapters[chapter_folder] = Chapter(name=pretty_folder(relative[0]), folder=chapter_folder,
                                               steps=[])
        chapter = chapters[chapter_folder]
        sub = relative[1:]
        steps = steps_by_folder[folder]

        if not sub or sub == ("lessons",):
            chapter.steps = steps
            chapter.intro_md = intro_for(folder)
        elif sub[0] == "lessons":
            node = child_named(chapter, strip_order(" / ".join(sub[1:])), folder)
            node.folder, node.steps, node.intro_md = folder, steps, intro_for(folder)
        elif sub[0].startswith("try"):
            if len(sub) == 1:
                owner = chapter
            else:
                # An edition's try-it folder nests under that edition's node.
                owner = child_named(chapter, " / ".join(sub[1:]), chapter.folder / "lessons" / sub[1])
            node = child_named(owner, TRY_IT_NAME, folder)
            node.folder, node.steps, node.intro_md = folder, steps, intro_for(folder)
        else:
            node = child_named(chapter, " / ".join(sub), folder)
            node.folder, node.steps, node.intro_md = folder, steps, intro_for(folder)

    for chapter in chapters.values():
        sort_children(chapter)
    return list(chapters.values())


def tidy_name(name: str) -> str:
    """A display name for a sub-folder: '02a-distribution-types' -> 'Distribution types'."""
    text = re.sub(r"^\d+[a-z]?[-_\s]+", "", name)
    text = text.replace("-", " ").replace("_", " ").strip()
    return text[:1].upper() + text[1:] if text else name


def part_three_tree(root: Path, steps_by_folder: dict[Path, list[Step]]) -> list[Chapter]:
    """Build the Part III tree: each chapter folder's sub-folders become nested nodes."""
    chapters: dict[Path, Chapter] = {}
    ordered = sorted(steps_by_folder, key=lambda f: natural_key(f.relative_to(root).as_posix()))
    for folder in ordered:
        parts = folder.relative_to(root).parts
        top = root / parts[0]
        if top not in chapters:
            chapters[top] = Chapter(name=pretty_folder(parts[0]), folder=top, steps=[])
        node = chapters[top]
        for depth in range(1, len(parts)):
            node = child_named(node, tidy_name(parts[depth]), root.joinpath(*parts[:depth + 1]))
        node.folder, node.steps, node.intro_md = folder, steps_by_folder[folder], intro_for(folder)

    for chapter in chapters.values():
        sort_children(chapter)
    return list(chapters.values())


def discover() -> list[Scope]:
    """Return the Part I and Part III scopes with their chapters and steps."""
    scopes: list[Scope] = []
    for scope_name, root, include_lessons in SCOPES:
        steps_by_folder: dict[Path, list[Step]] = {}
        for folder in [root] + [p for p in root.rglob("*") if p.is_dir()]:
            if folder == root:
                continue
            if any(part in SKIP_DIRS for part in folder.relative_to(root).parts):
                continue
            steps = folder_steps(folder, include_lessons)
            if steps:
                steps_by_folder[folder] = steps

        scope = Scope(name=scope_name)
        if include_lessons:
            scope.chapters = part_three_tree(root, steps_by_folder)
        else:
            scope.chapters = part_one_tree(root, steps_by_folder)
        scopes.append(scope)
    return scopes
