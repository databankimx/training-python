# Quickstart

This guide takes you from a fresh copy of the repository to a working lesson runner, where every lesson example can run. Follow the steps in order.
Each step says how to check it worked. The last section covers the errors you're most likely to see.

Commands are for **Windows PowerShell**, and assume you're in the repository root, `training-python`, unless a step says otherwise.

---

## Quick setup with the script

If you'd rather not type each command, `setup.ps1` in the repository root runs steps 2 to 7 below, in order. It's safe to run more than once: anything already
in place is skipped.

First, install **Python 3.12** and **Node.js** (steps 1 below). Then, from the repository root, run:

```pwsh
powershell -ExecutionPolicy Bypass -File .\setup.ps1
```

The `-ExecutionPolicy Bypass` part lets this one script run. It doesn't change any setting on your machine.

The script leaves three things to you:

- **Installing Python and Node.js.** The script checks for them. Add `-InstallMissing` to have it install them with winget, using
  `powershell -ExecutionPolicy Bypass -File .\setup.ps1 -InstallMissing`. Without the switch, it stops and shows the winget commands. Company policy can block winget,
  in which case the script says so and you'll need IT.
- **The GitHub token (step 5).** The script tells you if it isn't set.
- **The admin account.** The runner asks for it on the first web run (step 9).

When the script finishes, it prints a summary and any warnings. Then start the runner (step 8). Steps 1 to 9 below cover the same work, if you need to see what the script does
or run one part by hand.

---

## 1. Install the tools

| Tool | Why | Check |
|---|---|---|
| **Python 3.12** (python.org) | Runs everything | `python --version` shows 3.12 or later |
| **Node.js LTS** | Supplies MathJax and Prism, which typeset math and code in the lesson runner | `npm --version` prints a version |
| **VS Code** (optional) | Editor, with the Python extension | |
| **Git** (optional) | Updating the repository | `git --version` |

When you run the Python installer, tick **Add python.exe to PATH**, and tick **tcl/tk and IDLE**. The second option is what gives you `tkinter`, which the
Tkinter chapter and the lesson runner's logo use.

Restart PowerShell after installing, so the new PATH is picked up.

---

## 2. Create the runner's environment

The lesson runner runs the lessons with the Python that started it. So the libraries the lessons use go into the repository's own environment, `.venv`, in
the repository root.

```pwsh
cd C:\Development\training\training-python
python -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r lesson-runner\requirements.txt
```

**Check:** `.venv\Scripts\python.exe -c "import PySide6, markdown_it; print('ok')"` prints `ok`.

---

## 3. Install the lesson libraries

These are the libraries that the lesson examples import. Install all of them into the same environment now, so no lesson stops on a missing import later.

```pwsh
.venv\Scripts\python.exe -m pip install pytest pygame matplotlib requests plotly sm-utils beautifulsoup4 mechanicalsoup numpy pandas seaborn scipy pyperclip build twine pymongo mysql-connector-python
```

What each one is for:

| Library | Used by |
|---|---|
| `pytest` | Part I, Chapter 11 (testing) |
| `pygame` | Making a Game (Ch12-14), and Part III S23 (Game of Life) |
| `matplotlib`, `plotly`, `requests` | Data Visualization (Ch15-17) |
| `sm-utils` | Several Part I lessons, and Part III S17 |
| `beautifulsoup4`, `mechanicalsoup`, `requests` | Part III S10 (web scraping) |
| `numpy`, `pandas`, `scipy`, `seaborn`, `matplotlib` | Part III S14, S15, S16 |
| `pyperclip` | Part III S24 (built-ins) |
| `build`, `twine` | Part III S13 (publishing a library). The lessons build packages, they don't upload them |
| `pymongo`, `mysql-connector-python` | Part III S17 and S12. These install the client only, see the note below |

The standard library covers everything else, including the Part III chapters S01 to S09, S11, S18, S19 (`tkinter`), S20 to S22.

**Note on S12 and S17:** these two chapters talk to a MySQL or MongoDB server. The libraries install here, but the examples fail with a connection error
until you have a server. That's expected, and the lessons explain the setup in `00_mysql_setup.md` and the S17 notes.

**Check:** `.venv\Scripts\python.exe -c "import pygame, matplotlib, pandas; print('ok')"` prints `ok`. A `pygame` welcome line may print first, which is fine.

---

## 4. Set up the math and code display

The lesson pages load MathJax and Prism from a `vendor` folder. The folder is not in the repository, so install them once with Node.js:

```pwsh
cd lesson-runner\vendor
npm init -y
npm install mathjax@3 prismjs@1
cd ..\..
```

**Check:** these two files exist:

- `lesson-runner\vendor\node_modules\mathjax\es5\tex-svg.js`
- `lesson-runner\vendor\node_modules\prismjs\prism.js`

---

## 5. Set the GitHub token (Data Visualization, Chapter 17)

The Chapter 17 scripts call the GitHub API. Without a token, GitHub allows 60 requests an hour, which the exercises can use up.

Follow [part-ii-projects/data-visualization/github-token-setup.md](part-ii-projects/data-visualization/github-token-setup.md). It creates a classic token with no scopes, and
saves it as a user environment variable named `GITHUB_TRAINING_TOKEN`.

**Check:** open a new PowerShell window, and run `echo $env:GITHUB_TRAINING_TOKEN`. It should print a long string. The token is never written into the code.

The token is only needed for Chapter 17. Skip this step until you reach it if you prefer.

---

## 6. Set up VS Code (optional, recommended)

The Making a Game and Data Visualization code needs the editor settings in `resources\vscode\settings.json`. Without them, VS Code reports import errors that
aren't real.

```pwsh
New-Item -ItemType Directory -Force .vscode | Out-Null
Copy-Item resources\vscode\settings.json .vscode\settings.json
```

If `.vscode\settings.json` already exists, back it up first, because the copy replaces it. Then open the repository root (not a sub-folder) in VS Code, and
run **Developer: Reload Window** from the Command Palette (Ctrl+Shift+P).

**Check:** the Pylint and import errors in the Making a Game files go away after the reload.

---

## 7. Set up the web applications environment

The Django chapters (18 to 20) and the Flask chapter (Part III, S25) run in their own environment, in `part-ii-projects\web-applications`. The runner checks it
before each web build, and shows the exact commands if it isn't ready.

This environment must be named `.venv`, and it goes in `web-applications`:

```pwsh
cd part-ii-projects\web-applications
python -m venv .venv
.venv\Scripts\python.exe -m pip install -r ch20-styling-and-deploying\lessons\01-bootstrap-setup\requirements.txt
.venv\Scripts\python.exe -m pip install -r ..\..\part-iii-beyond-the-book\s25-flask-learning-log\01-flask-setup\requirements.txt
cd ..\..
```

The first install gives Django and `django-bootstrap5`. The second gives Flask and SQLAlchemy. Both go into the same environment.

**Check:** `part-ii-projects\web-applications\.venv\Scripts\python.exe -c "import django, flask, sqlalchemy; print('ok')"` prints `ok`.

You don't need to activate this environment. The runner uses its Python directly.

---

## 8. Start the lesson runner

From the repository root, using the repository environment from step 2:

```pwsh
.venv\Scripts\python.exe lesson-runner\app.py
```

The window opens on the welcome lesson. The chapter tree is on the left.

---

## 9. Your first run of each kind of step

Work through these once, to confirm each kind of example runs. Each one should take a few seconds, except the naive Fibonacci lesson, which the lesson warns
about.

| Kind | Where | What you should see |
|---|---|---|
| Part I | Part I, Chapter 2 | Output in the Output pane. Press **Run** (or F5) |
| Pygame | Making a Game, Chapter 12, first step | A game window opens. Close it, or press Escape |
| Charts | Data Visualization, Chapter 15 | A chart window or a browser page opens |
| Web | Web Applications, Chapter 18, step 1 | The build runs its checks, and the browser opens the start page |
| Flask | Part III, S25, step 1 | The build runs its checks, and the browser opens the home page |

**The first web run asks for an admin account.** A dialog asks for a username and password, once per session. The username is lowercase letters and numbers,
from 3 to 30 characters. The password is at least 8 characters. The runner creates the account in the local build, so you can sign in to the sites you build.
Keep these details somewhere safe, because the runner asks again next time you start it.

---

## 10. Optional extras

You can skip all of these, and every lesson still runs.

- **A database server for Part III S12 or S17.** See the note in step 3.
- **SQL Server or MySQL for the Flask chapter.** S25 step 14 explains how to switch. It's information only, and the chapter runs on SQLite without it.
- **The textbook downloads.** They're already in each chapter's `textbook-downloads` folder.
- **Deploying the web sites to PythonAnywhere.** The Django chapter's step 5 explains it. It's optional, and you don't need it to run the lessons.

---

## Troubleshooting

| What you see | What to do |
|---|---|
| `ModuleNotFoundError` for `pygame`, `matplotlib` or another library, in a lesson | The library isn't in the repository's `.venv`. Run step 3 again. Make sure the runner was started with `.venv\Scripts\python.exe` (step 8). |
| "The web applications environment isn't ready" in the Output pane | Follow the commands it prints, which are the same as step 7. Then click **Run** again. |
| Port 8000 is in use, and the runner asks to stop it | Something from an earlier run is still listening. Choose **Yes** to stop it. |
| `No module named 'django_bootstrap5'`, or any module for the web chapters, when run outside the runner | The command used the wrong Python. Use `web-applications\.venv\Scripts\python.exe`, not the system Python. |
| Lesson math or code shows as plain text | The `vendor` folder is missing. Repeat step 4. |
| `tkinter` is missing, or the Tkinter chapter fails to import | Re-run the Python installer, and tick **tcl/tk and IDLE**. On Linux, install it with `sudo apt install python3-tk`. |
| Chapter 17 reports a GitHub rate limit | The token isn't set. Repeat step 5, then open a new PowerShell window. |
| S12 or S17 reports a connection error | The database server isn't running. Those lessons need a server (see step 3). |
| A Pylint or import error appears in the Making a Game files only in VS Code | Repeat step 6, and reload the window. |
| `Could not open requirements file` | Run the install command from the folder it names. The path is relative to where you are. |

If a problem isn't listed here, note the step you were on and the full error text, then report it. Include the Output pane text, because the first error is
often the useful one.
