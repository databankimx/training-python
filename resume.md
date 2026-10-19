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
- **Editor settings copy for students:** `resources\vscode\settings.json`

## Conventions

- US English throughout: color, center, maximize, lowercase.
- No status sections in any README. READMEs describe the content only.
- Lessons: a "For dummies" section, then runner steps where relevant, then the code, then testing, output and changed files.
  Screenshot placeholders go in the Output section, in a `lesson-images` folder inside the step or exercise.
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

## Open questions

- Whether the runner should offer a database choice for the Flask chapter, or use a connection string.
- Whether the runner should stop with a clear error when `.venv` is missing, rather than quietly using the repo's environment. The current
  fallback caused confusion during chapter 20. A change here is a candidate for a future session.
- Whether to delete the `.ll_venv` folder. It's not used, so it can go.
- Whether the Learning Log deployment lesson should be dry-run before students see it (see chapter 20 above).

## Recently fixed, so you don't re-investigate

- Build: `createsuperuser --noinput` needs an email, so a placeholder is supplied from the username.
- Build: exercises accept `ex:<folder>`, and load seed data from the chain of exercises.
- Build: `builds_on.txt` accepts `ch19/19-5-protected-blog` (another chapter) and `step:ch20/5` (a lesson step).
- Build: the seed step no longer fails when the sample data needs an admin account that wasn't created. It prints the commands instead.
- Build: `requirements.txt` is now copied into builds.
- Runner: Source tab catches `SystemExit` from a bad build reference, so the app doesn't close.
- Runner: Web chapter Stop on leaving (resets the Run button at once).
- Runner: admin dialog OK and Cancel buttons use the accent colour.
- Runner: `ui/window_layout.py` once broke with two statements on one line. That's fixed.
