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

from .stages import StageInfo, chapter_folders, load_chapter

REPO_ROOT = Path(__file__).resolve().parents[2]

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

# The Part III chapter that is built and run like a web chapter.
FLASK_FOLDER = "s25-flask-learning-log"

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
    note: str = ""
    stage: StageInfo | None = None
    # For a web applications step: the chapter prefix and step number that build_stage.py takes, such as ("ch18", 5).
    web_build: tuple[str, int | str] | None = None

    @property
    def runnable(self) -> bool:
        """True when Run is available for this step."""
        return self.kind in ("script", "stage", "exercise", "web")


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


def natural_key(text: str) -> list[int | str]:
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


PLACEHOLDER_NOTE = (
    "# Not yet implemented\n\n"
    "{name} is not yet implemented. Its material hasn't been moved into this training repo yet, "
    "so there are no lessons or code to show here.\n"
)

EDITION = re.compile(r"^(\d+)(st|nd|rd|th)-edition$")


def placeholder_chapter(name: str, folder: Path) -> Chapter:
    """A chapter that is not migrated yet: one step that explains this."""
    step = Step(title="Not yet implemented", number=None, kind="lesson", lesson_md=None,
                code_path=None, note=PLACEHOLDER_NOTE.format(name=name))
    return Chapter(name=name, folder=folder, steps=[step])


def edition_title(folder_name: str) -> str:
    """'2nd-edition' -> '2nd Edition'."""
    match = EDITION.match(folder_name)
    return f"{match.group(1)}{match.group(2)} Edition" if match else prettify(folder_name)


def part_two_chapter(chapter_folder: Path) -> Chapter | None:
    """One Part II chapter: its lesson sub-folders, then Try it Yourself.

    Lesson sub-folders become child nodes, as in Part III. Try-it-yourself scripts are shown
    as in Part I: the answers file is the lesson text for them, not a step of its own.
    """
    node = Chapter(name=pretty_folder(chapter_folder.name), folder=chapter_folder, steps=[])
    lessons = chapter_folder / "lessons"
    if lessons.is_dir():
        node.steps = folder_steps(lessons, include_lessons=False)
        if node.steps:
            node.intro_md = intro_for(lessons)
        for sub in sorted((p for p in lessons.iterdir() if p.is_dir()), key=lambda p: natural_key(p.name)):
            steps = folder_steps(sub, include_lessons=False)
            if steps:
                node.children.append(Chapter(name=tidy_name(sub.name), folder=sub, steps=steps,
                                             intro_md=intro_for(sub)))
    tiy = chapter_folder / "try-it-yourself"
    if tiy.is_dir():
        steps = folder_steps(tiy, include_lessons=False)
        if steps:
            node.children.append(Chapter(name=TRY_IT_NAME, folder=tiy, steps=steps,
                                         intro_md=intro_for(tiy)))
    return node if node.steps or node.children else None


def data_visualization_chapter(folder: Path) -> Chapter:
    """Data Visualization: one group per edition, each holding its chapters."""
    node = Chapter(name="Data Visualization", folder=folder, steps=[])
    setup_md = folder / "github-token-setup.md"
    if setup_md.exists():
        setup_step = Step(title=step_title("github-token-setup", setup_md), number=None, kind="lesson",
                          lesson_md=setup_md, code_path=None)
        node.children.append(Chapter(name="Setup", folder=folder, steps=[setup_step]))
    editions = (p for p in folder.iterdir() if p.is_dir() and p.name.endswith("-edition"))
    for edition in sorted(editions, key=lambda p: natural_key(p.name)):
        group = Chapter(name=edition_title(edition.name), folder=edition, steps=[])
        chapters = (p for p in edition.iterdir() if p.is_dir() and p.name.startswith("ch"))
        for chapter_folder in sorted(chapters, key=lambda p: natural_key(p.name)):
            chapter = part_two_chapter(chapter_folder)
            if chapter is not None:
                group.children.append(chapter)
        if group.children:
            node.children.append(group)
    return node


def exercise_steps(folder: Path) -> list[Step]:
    """One step per exercise folder. Each exercise runs its own script, the one with the main check."""
    steps: list[Step] = []
    exercises = sorted((p for p in folder.iterdir() if p.is_dir()), key=lambda p: natural_key(p.name))
    for exercise in exercises:
        md = exercise / "lesson.md"
        lesson_md = md if md.exists() else None
        code = None
        for script in sorted(exercise.glob("*.py")):
            try:
                if GUARD.search(script.read_text(encoding="utf-8")):
                    code = script
                    break
            except (OSError, UnicodeDecodeError):
                continue
        steps.append(Step(title=step_title(exercise.name, lesson_md), number=None,
                          kind="exercise" if code else "lesson", lesson_md=lesson_md, code_path=code))
    return steps


def making_a_game_chapter(folder: Path) -> Chapter:
    """Making a Game: the Alien Invasion chapters, each step a stage that can be built and run."""
    project = folder / "alien-invasion"
    node = Chapter(name="Making a Game", folder=folder, steps=[])
    if not project.is_dir():
        return placeholder_chapter("Making a Game", folder)
    for chapter_folder in chapter_folders(project):
        chapter = Chapter(name=pretty_folder(chapter_folder.name), folder=chapter_folder, steps=[])
        for stage in load_chapter(chapter_folder):
            title = step_title(stage.folder.name, stage.lesson_md)
            main = stage.folder / "alien_invasion.py"
            chapter.steps.append(Step(title=title, number=stage.number, kind="stage",
                                      lesson_md=stage.lesson_md, code_path=main, stage=stage))
        tiy = chapter_folder / "try-it-yourself"
        if tiy.is_dir():
            chapter.children.append(Chapter(name=TRY_IT_NAME, folder=tiy, steps=exercise_steps(tiy),
                                            intro_md=intro_for(tiy)))
        node.children.append(chapter)
    return node


def web_exercise_steps(folder: Path, prefix: str) -> list[Step]:
    """One step per try-it-yourself exercise. A project or an update runs; a text-only exercise is read as a lesson."""
    steps: list[Step] = []
    exercises = sorted((p for p in folder.iterdir() if p.is_dir()), key=lambda p: natural_key(p.name))
    for exercise in exercises:
        md = exercise / "lesson.md"
        lesson_md = md if md.exists() else None
        runnable = (exercise / "manage.py").exists() or (exercise / "builds_on.txt").exists()
        steps.append(Step(title=step_title(exercise.name, lesson_md), number=None,
                          kind="web" if runnable else "lesson", lesson_md=lesson_md, code_path=None,
                          web_build=(prefix, f"ex:{exercise.name}") if runnable else None))
    return steps


def web_chapter(chapter_folder: Path) -> Chapter:
    """One web-style chapter: its lesson steps are built and run, and its Try it Yourself folder holds the exercises."""
    prefix = chapter_folder.name.split("-")[0]
    chapter = Chapter(name=pretty_folder(chapter_folder.name), folder=chapter_folder, steps=[])
    lessons = chapter_folder / "lessons"
    base = lessons if lessons.is_dir() and any(re.match(r"^\d\d-", p.name) for p in lessons.iterdir() if p.is_dir()) else chapter_folder
    step_folders = sorted((p for p in base.iterdir() if p.is_dir() and re.match(r"^\d\d-", p.name)), key=lambda p: natural_key(p.name))
    for step_folder in step_folders:
        md = step_folder / "lesson.md"
        lesson_md = md if md.exists() else None
        number = int(step_folder.name[:2])
        chapter.steps.append(Step(title=step_title(step_folder.name, lesson_md), number=number,
                                  kind="web", lesson_md=lesson_md, code_path=None,
                                  web_build=(prefix, number)))
    tiy = chapter_folder / "try-it-yourself"
    if tiy.is_dir():
        chapter.children.append(Chapter(name=TRY_IT_NAME, folder=tiy,
                                        steps=web_exercise_steps(tiy, prefix)))
    return chapter


def web_applications_chapter(folder: Path) -> Chapter:
    """Web Applications: each step is built and run with build_stage.py, and its server stays running."""
    chapters = sorted((p for p in folder.iterdir() if p.is_dir() and CHAPTER_FOLDER.match(p.name))
                      if folder.is_dir() else [], key=lambda p: natural_key(p.name))
    if not chapters:
        return placeholder_chapter("Web Applications", folder)

    node = Chapter(name="Web Applications", folder=folder, steps=[])
    for chapter_folder in chapters:
        prefix = chapter_folder.name.split("-")[0]
        chapter = Chapter(name=pretty_folder(chapter_folder.name), folder=chapter_folder, steps=[])
        lessons = chapter_folder / "lessons"
        step_folders = sorted((p for p in lessons.iterdir() if p.is_dir() and re.match(r"^\d\d-", p.name))
                              if lessons.is_dir() else [], key=lambda p: natural_key(p.name))
        for step_folder in step_folders:
            md = step_folder / "lesson.md"
            lesson_md = md if md.exists() else None
            number = int(step_folder.name[:2])
            chapter.steps.append(Step(title=step_title(step_folder.name, lesson_md), number=number,
                                      kind="web", lesson_md=lesson_md, code_path=None,
                                      web_build=(prefix, number)))
        tiy = chapter_folder / "try-it-yourself"
        if tiy.is_dir():
            chapter.children.append(Chapter(name=TRY_IT_NAME, folder=tiy,
                                            steps=web_exercise_steps(tiy, prefix)))
        node.children.append(chapter)
    return node


def part_two_scope() -> Scope:
    """Part II: Making a Game, Data Visualization, and the Web Applications placeholder."""
    root = REPO_ROOT / "part-ii-projects"
    return Scope(name="Part II - Projects", chapters=[
        making_a_game_chapter(root / "making-a-game"),
        data_visualization_chapter(root / "data-visualization"),
        web_applications_chapter(root / "web-applications"),
    ])


def discover() -> list[Scope]:
    """Return the Part I, Part II and Part III scopes with their chapters and steps."""
    scopes: list[Scope] = []
    for scope_name, root, include_lessons in SCOPES:
        steps_by_folder: dict[Path, list[Step]] = {}
        for folder in [root] + [p for p in root.rglob("*") if p.is_dir()]:
            if folder == root:
                continue
            if any(part in SKIP_DIRS for part in folder.relative_to(root).parts):
                continue
            if include_lessons and folder.relative_to(root).parts[0] == FLASK_FOLDER:
                # The Flask chapter is built as a web chapter, below, not as loose lesson files.
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
    scopes.insert(1, part_two_scope())
    flask = REPO_ROOT / "part-iii-beyond-the-book" / FLASK_FOLDER
    if flask.is_dir():
        part_three = next(scope for scope in scopes if scope.name == "Part III - Beyond the Book")
        part_three.chapters.append(web_chapter(flask))
        part_three.chapters.sort(key=lambda chapter: natural_key(chapter.folder.name))
    return scopes
