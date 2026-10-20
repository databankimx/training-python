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

## Open questions

- None outstanding for the Flask chapter's database setup.
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
