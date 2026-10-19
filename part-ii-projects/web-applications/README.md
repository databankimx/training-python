# Web Applications

This section follows chapters 18 to 20 of *Python Crash Course* (3rd edition). It builds the Learning Log, a website for keeping notes
about the topics you're learning. Chapter 19 adds user accounts, and chapter 20 styles the site and prepares it for a live server.

## Layout

Each chapter has the same structure as the other projects.

```
web-applications/
  build_stage.py
  ch18-getting-started-with-django/
    lessons/
      01-setting-up-a-project/   requirements.txt, manage.py, ll_project/, lesson.md, lesson-images/, check.txt
      02-starting-an-app/        learning_logs/, seed.json, start.txt, lesson.md, lesson-images/
      ...
      09-edit-entries/
    try-it-yourself/
      18-1-new-projects/         lesson.md
      18-2-short-entries/        lesson.md, lesson-images/
      18-3-the-django-api/       lesson.md
      18-4-pizzeria/             a full project: manage.py, pizzeria_project/, pizzas/, start.txt
      18-5-meal-planner/         a full project: manage.py, meal_planner/, meal_plans/, start.txt
      18-6-pizzeria-home-page/   the changes to 18-4, with builds_on.txt
      18-7-template-documentation/  lesson.md
      18-8-pizzeria-pages/       the changes to 18-6, with builds_on.txt and seed.json
    textbook-downloads/
      2nd-edition/lessons/       the book's downloads, unchanged
      3rd-edition/lessons/       the book's downloads, unchanged
      3rd-edition/try-it-yourself/
  ch19-user-accounts/
    lessons/
      01-user-accounts/          accounts/, ll_project/, learning_logs/, lesson.md, lesson-images/
      02-topic-ownership/        learning_logs/, seed.json, start.txt, lesson.md
      03-restricting-access/     learning_logs/, start.txt, lesson.md
      04-duplicate-topics/       learning_logs/, start.txt, lesson.md
      05-deleting-entries/       learning_logs/, start.txt, lesson.md
    try-it-yourself/
      19-1-blog/                 a full project: manage.py, blog_project/, blogs/, seed.json
      19-2-blog-accounts/        the changes to 19-1, with builds_on.txt
      19-3-refactoring/          lesson.md (code change, shown in the lesson)
      19-4-protecting-new-entry/ lesson.md (already in place, shown in the lesson)
      19-5-protected-blog/       the changes to 19-2, with builds_on.txt and seed.json
    textbook-downloads/
      2nd-edition/lessons/       the book's downloads, unchanged
      3rd-edition/lessons/       the book's downloads, unchanged
      3rd-edition/try-it-yourself/
  ch20-styling-and-deploying/
    lessons/
      01-bootstrap-setup/        requirements.txt, ll_project/, lesson.md, lesson-images/
      02-navigation-bar/         learning_logs/templates, lesson.md
      03-styled-pages/           learning_logs/templates, accounts/templates, lesson.md
      04-production-settings/    ll_project/, learning_logs/templates (404.html, 500.html), lesson.md
      05-deploy-pythonanywhere/  requirements.txt, lesson.md, lesson-images/ (the deployment steps)
    try-it-yourself/
      20-1-other-forms/          lesson.md (the forms from step 3)
      20-2-stylish-blog/         the Blog's templates and settings, with builds_on.txt pointing to 19-5
      20-3-live-blog/            the Blog's settings and error pages, with builds_on.txt (optional deployment)
      20-4-extended-learning-log/  public topics, with builds_on.txt pointing to lesson step ch20/5
    textbook-downloads/
      2nd-edition/lessons/       the book's downloads, unchanged
      3rd-edition/lessons/       the book's downloads, unchanged
      3rd-edition/try-it-yourself/
```

- **Lesson steps** under `lessons` build the Learning Log one step at a time. Each folder holds only the files that step adds
  or changes, so the repo keeps one copy of each file.
- **`seed.json`** holds example data for a step, and it's loaded after the database is created.
- **`check.txt`** says what to look for after a step runs.
- **`start.txt`** names the page the browser opens first.
- **`lesson-images`** holds the screenshots that appear in a lesson. The build never copies them.
- **Exercises** in `try-it-yourself` are either full projects, or updates that name the exercise or lesson step they build on in
  `builds_on.txt`. An update can name an exercise in another chapter, as `ch19/19-5-protected-blog`, or a lesson step, as `step:ch20/5`.
  Exercises that only change code, with no project of their own, are lessons.
- **`textbook-downloads`** holds the book's own files, copied without changes.

## Building a step

`build_stage.py` builds a lesson step or an exercise into the `build` folder. It checks the project, creates the database,
creates an admin account, loads any seed data, and runs the tests. With `--run`, it also starts the development server.

```pwsh
python build_stage.py --list
python build_stage.py ch18 1 --run
python build_stage.py ch20 ex:20-4-extended-learning-log --run
```

The `build` folder is temporary, and Git ignores it.

## Running from the lesson runner

In the runner, open **Web Applications**, then the chapter. Lesson steps run from the steps list. The exercises that are
projects or updates run from the **Try it Yourself** node. The runner asks for an admin username and password once per session,
creates the account, and opens the browser at the step's start page. Press Escape, or close the runner, to stop the server.

## Requirements

Python 3.10 or later, which is the minimum Django 5.2 supports. Create the chapter's virtual environment in this folder, and name it
`.venv`, as the lessons do:

```pwsh
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r ch20-styling-and-deploying\lessons\01-bootstrap-setup\requirements.txt
```

The requirements pin Django 5.2.17, the latest long-term support release, and `django-bootstrap5`, which chapter 20 uses. The runner
uses this environment to build each step, so install the requirements before you run a web step.

## Deploying (optional)

Chapter 20 includes deployment to PythonAnywhere, a free host that keeps the site's data on disk for the length of the course. The
Learning Log deployment is in chapter 20, step 5. Deploying is optional: the course doesn't depend on a live site, and exercise 20-3
explains the same steps for the Blog. A free PythonAnywhere account has one web app, so deploying the Blog replaces the Learning Log
site, unless you create a second account.
