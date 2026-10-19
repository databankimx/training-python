"""
Build a step or an exercise of the web applications project, seed it with data, and check it.

Each lesson step's folder holds only the files that step adds or changes. This script copies every earlier step, in
order, plus the steps of the chosen chapter up to and including the step you name, into a build folder.

An exercise in try-it-yourself is either a full project, or an update to another exercise. An update names the
exercise it builds on in a builds_on.txt file. The script copies the chain of exercises, base first, into a build folder.

Then the script:

1. checks the project (manage.py check),
2. creates the database (manage.py migrate),
3. creates the admin account, if the runner gave one through the environment,
4. loads the seed data for a lesson step (the most recent seed.json up to this step; exercises have none),
5. runs the tests,
6. prints the step's check.txt, which says what to look for,
7. starts the development server, if --run is given.

The admin account is read from the environment variables STUDENT_ADMIN_USERNAME and STUDENT_ADMIN_PASSWORD.
They are passed to Django for that one build only. They are never printed.

Usage (from this folder):
    python build_stage.py --list
    python build_stage.py ch18 1
    python build_stage.py ch18 1 --run               (also starts the development server)
    python build_stage.py ch18 ex:18-6-pizzeria-home-page --run
"""

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUILD_ROOT = ROOT / "build"

CHAPTER_FOLDER = re.compile(r"^ch(\d\d)-")
STEP_FOLDER = re.compile(r"^(\d\d)-")
EXERCISE_PREFIX = "ex:"

# Items in a folder that describe the lesson or the build rather than the project. They are never copied.
SKIPPED_NAMES = {"lesson.md", "lesson-images", "__pycache__", "seed.json", "check.txt", "start.txt",
                 "builds_on.txt"}

ADMIN_USERNAME_VARIABLE = "STUDENT_ADMIN_USERNAME"
ADMIN_PASSWORD_VARIABLE = "STUDENT_ADMIN_PASSWORD"


def chapter_folders() -> list[Path]:
    """Chapter folders in order, such as ch18-getting-started-with-django."""
    return sorted(
        (p for p in ROOT.iterdir() if p.is_dir() and CHAPTER_FOLDER.match(p.name)),
        key=lambda p: p.name,
    )


def step_folders(chapter: Path) -> list[Path]:
    """Numbered step folders inside one chapter's lessons folder, in order."""
    lessons = chapter / "lessons"
    if not lessons.is_dir():
        return []
    steps = [p for p in lessons.iterdir() if p.is_dir() and STEP_FOLDER.match(p.name)]
    return sorted(steps, key=lambda p: p.name)


def find_chapter(name: str) -> Path:
    """Find a chapter folder by its prefix, such as ch18."""
    for chapter in chapter_folders():
        if chapter.name.startswith(name):
            return chapter
    raise SystemExit(f"No chapter folder starts with {name!r}.")


def copy_folder(source: Path, target: Path) -> None:
    """Copy one folder's project files into the build folder. Later copies overwrite earlier ones."""
    for item in source.iterdir():
        if item.name in SKIPPED_NAMES:
            continue
        destination = target / item.name
        if item.is_dir():
            shutil.copytree(item, destination, dirs_exist_ok=True,
                            ignore=shutil.ignore_patterns("__pycache__", "lesson-images"))
        else:
            shutil.copy2(item, destination)


def fresh_build_folder(name: str) -> Path:
    """An empty build folder with the given name."""
    target = BUILD_ROOT / name
    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)
    return target


# Lesson steps ---------------------------------------------------------------

def build_sources(chapter: Path, step_number: int) -> list[Path]:
    """The step folders that make up the project after the given step, in order."""
    steps = step_folders(chapter)
    if not 1 <= step_number <= len(steps):
        raise SystemExit(f"{chapter.name} has steps 1 to {len(steps)}, not {step_number}.")

    sources: list[Path] = []
    for earlier in chapter_folders():
        if earlier == chapter:
            break
        # Optional steps (folder names ending in -optional) are not carried into later chapters.
        sources.extend(p for p in step_folders(earlier) if not p.name.endswith("-optional"))
    sources.extend(steps[:step_number])
    return sources


def build_step(chapter: Path, step_number: int) -> tuple[Path, list[Path]]:
    """Build the project as it stands after a lesson step. Returns the build folder and its source steps."""
    sources = build_sources(chapter, step_number)
    target = fresh_build_folder(f"{chapter.name}-step-{step_number:02d}")
    for step in sources:
        copy_folder(step, target)
    print(f"Built {target}")
    return target, sources


def latest_seed(sources: list[Path]) -> Path | None:
    """The most recent seed.json among the source steps. Each seed holds the full data for its step."""
    for step in reversed(sources):
        seed = step / "seed.json"
        if seed.is_file():
            return seed
    return None


# Exercises ------------------------------------------------------------------

def try_it_yourself(chapter: Path) -> Path:
    """The try-it-yourself folder of a chapter."""
    return chapter / "try-it-yourself"


def exercise_chain(chapter: Path, name: str, seen: set[str] | None = None) -> list[Path]:
    """The folders needed to build this exercise, base first, ending with the exercise itself.

    builds_on.txt can name another exercise ("19-2-blog-accounts") or a lesson step ("step:ch20/5"). A lesson step
    brings in every lesson step up to it, as a lesson build does.
    """
    seen = seen or set()
    if name in seen:
        raise SystemExit(f"The exercises build on each other in a loop: {name}.")
    seen.add(name)

    folder = try_it_yourself(chapter) / name
    if not folder.is_dir():
        raise SystemExit(f"No exercise folder called {name!r} in {try_it_yourself(chapter)}.")

    builds_on = folder / "builds_on.txt"
    if not builds_on.is_file():
        return [folder]
    base = builds_on.read_text(encoding="utf-8").strip()
    if base.startswith("step:"):
        base_prefix, base_number = base[len("step:"):].split("/")
        base_chapter = find_chapter(base_prefix)
        return build_sources(base_chapter, int(base_number)) + [folder]
    if "/" in base:
        # An exercise in another chapter, written as chapter/exercise, such as ch19/19-5-protected-blog.
        base_prefix, base_name = base.split("/", 1)
        return exercise_chain(find_chapter(base_prefix), base_name, seen) + [folder]
    return exercise_chain(chapter, base, seen) + [folder]


def build_exercise(chapter: Path, name: str) -> tuple[Path, list[Path]]:
    """Build an exercise, starting from its base project. Returns the build folder and the folders used."""
    chain = exercise_chain(chapter, name)
    target = fresh_build_folder(f"{chapter.name}-exercise-{name}")
    for folder in chain:
        copy_folder(folder, target)
    print(f"Built {target}, from {' then '.join(folder.name for folder in chain)}")
    return target, chain


# Running --------------------------------------------------------------------

def run_django(target: Path, *args: str, extra_env: dict[str, str] | None = None) -> int:
    """Run a manage.py command in the build folder, and show its output."""
    env = os.environ.copy()
    if extra_env:
        env.update(extra_env)
    result = subprocess.run([sys.executable, "manage.py", *args], cwd=target, env=env, check=False)
    return result.returncode


def create_admin_account(target: Path) -> None:
    """Create the admin account from the environment, without asking any questions."""
    username = os.environ.get(ADMIN_USERNAME_VARIABLE)
    password = os.environ.get(ADMIN_PASSWORD_VARIABLE)
    if not username or not password:
        print("No admin account was given, so none was created.")
        return

    # Django reads these variables when --noinput is used. The password never appears on the command line.
    # The user model requires an email address even when --noinput is used, so a placeholder is supplied.
    extra_env = {
        "DJANGO_SUPERUSER_USERNAME": username,
        "DJANGO_SUPERUSER_PASSWORD": password,
        "DJANGO_SUPERUSER_EMAIL": f"{username}@example.com",
    }
    print("\nCreating the admin account...")
    if run_django(target, "createsuperuser", "--noinput", extra_env=extra_env) != 0:
        raise SystemExit("The admin account could not be created.")


def load_seed(target: Path, seed: Path | None) -> None:
    """Load the step's seed data, so the database holds what the step's check.txt describes.

    Some sample data belongs to the admin account (user 1). If no admin account was created, the data can't be loaded
    yet, so the build says how to finish the job by hand.
    """
    if seed is None:
        print("\nNo seed data for this step.")
        return

    shutil.copy2(seed, target / "seed.json")
    admin_given = bool(os.environ.get(ADMIN_USERNAME_VARIABLE))
    if '"owner"' in seed.read_text(encoding="utf-8") and not admin_given:
        print("\nThe sample data belongs to an admin account, and no admin account was created by this build.")
        print("To finish, open a terminal in the build folder, and run:")
        print("    python manage.py createsuperuser")
        print("    python manage.py loaddata seed.json")
        return

    print("\nLoading the seed data...")
    if run_django(target, "loaddata", "seed.json") != 0:
        raise SystemExit("The seed data could not be loaded.")


def show_check_file(chapter: Path, step_number: int) -> None:
    """Print what to look for in this step, from the step's check.txt."""
    step = step_folders(chapter)[step_number - 1]
    check = step / "check.txt"
    if not check.is_file():
        return
    print("\n" + "=" * 60)
    print("WHAT TO CHECK")
    print("=" * 60)
    print(check.read_text(encoding="utf-8").rstrip())
    print("=" * 60)


def list_steps() -> None:
    """Show every chapter, its steps, and its try-it-yourself exercises."""
    for chapter in chapter_folders():
        print(chapter.name)
        for step in step_folders(chapter):
            print(f"  {step.name}")
        tiy = try_it_yourself(chapter)
        if tiy.is_dir():
            for exercise in sorted(p for p in tiy.iterdir() if p.is_dir()):
                print(f"  try-it-yourself: {exercise.name}")


def check_and_test(target: Path) -> None:
    """Check the project, create its database, create the admin account, and run the tests."""
    print("\nChecking the project (manage.py check)...")
    if run_django(target, "check") != 0:
        raise SystemExit("The check failed. Fix the errors above before going on.")

    print("\nCreating the database (manage.py migrate)...")
    if run_django(target, "migrate") != 0:
        raise SystemExit("The database could not be created. Fix the errors above before going on.")

    create_admin_account(target)


def main(argv: list[str]) -> None:
    """Parse the command line, build the step or exercise, and check it."""
    if argv == ["--list"]:
        list_steps()
        return

    run = "--run" in argv
    args = [a for a in argv if a != "--run"]
    if len(args) != 2:
        raise SystemExit(__doc__)

    chapter = find_chapter(args[0])

    if args[1].startswith(EXERCISE_PREFIX):
        target, chain = build_exercise(chapter, args[1][len(EXERCISE_PREFIX):])
        check_and_test(target)
        load_seed(target, latest_seed(chain))
    else:
        try:
            step_number = int(args[1])
        except ValueError as exc:
            raise SystemExit(f"The step must be a number or ex:<exercise>, not {args[1]!r}.") from exc
        target, sources = build_step(chapter, step_number)
        check_and_test(target)
        load_seed(target, latest_seed(sources))

    print("\nRunning the tests (manage.py test)...")
    if run_django(target, "test") != 0:
        raise SystemExit("A test failed. Fix the errors above before going on.")

    if not args[1].startswith(EXERCISE_PREFIX):
        show_check_file(chapter, int(args[1]))

    if run:
        print("\nStarting the development server. Press Ctrl+C to stop it.")
        run_django(target, "runserver")


if __name__ == "__main__":
    main(sys.argv[1:])
