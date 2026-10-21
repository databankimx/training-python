# Resume: Python Training Solution

This file is for picking up work after a restart. It records where things stand, what was decided, and what's next.
Read this first, then the lesson pages for the chapter you're working on.

## Locations

- **Solution root:** `C:\Development\training\training-python`
- **Source material (do not edit):** `C:\Development\training\python-crash-course`
- **Part I:** `part-i-basics`
- **Part II, Making a Game:** `part-ii-projects\making-a-game\alien-invasion`
- **Part II, Data Visualization:** `part-ii-projects\data-visualization`
- **Part II, Web Applications:** `part-ii-projects\web-applications`
- **Part III:** `part-iii-beyond-the-book`
- **Lesson runner:** `lesson-runner` (PySide6 app, run with `python app.py`)
- **Quickstart:** `QUICKSTART.md` at the solution root. It walks through every setup step, and includes troubleshooting. Keep it in step with any setup change.
- **Setup script:** `setup.ps1` at the solution root. It runs quickstart steps 2 to 7 in order, and skips anything already in place. Keep it in step with the quickstart.
- **Editor settings copy for students:** `resources\vscode\settings.json`

## Conventions

- US English only: color, center, maximize, lowercase, behavior, favorite. Check every new sentence.
- Voice: write like the author. Wry humor, a bit self-deprecating, conversational rather than didactic. Keep it light, but never at the
  learner's expense.

- US English throughout: color, center, maximize, lowercase.
- Documentation: use hyphens, not em dashes. Avoid emojis.
- Pylint and NOSONAR comments stay in the code file. Lessons mention them only in a note saying the code file turns them off. This includes code blocks: lesson and TIY `.md` code blocks never show a Pylint or NOSONAR comment.
- Pylance hover docstrings render as Markdown. Escape square brackets (`\[a\]dd`). Google-style `Args:` and `Returns:` sections are used for function docs.
- Lessons don't refer to the textbook. Book topics we're missing are paraphrased in our own words. Exception: Chapter 10's relative-path lesson keeps the 2nd and 3rd edition names, because the two editions use different methods.
- Exercise prompts are never paraphrased. Use the book's prompt text as written, with formatting changes only (for example, code in backticks). Where the code's names or minor values differ from the prompt (for example, method names or a message string), that's the author's implementation and is fine. Don't add notes about those differences.
- Lessons whose names start with "bonus" were written by the author, not taken from the book. For those, skip the book-coverage check and review for accuracy and voice only.
- Each step with a pause helper (`pause()` from `sm_utils`) gets a note saying the code file pauses between sections.
- Review workflow: one file at a time. Report findings, wait for approval, then edit. A user reply of "ok" means ready for the next file.
- No status sections in any README. READMEs describe the content only.
- Lessons: web chapters use a "For dummies" section, then runner steps where relevant, then the code, then testing, output and changed files.
  Part I lessons don't use that layout. Part I reviews check three things: does the textbook cover anything we left out, are there errors, and is it in the author's voice.
  Lessons should be complete, correct, and conversational.
  Screenshot placeholders go in the Output section, in a `lesson-images` folder inside the step or exercise.
- MD lesson files always end with a horizontal rule (`---`).
- When a method's trailing `\n` is removed, add a `print()` after each call to that method, in both the `.md` and `.py`, and add the matching blank line to the outputs.
- The exercise heading `print()` in every lesson `.py` ends with `\n`, so there's always a blank line after it. For example: `print("Exercise 4 - Overriding Parent Class Methods\n")`.
- This file is the bible for picking up in a new chat. Claude may update it whenever something changes.
- Step folders hold only the files that step adds or changes. The build copies every earlier step, in order.
- Seed data is a `seed.json` in a step folder. The build loads the most recent seed up to the step.
- `check.txt` says what to look for; `start.txt` names the page the browser opens first.
- Exercises that are projects or updates have `builds_on.txt`. It names another exercise (`19-2-blog-accounts`), an exercise in another
  chapter (`ch19/19-5-protected-blog`), or a lesson step (`step:ch20/5`).
- Exercises that only change code are lessons, with the code shown in the lesson (19-3, 19-4, 20-1).
- Numbered screenshots (`01-...png` and so on) in any `lesson-images` folder are ignored by git. Only the lesson's own pictures are committed.
- Textbook downloads are copied unchanged into `textbook-downloads`, in `2nd-edition/lessons`, `3rd-edition/lessons` and
  `3rd-edition/try-it-yourself`. The book's own lesson text is not copied.
- The `build` folders and `.venv` folders are not committed. `.vscode` is not tracked in git.
- The web applications virtual environment is `part-ii-projects\web-applications\.venv`. The runner uses it. A `.ll_venv` folder was
  created by mistake and is not used.
- Do not write into `C:\Development\training\python-crash-course`. Check any path before writing.
- Django 5.2.17 (latest long-term support release). `django-bootstrap5` 26.4.

## Web Applications (Learning Log)

### Chapter 18: complete
- Lesson steps 1 to 9, all screenshots in place, tests passed in the runner.
- Exercises: 18-1, 18-2, 18-3, 18-7 are lessons. 18-4 Pizzeria and 18-5 Meal Planner are full projects. 18-6 and 18-8 are updates.
- Textbook downloads copied.

### Chapter 19: complete (User Accounts)
- Lesson steps 1 to 5 (accounts, ownership, restricting access, duplicate topics, deleting entries). Screenshots in place.
- Exercises: 19-1 Blog is a full project. 19-2 (accounts) and 19-5 (protected blog) are updates. 19-3 and 19-4 are lessons.
- Textbook downloads copied.

### Chapter 20: complete (Styling and Deploying)
- Lesson steps 1 to 5: Bootstrap setup, navigation bar, styled pages, production settings, and the PythonAnywhere deployment lesson.
  Screenshots in place for steps 1 to 4, and the live pages in step 5.
- Exercises: 20-1 is a lesson. 20-2 Stylish Blog is an update to 19-5. 20-3 Live Blog is an update to 20-2, and its deployment is optional.
  20-4 Extended Learning Log is an update to lesson step ch20/5, adding public topics. All tested in the runner. Screenshots in place
  for 20-2 and 20-4.
- Textbook downloads copied.
- The PythonAnywhere deployment lesson (step 5) has not been dry-run by the author from start to finish. Its screen labels were checked
  against the author's own account where possible. Before students use it, do one full deployment and correct any wording that differs.

### Web applications README
- Updated for chapters 18 to 20, including the optional deployment note.

## Runner and build system

- `part-ii-projects\web-applications\build_stage.py` builds a lesson step (`ch18 5`) or an exercise (`ch18 ex:18-8-pizzeria-pages`) into `build\`.
  It creates the admin account from `STUDENT_ADMIN_USERNAME` and `STUDENT_ADMIN_PASSWORD` (no prompts), loads seed data, runs tests, prints
  `check.txt`, and with `--run` starts the server.
- If no admin account is given and the seed data belongs to one, the build copies the seed into the build folder and prints the commands to
  finish by hand, rather than failing.
- `requirements.txt` is copied into builds, so the lesson 05 upload includes it.
- The runner (`lesson-runner`) shows web chapters with the lesson steps and a **Try it Yourself** node. Run asks once per session for an admin
  username (lowercase letters and numbers) and password (at least 8 characters). It opens the browser at `start.txt` when the server is ready.
- Escape, selecting another step or chapter, or closing the window stops the run.
- Child processes are put in a Windows job object, so they end if the runner exits or crashes.
- Before a web run, if port 8000 is in use, the runner asks whether to stop the process using it.
- The Source tab shows read-only listings for web steps and exercises: new files in full, and changed files as diffs with `--snip--`.
  It catches build errors and shows them as text, rather than closing the app.

## Other areas

### Making a Game (Alien Invasion)
- Chapters 12, 13 and 14 are complete. The chapter 14 expanded game is in `ch14-scoring\try-it-yourself\14-7-expanding-the-game`.
- The `final` folder holds the book's finished game, with its own README.

### Data Visualization
- Complete as of earlier sessions.

### Part I
- Not changed in this work.

## Roadmap

- **Flask Learning Log (Part III, section s25):** a new section that builds the same Learning Log with Flask, because DataBank uses Flask.
  Same lessons, written for Flask. Decisions so far:
  - Flask 3.1.3, the latest stable release. Flask doesn't have long-term support releases.
  - Step-by-step with runner support, as in the Django chapter.
  - SQLAlchemy as the data layer. It works with SQLite, SQL Server and MySQL.
  - The lessons use SQLite. A later step switches to SQL Server or MySQL with a connection string, and the app is tested against each.
  - DataBank hosts both SQL Server and MySQL on AWS, and both are installed on the author's PC.
  - Still to decide: whether the runner offers the database as a choice, or the connection string is set in an environment variable.
  Not started.

## Flask chapter status (s25)

- Started. Folder: `part-iii-beyond-the-book\s25-flask-learning-log`. Step 1 requirements are in place (Flask 3.1.3, SQLAlchemy 2.0.52).
- Build design: a Flask project does not use `manage.py`. It has `flask_app.py` at its root, and build_stage.py runs Flask-specific
  commands for it: create the tables, create the admin account, load the seed, run the tests with unittest, and start `flask run` with a
  "Starting development server at" line, so the runner recognizes it.
- Build tree: build_stage.py must treat `s25` as its own track. A chapter only builds from earlier chapters in the same track, so the
  Flask chapter never pulls in the Django chapters.
- Discovery: the Part III scope must skip `s25` and add it as a web-style chapter (lessons, then Try it Yourself), as Web Applications does.
- Test runner: unittest, so no extra packages beyond Flask and SQLAlchemy.
- Done: build_stage.py has Flask support (`flask_app.py` marks a Flask project; init-db, create-admin, load-seed, unittest, and `flask run`
  with the Starting line). It has its own track for s25. The runner checks Flask and SQLAlchemy for s25, and Django for the other chapters.
  Discovery shows s25 in Part III as a web chapter, and skips its folders in the loose lesson scan.
- Venv: installed by the learner into `web-applications\.venv`, from `..\..\part-iii-beyond-the-book\s25-flask-learning-log\01-flask-setup\requirements.txt`.
- Step 1 is written: `01-flask-setup` (directly in the chapter folder) has the app factory, the database module, the entry point, three tests, the
  three build commands (init-db, create-admin placeholder, load-seed placeholder), the lesson, and check.txt. Ran in the runner: 3 tests OK,
  home page served.
- Layout: the Flask chapter has no `lessons` folder, since it has no sibling Try it Yourself or textbook folders. Its steps (`01-...`,
  `02-...`) sit directly in `s25-flask-learning-log`. The build and discovery find steps in `lessons` when it holds steps, and otherwise in the
  chapter folder itself. An empty `lessons` folder left behind is ignored, but can be deleted.
- Structure: one chapter folder (`s25`), with every step numbered, as in chapters 18 to 20. Not split into separate chapters.
- All planned steps are written and run in the runner: 1 to 13. The Flask chapter has no deployment step: it points to the Django deployment lesson
  (chapter 20, step 5).
- Database choice: step 14 (`14-database-choice`) is informational, with no code and no runner dialog. It explains the connection string for SQL Server
  and MySQL, the drivers, and keeping the string out of files. The chapter runs on SQLite by default. Students set `DATABASE_URL` in a PowerShell
  window, and run the build from that window, since the runner doesn't read it.

## Decided

- Flask chapter database: the learner provides a connection string. The runner asks once per session, like the admin account, keeps it in
  memory, and passes it to the build as an environment variable. There is no settings file and no editing: the learner sets it up once per
  session. Nothing is written to a file. The default is SQLite, so the lessons work without setup. The production connection on
  PythonAnywhere is set the same way, as an environment variable in the WSGI file. No separate parameter fields.

- Flask chapter scope: it stops at readiness for production (settings from environment variables, debug off, error pages, and the database
  connection). It doesn't include deployment. The chapter says the deployment process is the same as the Django chapter's PythonAnywhere lesson
  (chapter 20, step 5), and points there.

## Repository audit (in progress)

- Goal: a learner who never opens the book should get a solid path from the lesson files alone. Each chapter is checked against the book for
  (1) topics we haven't covered, (2) mistakes or inaccuracies, and (3) narrative gaps. Findings are discussed before changes are made.
- Decisions: Python 3.12 or later is required. Lessons stay Windows-focused, with a pointer to the book's appendix for macOS and Linux.
  Book topics we're missing are paraphrased into our lessons. We aren't reproducing the book.
- Part I, Chapter 1: done. Lessons updated (setup links, Python requirement, running from a terminal, the prompt, and the purpose of Hello World).
  Try It Yourself matched the book, so unchanged.
- Part I, Chapter 2: lessons 01 to 13 reviewed and revised (variables, input, strings, case, whitespace, escapes, stripping, prefixes, numbers,
  floats, rounding errors, underscores, multiple assignment, constants). Try It Yourself checked; 09 has a comment on integer division.
- Part I, Chapter 3 (lists): lessons 00 to 09 reviewed and revised, Try It Yourself reviewed and revised (10 is now a full sample program).
- Part I, Chapter 4 (using lists): lessons 01 to 11 reviewed and revised; Try It Yourself reviewed and revised.
- Part I, Chapter 5 (boolean logic): lessons 01 to 08 reviewed and revised; the boolean_logic_tester.html page now uses vanilla JavaScript and a NOT fix;
  Try It Yourself reviewed and revised.
- Part I, Chapter 6 (dictionaries): lessons 01 to 15 reviewed and revised; Try It Yourself reviewed, with outputs added for 6.2, 6.3, 6.4, 6.7, 6.9,
  6.10 and 6.11. 6.1 and 6.7 use made-up people, not Scott McLean.
- Part I, Chapter 7 (more functionality): lessons 01 to 11 reviewed and revised, including the primes folder (its files were re-zipped by the author).
  Try It Yourself reviewed and revised (exercise 7.6 has three versions; 7.10 uses the `== "n"` check).
- Part I, Chapter 8 (functions): lessons 01 to 16 reviewed and revised, including bonus lessons 15 (global variables) and 16 (mutable defaults). Try It Yourself reviewed and revised: prompts paraphrased, outputs match, names and docstrings match the code, and the 10_sending_messsages file was renamed to 10_sending_messages.py.
- Part I, Chapter 9 (classes): lessons 01 to 05 reviewed and revised. Lesson 01 has class methods (`from_string()`), not yet run. Lesson 02 retitled "Working with Attributes", and its code file now covers every example. Lesson 03 has the shared-code rule, the commented-out error line (line 67 of the code file), and the parent-availability rule (the parent must be defined earlier in the file or imported; tested both ways). Lesson 04 has the fuel overrides, `fuel_level` starts at 0.0, the trailing `\n` is removed with `print()` after each `check_fuel_level()` call, and the `#NOSONAR` note is added. Lesson 05 has the composition term, the where-does-the-method-belong discussion, `Battery` above `ElectricCar`, and matching `battery_range` names.
- Part I, Chapter 9, lesson 06 (importing classes): reviewed and revised. Module files (`car.py`, `electric_car.py`, `full_car.py`) updated to match: `fuel_level` starts at `0.0`, fuel docstrings corrected, trailing `\n` removed, `#NOSONAR` on `get_range()`, comment above `from car import Car`. Added `from module import *` section and a note that `upgrade_battery()` is for the battery exercise. 06a and 06b call `print()` after the car reads. 06b heading fixed to "Exercise 6-b". Traceback in 06 now names `06d_import_module.py`, line 13.
- Part I, Chapter 9, lesson 07 (importing from a library): reviewed and revised. Added the `random` security caveat (use `secrets`), "virtual environment" fix, and the output now matches the code (heading `\n`, leading and trailing `\n` removed).
- Part I, Chapter 9, lesson 08 (bonus properties): reviewed and revised. Name mangling explained (`_Human__first_name`), with a note that it isn't security. "Encapsulation" defined. Notes added for `clear_terminal()`/`pause()` and the `too-few-public-methods` disable. Class syntax matched to the code (`class Person:`). Heading is now "Bonus - Properties".
- Part I, Chapter 9, lesson 09 (bonus magic methods): reviewed and revised. Table fixed (`__init__`/`__new__` order, Python 2 methods removed, `__bool__` added, `//` and `/` corrected, typos). Code file adds `PlainPerson` so the "As is" output runs. Heading is now "Bonus - Magic (Dunder) Methods and Properties".
- Part I, Chapter 9 Try It Yourself: reviewed and revised. Prompts paraphrased and matched to the code's method names (`describe()`, `greet()`, `roll()`). The trailing and leading `\n` removed from methods, with `print()` at each call site. Outputs traced to the code. `02_three_restauants.py` renamed to `02_three_restaurants.py`. The `print(selected)` in 9.15 is commented out and explained. Module files updated to match (`is None`, "as" typo fixed, Pylint and NOSONAR comments kept).
- Part I, Chapter 10 (files and exceptions): bonus pre-lesson 00 and lesson 01 reviewed and revised. Edition references (2nd and 3rd) are kept in this chapter's reading lessons, since the methods differ. Lesson 01's `.py` separates each example with a blank line. Lesson 02 reviewed: encoding added to examples, the `readlines()` memory trade-off explained, and the heading corrected to "iterable" wording. Lesson 03 reviewed: generator-expression wording corrected, `l` renamed to `line` in both files, the slice note fixed (53 characters), and the larger-file sections tidied. Lesson 04 reviewed: encoding added to examples, sample input moved above the output, and the pi paragraph reflowed. Lesson 05 reviewed: encoding added to every call, the file-path sentence rewritten, the 3rd edition helper named `write_line_to_file()` in both files, docstrings added, blank lines added to output blocks, and the 2nd edition helper parameter renamed to `output_file` (the earlier `file_object` name clashed with the module-level `file_object`). Lesson 06 reviewed: error categories merged (syntax errors are found at compile time), "undefined behavior" replaced with the mathematical explanation, the template uses `except ZeroDivisionError:`, the traceback is line 12 with a note about the commented-out loop, the import is added, and prompt and result spacing matches the code. Lesson 07 reviewed: encoding added, the setup paragraph rewritten, the Side Note limited to the backslash split with a Windows tip, the `else` block explained, and "raises" used in place of "throws." Lesson 08 reviewed: the 2nd edition code now matches the `.py` (no `\n` in the prints, `filename` parameter, the broad `except` added and explained), the encoding is `"UTF-8"` throughout, and the Pylint note is in the `.md`. Lesson 09 (bonus) reviewed: Baudot dated to the 1870s, ASCII dated to 1963, the ASCII table fixed (HT at 9, backtick at 96), the upper half and UCS-2 wording corrected, the "Python uses the system default encoding" section replaces the wrong ASCII claim, the failing examples are commented out in the `.py` with traceback line numbers 20 and 37, and the encoding is `"UTF-8"` throughout. Lesson 10 reviewed: the file name `missing.txt` is used throughout, the `.py` and `.md` function names match, the log file handle is `log` instead of `l`, encoding is `"UTF-8"`, and the append-mode growth of the log is explained. Lesson 11 reviewed: JSON described as a format, "nearly identical" to the dictionary with the `true`/`false`/`null` differences noted, encoding added to every read and write, and the pause note added. Lesson 12 reviewed: encoding added to every read and write (`"UTF-8"` in both files), the pause note added, the 3rd edition retrieval note added, the backslash line continuation explained, the opening sentence reworded, and a `dump()` vs `dumps()` section added. Lesson 13 reviewed: both calls (file missing, file present) are now in the `.py` for each edition, encoding is `"UTF-8"`, the first-run behavior is explained, the pause note and the earlier-lesson note are added, and the `<details>` tags are no longer open by default. Lesson 14 reviewed: encoding is `"UTF-8"` in both code files and the `.md`, the 2nd edition return type matches the code, docstrings and imports match, both code files are linked, the terminal-clearing note is added, and the first best-practice guideline is reworded. Lesson 15 (bonus) reviewed: the `BaseException` vs `Exception` point added, the output dash removed to match the code, "printing" used in place of "logging," a note added that the code file comments out the dangerous loops, and closing the terminal listed as a way out. Lesson 16 (bonus) reviewed: the `__dict__` description corrected, the `json.dump()`/`json.dumps()` sentence corrected, "common" in place of "efficient," the TypeError and improved examples noted as commented out, the Chapter 10 and exercise headings added, and the traceback line numbers set to 35 and 21. Chapter 10 lessons are all reviewed. Next: Chapter 10 Try It Yourself, if it exists, or the next chapter.
- Part I, Chapter 10 Try It Yourself, 2nd edition: reviewed and revised. Assignment 10.12 is the verify-user exercise (the numbering was corrected by the author). Prompts paraphrased; spoilers match the code, including encoding (`"UTF-8"`), variable and parameter names, and the `is None` checks. NOSONAR notes stay in the code, with a note in the `.md`. The 10.10 output uses the author's run, including the `the` counts. The verify-user link now points to `../textbook-downloads/2nd-edition/remember_me.py`. Next: the 3rd edition Try It Yourself (`3ed_` files, 14 exercises plus two intentional extras, `3ed_03_simpler_code.py` and `3ed_11_02_favorite_number_part_2.py`).
- Part I, Chapter 10 Try It Yourself, 3rd edition: reviewed and revised. Prompts restored from the book (10-1 says two times, and the code prints two times). 10-10 now uses `lower()` and searches for `the` as well as `man`, `woman`, and `person`, and its output matches the 2nd edition run (same logic). 10-9 renames the file handle to `log` and drops the stray `pass`. 10-11 part 2 is in the answers file. The `relative_paths.py` embed matches the real module. Textbook links point to `../textbook-downloads/3rd-edition/...` (verified). All files use `"UTF-8"`.
- Part I, Chapter 11 (testing), shared lessons: `00 - Both Editions - Main Guarding/01_main_function` reviewed and revised. The lesson isn't in the book (the book uses the guard only in the Alien Invasion chapter), so it was reviewed for accuracy and voice. Added the Pylint note and the pause and clear-terminal note, and reworded the snippet sentence as a simplified version of the template.
- Next: Part I Chapter 11, `00 - Both Editions - Main Guarding/02_bonus_using_underscores` (bonus: review accuracy and voice only).
  Each Part I chapter: lessons first (one file at a time, with discussion before edits), then Try It Yourself.

## Open questions

- Docstring style (Chapter 9 module files): these use "Parameters:" and "**Returns**:" rather than Google-style `Args:` and `Returns:`. Decided to keep them, so this is an exception to the convention.
- `Battery.get_range()` in `electric_car.py`, `full_car.py`, and the lesson 06 embeds: for a battery size other than 75 or 100 kWh, it prints "This car can go about unknown miles." Lesson 05 handles this with an else branch that prints a "Range unknown" message. Decide whether to make the module files match lesson 05.
- Class methods: added to lesson 9.1 (factory-style `from_string()` with `@classmethod`, lesson md and py updated). Not yet run. Lesson 9.2 doesn't need a class-level counter for class methods.
- None outstanding for the Flask chapter's database setup.
- Chapter 8 type hints (13): hover tooltip shows only the docstring summary line, not the Args section. Cause not confirmed. Pylance is
  documented as rendering docstrings as Markdown, and older reports describe the same limits, but no recent change was found. Options:
  update Pylance and reload, or fall back to comments. Waiting on the author. Images 01 to 05 are in the lessons folder. 06 is removed.
  05 was replaced and may need checking against the current Args layout.
- Chapter 14 (rounding): code and outputs checked by hand, not run. Needs a run in VS Code with sm_utils installed.
- Whether the Learning Log deployment lesson should be dry-run before students see it (see chapter 20 above). The author will do this later.

## Recently fixed, so you don't re-investigate

- Runner: before a web run, the runner checks the web applications environment (`.venv`). If it's missing, can't start, or lacks Django or
  django-bootstrap5, the output pane shows the commands to fix it, which can be copied. Activating the environment isn't needed.

- Build: `createsuperuser --noinput` needs an email, so a placeholder is supplied from the username.
- Build: exercises accept `ex:<folder>`, and load seed data from the chain of exercises.
- Build: `builds_on.txt` accepts `ch19/19-5-protected-blog` (another chapter) and `step:ch20/5` (a lesson step).
- Build: the seed step no longer fails when the sample data needs an admin account that wasn't created. It prints the commands instead.
- Build: `requirements.txt` is now copied into builds.
- Runner: Source tab catches `SystemExit` from a bad build reference, so the app doesn't close.
- Runner: Web chapter Stop on leaving (resets the Run button at once).
- Runner: admin dialog OK and Cancel buttons use the accent colour.
- Runner: `ui/window_layout.py` once broke with two statements on one line. That's fixed.
