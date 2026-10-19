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
- Exercises that are projects or updates have `builds_on.txt` if they extend another exercise.
- Textbook downloads are copied unchanged into `textbook-downloads`, in `2nd-edition`, `3rd-edition/lessons` and `3rd-edition/try-it-yourself`.
  The book's own lesson text is not copied.
- The `build` folders and `.venv` folders are not committed. `.vscode` is not tracked in git.
- Do not write into `C:\Development\training\python-crash-course`. Some earlier path tricks resolve into it, so check the path first.
- Django version: 5.2.17 (latest LTS, per the official download page). Django 6.2 LTS is expected in April 2027.

## Web Applications (Learning Log)

### Chapter 18: complete, committed
- Lesson steps 1 to 9 in `ch18-getting-started-with-django\lessons`. All screenshots are in place. Tests passed in the runner.
- Exercises in `try-it-yourself`:
  - 18-1, 18-2, 18-3, 18-7: lesson pages only. 18-2 points to the conditional already in step 3.
  - 18-4 Pizzeria: full project `pizzeria_project` with the `pizzas` app. Seed: none.
  - 18-5 Meal Planner: full project with `meal_plans`. Start page `/`.
  - 18-6 Pizzeria home page: update on 18-4 (`builds_on.txt`).
  - 18-8 Pizzeria pages: update on 18-6 (`builds_on.txt`), with `seed.json` (Hawaiian and Meat Lovers).
- Textbook downloads copied. Build folder deleted.

### Chapter 19: lessons complete, exercises not started (User Accounts)
Lesson steps in `ch19-user-accounts\lessons`, each with its screenshots in place unless noted:
1. `01-user-accounts`: accounts app, login, logout, registration, top bar greeting. Tests: 33. Start page is the login page.
2. `02-topic-ownership`: `Topic.owner` foreign key, migration `0003_topic_owner` (default user 1, `preserve_default=False`). New topics need sign-in and
   record the owner. Seed topics are owned by user 1, the account the runner creates first. Tests: 35. Start page is the login page.
   Screenshot placeholder `topics-signed-in.png` (check whether it has been added).
3. `03-restricting-access`: topics, topic, new entry and edit pages require sign-in. Topics list filtered by owner. Other users' topics and entries give
   a 404. Tests: 41. Screenshot `topics-own.png` in place.
4. `04-duplicate-topics`: unique constraint per owner (`0004_unique_topic_per_owner`), form check case-insensitive. Tests: 45. Screenshot
   `duplicate-topic.png` in place.
5. `05-deleting-entries`: delete with confirmation page, owner only, admins can still delete via the admin site. Tests: 50. Screenshot
   `delete-entry.png` in place.

Not yet tested in the runner: chapter 19 steps 1 to 5 (the user reported step 3 as working, and step 4 and 5 still need the runner test).
Screenshot placeholders for steps 1 and 2 are noted above.

Remaining for chapter 19:
- Chapter 19 exercises (3rd Edition 19-1 to 19-5). Wording to be checked against the book first. The 2nd Edition solution in
  `C:\Development\training\python-crash-course\...\2nd Edition\03 - Web Applications\Ch19 - User Accounts` has code to adapt.
- Chapter 19 textbook downloads: from the 2nd Edition's Ch19 folder and the 3rd Edition's `Ch19 - Users` folder, same layout as chapter 18.
- Update the web applications README after chapter 19.

### Chapter 20: not started (Styling and Deploying)
- Styling with Bootstrap (3rd Edition uses django-bootstrap5).
- Exercises 20-1 Other Forms, 20-2 Stylish Blog, 20-3 Live Blog, 20-4 Extended Learning Log.
- Live deployment at the end, as the final step, done manually. Students can't deploy to AWS directly (that goes through the cloud team and
  security review), so AWS is out for students. Platform.sh has been renamed Upsun (23 September 2025), but Upsun's only free option is a
  15-day trial, which fails the requirement that students get a free tier. Render's free web service is the candidate: it sleeps after 15
  minutes idle, and its free PostgreSQL expires (the sources disagree on how long, so check Render's page). Still to decide: the database
  students use on Render, and how the lesson handles the sleep and expiry. Heroku is out, because it no longer has a free tier.
- Chapter 20 step 4 (Production Settings): the lesson uses `debug-404.png`, the local debug page. In step 5, add the friendly Page not found
  screenshot taken on the live PythonAnywhere site, as a second picture, and show both in the lesson.
- Deployment options checked (2026): Upsun has only a 15-day trial, so it's out. Render's free web service sleeps, and its free database expires,
  so students' data would be lost partway through a course. PythonAnywhere's free account keeps data on disk (SQLite persists), needs a
  monthly click to renew the web app, and allows 100 CPU-seconds a day. Recommended: PythonAnywhere. Awaiting the decision. The deployment
  lesson must say why this host was chosen, and how it differs from the book (Heroku and Platform.sh steps, and the free tier change).
- Textbook downloads, then the README update.

## Runner and build system

- `part-ii-projects\web-applications\build_stage.py` builds a lesson step (`ch18 5`) or an exercise (`ch18 ex:18-8-pizzeria-pages`) into `build\`.
  It creates the admin account from `STUDENT_ADMIN_USERNAME` and `STUDENT_ADMIN_PASSWORD` (no prompts), loads seed data, runs tests, prints `check.txt`,
  and with `--run` starts the server.
- The runner (`lesson-runner`) shows web chapters with the lesson steps and a **Try it Yourself** node. Run asks once per session for an admin username
  (lowercase letters and numbers, at least 8 characters for the password). It opens the browser at `start.txt` when the server is ready.
- Escape, or selecting another step or chapter, stops the run. Closing the window also stops it.
- Child processes are put in a Windows job object, so they end if the runner exits or crashes.
- Before a web run, if port 8000 is in use, the runner asks whether to stop the process using it.
- The Source tab shows read-only listings for web steps and exercises: new files in full, and changed files as diffs with `--snip--`.
- The web build runs with the Python in `part-ii-projects\web-applications\.venv`, which the runner uses when it exists. Install Django there first, from
  `ch18-getting-started-with-django\lessons\01-setting-up-a-project\requirements.txt`.

## Other areas

### Making a Game (Alien Invasion)
- Chapters 12, 13 and 14 are complete. The chapter 14 expanded game is in `ch14-scoring\try-it-yourself\14-7-expanding-the-game`.
- The `final` folder holds the book's finished game, with its own README.

### Data Visualization
- Complete as of earlier sessions. Its files use `#pylint: disable=invalid-name` where needed; the solution settings now disable that check globally.

### Part I and Part III
- Not changed in this work.

## Roadmap

- **Flask Learning Log (Part III, section s25):** a new section that builds the same Learning Log with Flask instead of Django, because
  DataBank uses Flask. Same lessons, written for Flask. Decisions so far: placement s25 (order irrelevant), Flask 3.1.3 (latest stable,
  which Flask doesn't label LTS), step-by-step with runner support, and SQLAlchemy as the data layer. Database: DataBank hosts both SQL Server
  and MySQL on AWS, and both are installed on the author's PC and expected to be on students' PCs too. The lessons use SQLite by default. A
  later step switches to SQL Server or MySQL by setting a connection string, and the app is tested against each. Still to decide: whether the
  runner offers the database as a choice, or the connection string is set in an environment variable. Not started.

## Open questions

- Whether admins may delete entries in the app pages. Current decision: admins delete through the admin site only, and the app pages stay owner-only.
- Whether the runner should offer a database choice for the Flask chapter, or use a connection string.

## Recently fixed, so you don't re-investigate

- Runner: Web chapter Stop on leaving (resets the Run button at once).
- Runner: OK and Cancel buttons in the admin dialog are styled with the accent colour.
- Build: `createsuperuser --noinput` needs an email, so a placeholder is supplied from the username.
- Build: exercises accept `ex:<folder>`, and load seed data from the chain of exercises.
- Runner: `ui/window_layout.py` once broke with two statements on one line. That's fixed.
