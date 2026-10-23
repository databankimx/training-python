# Setting Up a Project

## What this step does

This step starts the Learning Log project. It sets up a Python environment, installs Django, creates the project, and
checks that the project runs. The project is called `ll_project`, and it has no app yet. The app comes in the next
step.

## If you're using the lesson runner

You don't need the setup steps below. The runner does them for you.

1. In the steps list on the left, choose **Ch18 · Getting started with django**, then step 1.
2. Click **Run**.
3. In the **Admin account** dialog, enter a username (lowercase letters and numbers only) and a password (at least 8 characters). Repeat the password, then click **OK**. You only need to do this once per runner session.
4. Watch the output. When it says `Starting development server`, click **Open in browser**.
5. The browser shows Django's "install worked" page at the home address. That's expected at this step. To see the admin page, add `admin/` to the end of the address, so it reads `http://127.0.0.1:8000/admin/`.
6. Sign in with the username and password you chose. You should see the Django admin page.
7. Press **Escape** in the runner to stop the server.

## For dummies: the quick version

Do these in order. Each step tells you what to type, and what you should see.

1. Open PowerShell, and go to the `web-applications` folder.
2. Type `python -m venv .venv` and press Enter. This makes a private space just for this project.
3. Type `.venv\Scripts\Activate.ps1` and press Enter. You should see `(.venv)` at the start of the line.
4. Type `python -m pip install -r ch18-getting-started-with-django\lessons\01-setting-up-a-project\requirements.txt` and press Enter. This installs Django.
5. Type `python build_stage.py ch18 1 --run` and press Enter. This builds the project, checks it, runs the tests, and starts the server.
6. Open a browser and go to `http://127.0.0.1:8000/admin/`. You should see a login box.
7. Back in PowerShell, press Ctrl+C to stop the server.

### Words you'll see

- **Django:** a toolkit for building websites in Python. It does the hard parts, such as databases and logins.
- **Virtual environment (`.venv`):** a private copy of Python for one project, so its installs don't mix with others.
- **Project:** the whole website. Here it's `ll_project`.
- **App:** one part of the website that does one job. Here the Learning Log will have one app.
- **Server:** the program that answers web requests. `runserver` starts it on your own computer.
- **Test:** a small program that checks the project does what it should.

### If something goes wrong

- **`python` is not recognized:** Python isn't on your PATH. Reinstall Python from python.org, and tick "Add python.exe to PATH".
- **No `(.venv)` at the start of the line:** the activate step didn't work. Run step 3 again from the `web-applications` folder.
- **The browser shows Django's "install worked" page at `http://127.0.0.1:8000/`:** that's expected at this step. The only address the project knows about is `/admin/`, so Django shows its welcome page for the home address. Chapter 18 adds a real home page in a later step.
- **The browser shows nothing:** look at the PowerShell window. Any error message is printed there.

## Setup

Django needs its own virtual environment. From the `web-applications` folder, create and activate one:

```pwsh
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r ch18-getting-started-with-django\lessons\01-setting-up-a-project\requirements.txt
```

The requirements file pins Django to version 5.2.17, the latest long-term support (LTS) release. Every step in this
chapter uses that version. The `.venv` folder is your environment, and it isn't part of the project. Git ignores it.

## Running this step

From the `web-applications` folder, with the environment active, run:

```pwsh
python build_stage.py ch18 1 --run
```

The script builds the project into `build\ch18-step-01`, checks it, runs its tests, and starts the development
server. Open `http://127.0.0.1:8000/admin/` in a browser to see the Django admin login page. Press Ctrl+C to stop the
server.

## The code

The project is made of the files that `django-admin startproject` creates. They're shown here for reference, and the
settings are the ones the book describes.

`manage.py` is the command-line tool for the project. Every command you run in this chapter goes through it:

```python
#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
--snip--
```

`ll_project/settings.py` holds the settings. The database is a single SQLite file, which Django creates for you:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

The `SECRET_KEY` in this file is a placeholder for learning. Chapter 20 replaces it before the live deployment.

`ll_project/urls.py` routes URLs to pages. At this point it only routes the admin site:

```python
urlpatterns = [
    path("admin/", admin.site.urls),
]
```

## Testing this step

The tests in `ll_project/tests.py` check two things. The admin login page loads, which proves the URL routing works. The
database is SQLite, which proves the settings are as the book describes. Run them with the build script, or in the built
folder with:

```pwsh
cd build\ch18-step-01
python manage.py test
```

You should see `Ran 2 tests` and `OK`.

## Changed files

- `requirements.txt`: pins Django 5.2.17
- `manage.py`: the command-line tool
- `ll_project\__init__.py`, `settings.py`, `urls.py`, `wsgi.py`, `asgi.py`: the project
- `ll_project\tests.py`: the tests for this step

---
