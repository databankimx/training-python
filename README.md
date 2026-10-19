# DataBank IMX - Python Developer Training

## License and Support

This repository is provided under the [MIT License](LICENSE). You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell the materials in this repository, subject to the terms of that license.

This repository is provided for training and reference purposes only. DataBank IMX does not provide warranties, guarantees, maintenance, troubleshooting, implementation assistance, or technical support for this code or its use. Use it in any way permitted by the MIT License, but you are responsible for evaluating, adapting, testing, and supporting any use of it in your own environment.

---

## What is this repository for?

- Python developer training curriculum for DataBank IMX
- Chapter-by-chapter lesson files, code samples, and exercises covering Python fundamentals through advanced topics, based on the *Python Crash Course* textbook (3rd edition) by Eric Matthes
- Extended with a substantial "Beyond the Book" supplemental track covering topics not addressed in the textbook
- Includes a Qt-based lesson runner for navigating, reading, and running lessons interactively

---

## About

- **Author:** [Scott McLean](mailto:smclean@databankimx.com)
- **Purpose:** Internal developer training curriculum for DataBank IMX

---

## DataBank Responsibilities for Custom Code

All DataBank employees - including those working with AI-assisted tools - are bound by the [Development Rules of Engagement](development-rules-of-engagement.md). That document defines the rules for quoting, approving, developing, reviewing, scanning, storing, and delivering custom code for client work.

Key obligations that apply to everyone on every custom code engagement:

- **You own the code you deliver.** This applies equally to hand-written code, AI-assisted code, and AI-generated code. "The AI wrote it" is not an acceptable explanation for a production issue, a failed review, a security finding, or a support problem.
- **Code must be reviewed before delivery.** Review is interactive and must confirm that the code works, meets DataBank standards, is maintainable, and that the developer understands it well enough to explain, debug, and maintain it. Polished or well-formatted output - including AI-generated output - is not evidence of correctness.
- **Code must be in source control before delivery.** All custom code must be committed to the appropriate DataBank GitHub Enterprise repository before it is delivered to a client, regardless of whether the client receives source code, compiled binaries, or deployed functionality.
- **CI scanning must pass before delivery.** Required checks are the standards policy scan, SonarQube, and Snyk. A passing local run is not a substitute.
- **All third-party dependencies must be license-vetted.** The license must permit closed-source commercial use. Copyleft or unclear licensing must be escalated before use. Dependencies must not be added simply because an AI tool suggested them.
- **Only approved AI tools may be used.** Use only IT-approved tools through company accounts. All data entered into AI systems must be treated as confidential by default.
- **Custom code is billable work.** Code must be tied to an approved quote or engagement before commitment or delivery. Development quotes require approval from the Development Director or delegated development leadership before being sent externally.
- **Exceptions require explicit approval.** Time pressure alone is not a reason to bypass quote approval, source control, review, or CI scanning.

See the [Development Rules of Engagement](development-rules-of-engagement.md) for the full policy, including billing and quoting rules, source-code delivery rules, the delivery readiness checklist, and the exception process.

---

## Textbook reference

*Python Crash Course, 3rd Edition* - Eric Matthes - No Starch Press
ISBN: 978-1718502703 - [Amazon](https://www.amazon.com/dp/1718502703)

Textbook resources:
- [3rd Edition Downloads](https://github.com/ehmatthes/pcc_3e/archive/refs/heads/main.zip)
- [2nd Edition Downloads](https://github.com/ehmatthes/pcc_2e/zipball/master/) (reference only - some exercise answers retained for comparison)

### Why Python Crash Course?

Python Crash Course strikes the right balance between accessibility and depth for developers who are new to Python but not new to programming. Part I covers the language fundamentals clearly. Part II puts them to work in three substantive projects. The Beyond the Book track adds the topics that matter for professional Python development at DataBank - data structures, databases, regular expressions, library publishing, and more.

---

## Setup and requirements

- Python 3.12 or later (3.15 is current and works fine; 3.12 is the minimum tested version)
- VS Code with the Python extension (recommended), or any editor you prefer
- A virtual environment (instructions below)

See [QUICKSTART.md](QUICKSTART.md) for a step-by-step guide that sets up everything the lesson runner needs to run every lesson example, including the separate environment for the web chapters. The guides in `resources/setup/` cover the workstation and Python installation in more detail:

* [Setting Up Your Workstation for Development Training](resources/setup/01%20Setting%20Up%20Your%20Workstation%20for%20Development%20Training.md)
* [Setting Up Your Workstation for Python Training](resources/setup/02%20Setting%20Up%20Your%20Workstation%20for%20Python%20Training.md)

### Quick start

```bash
# Create a virtual environment
python -m venv .venv

# Activate it (Windows)
.venv\Scripts\activate

# Activate it (macOS / Linux)
source .venv/bin/activate

# Update pip
python -m pip install --upgrade pip

# Install Scott's utility functions (used throughout the lessons)
pip install sm-utils

# Install chapter-specific libraries as needed (see below)
```

### Libraries by section

| Library | Section | Install |
|---|---|---|
| `pytest` | Ch11 - Testing | `pip install pytest` |
| `pygame` | Part II - Alien Invasion (Ch12-14) | `pip install pygame` |
| `matplotlib` | Part II - Data Visualization (Ch15-17) | `pip install matplotlib` |
| `requests` | Part II - Data Visualization (Ch15-17) | `pip install requests` |
| `plotly` | Part II - Data Visualization (Ch15-17) | `pip install plotly` |

The Django chapters (Part II, Web Applications) and the Flask chapter (Part III, S25) need their own environment, in `part-ii-projects\web-applications\.venv`. Quickstart step 7 explains how to set it up.

You can wait until the relevant chapter to install each library, or install everything up front. There is no harm in installing all of them now.

### GitHub token for chapter 17

The chapter 17 scripts call the GitHub API. Without a token, GitHub allows 60 requests per hour, which the chapter's exercises can use up. With a token, the limit is 5,000 per hour.

Create a classic token with no scopes, and set it as a user environment variable named `GITHUB_TRAINING_TOKEN`. The scripts read the variable, so the token never goes in the code. The full steps are in [github-token-setup.md](part-ii-projects/data-visualization/github-token-setup.md). The same guide is in the lesson runner, under **Part II - Projects > Data Visualization > Setup**.

### Libraries for the lesson runner and Beyond the Book

The lesson runner and the Beyond the Book chapters use the libraries below.
The Part II libraries are in the table above. Install a library only when you
get to the chapter that needs it.

#### Lesson runner (`lesson-runner/`)

| Library | Purpose | Install |
|---|---|---|
| `PySide6` | Qt for Python: the window, widgets, and the WebEngine that shows lessons | `pip install PySide6` |
| `markdown-it-py` | Converts lesson Markdown to HTML | `pip install markdown-it-py` |
| `mdit-py-plugins` | Adds `$...$` and `$$...$$` math support to `markdown-it-py` | `pip install mdit-py-plugins` |
| `tkinter` | Standard library. Used by `logo.py`, which the Qt runner imports. Included in the python.org Windows installer | Included with Python |
| MathJax and Prism | Typesets math and highlights code in lesson pages. These are Node.js packages, not Python packages | `npm install mathjax@3 prismjs@1`, run in `lesson-runner/vendor/` |

The Python packages for the runner are listed in `lesson-runner/requirements.txt`:

```bash
python -m pip install -r lesson-runner/requirements.txt
```

The legacy Tkinter runner in `lesson-runner-tk/` also uses `tkinter`. It can
also use `matplotlib` for math, but that is optional.

#### Beyond the Book (`part-iii-beyond-the-book/`)

| Library | Chapter | Install |
|---|---|---|
| `sm-utils` | S17 (`login.py`). Other lessons use local copies of the same helpers in `utility_functions.py` | `pip install sm-utils` |
| `beautifulsoup4` | S10 - Web scraping | `pip install beautifulsoup4` |
| `requests` | S10 - Web scraping | `pip install requests` |
| `mechanicalsoup` | S10 - Web scraping | `pip install mechanicalsoup` |
| `mysql-connector-python` | S12 - MySQL databases. Needs a MySQL server; see `00_mysql_setup.md` | `pip install mysql-connector-python` |
| `numpy` | S14 - NumPy, and S16 - SciPy | `pip install numpy` |
| `pandas` | S15 - Pandas | `pip install pandas` |
| `matplotlib` | S14 and S15 - plotting | `pip install matplotlib` |
| `seaborn` | S14 - NumPy random distributions | `pip install seaborn` |
| `scipy` | S16 - SciPy | `pip install scipy` |
| `pymongo` | S17 - MongoDB. Needs a MongoDB server | `pip install pymongo` |
| `pygame` | S23 - Game of Life | `pip install pygame` |
| `pyperclip` | S24 - Built-ins (clipboard example) | `pip install pyperclip` |
| `build` and `twine` | S13 - Publishing a library | `pip install build twine` |

Several Beyond the Book chapters use only the standard library, including S19
(`tkinter`). On Linux, tkinter must be installed separately, for example with
`sudo apt install python3-tk`.

### Licensing of libraries

The libraries in this repository are used under the following conditions.

**Approved for the training repository only.** Development leadership has approved the
following libraries for use in `training-python`, on the condition that there are no
liabilities in how the solution is packaged:

* PySide6 (LGPL/GPL, or commercial) - lesson runner
* mysql-connector-python (GPL-2.0 with FOSS exception) - S12
* pygame (LGPL-2.1) - S23, and Part II

This approval covers running the tutorial and the lesson runner from this repository.
It does **not** cover packaged or delivered projects. Do not use these libraries, or
code that depends on them, in an installer, a PyInstaller or other bundled build, a
container image, a client deliverable, or any closed-source product. If you want to
move any code out of this repository, stop and take it to development leadership first.
The approval does not carry over to the new code.

**Other libraries** in the tables above are under permissive licenses (MIT, BSD, or
Apache 2.0), and can be used in closed-source work under the Development Rules of
Engagement.

**Vendored files.** MathJax (Apache 2.0) and Prism (MIT) are copied into the lesson
runner's `vendor/` folder. Keep their license and notice files with them.

The full policy is in [Development Rules of Engagement](development-rules-of-engagement.md),
section 12.

### VS Code settings

The Making a Game and Data Visualization projects need the VS Code settings in `resources/vscode/settings.json`. They tell the editor where the game's files are, which Pylint checks to skip, and the spell-check word list. Without them, the editor reports import and Pylint errors in the game code.

Copy the file into a `.vscode` folder at the root of the repository. The `.vscode` folder isn't tracked in git, so a clone doesn't include it. From the repository root, run:

```pwsh
New-Item -ItemType Directory -Force .vscode | Out-Null
Copy-Item resources\vscode\settings.json .vscode\settings.json
```

If a `.vscode\settings.json` file already exists, back it up first, because the copy replaces it. Then open the repository root in VS Code, and run **Developer: Reload Window** from the Command Palette (Ctrl+Shift+P). The settings are read when the window starts, so the reload is needed.

Open the repository root, not a sub-folder. The settings use paths from the root, so they don't apply when only a project folder is open.

### Pylint (optional)

A linter helps enforce best practices and style guidelines. If you use Pylint in VS Code, the following arguments suppress warnings that would fire on intentional training-repository patterns:

```json
"pylint.args": [
    "--disable=invalid-name",
    "--disable=global-statement",
    "--disable=global-variable-undefined",
    "--disable=broad-exception-caught"
]
```

Add these to your VS Code User Settings JSON (`Ctrl+Shift+P` -> `Preferences: Open User Settings (JSON)`).

---

## Running the training

### Lesson Runner

The lesson runner is a Qt desktop application that lets you browse chapters, read lesson notes, and run code examples interactively. Lessons are rendered with MathJax for math and Prism for code.

Setup (the `vendor/` MathJax and Prism files, and the Python packages) is in [lesson-runner/README.md](lesson-runner/README.md). Once it's set up, start the runner from the repository root:

```bash
python lesson-runner/app.py
```

#### Finding lessons

The chapter tree on the left lists every chapter:

* **Part I** chapters hold their lessons directly. Each chapter's `try-it-yourself` steps, and the chapter 11 editions, are nested beneath the chapter. Chapters start collapsed. Selecting a chapter with no steps of its own moves to its first sub-chapter.
* **Part II** chapters are grouped by project. Data Visualization comes first, with its 2nd and 3rd Editions, each holding Ch15 to Ch17 with their lessons and try-it-yourself steps. The **Setup** entry at the top of Data Visualization has the GitHub token instructions. Making a Game covers Ch12 to Ch14, with the Alien Invasion game built step by step. Web Applications covers Ch18 to Ch20: the Learning Log built with Django, from models and forms through user accounts, styling, and optional deployment. Each step runs a live site, and the runner shows the step's changes in the Source tab.
* **Part III** chapters hold their lessons directly, and any sub-folders are nested beneath them (for example S13 and S14).

Select a step in the list below the chapters. Steps that share one lesson file are indented under the first one.

#### Reading and running a step

* The **Lesson** tab shows the step's lesson. Maths is typeset, and code blocks are highlighted.
* The **Source** tab shows the step's code. You can edit it, but edits are not saved to the file. Reset restores the original, and Copy copies whatever tab is open.
* Press **Run** (or F5) to run the step. Output appears in the Output pane, and errors appear in red.
* If the step asks for input, a dialog opens. If it pauses, press **Continue** (or Ctrl+Shift+Enter).
* To pass command-line arguments, type them in the **args** box before running.
* Press Escape to cancel a run.
* Badges under the step title say what the step does: **Window** (opens a matplotlib window), **Browser** (opens a chart or an algorithm animation in the browser), **Saves file**, **Internet** (calls an API), and **Input** (asks for a typed reply). Each has a tooltip.
* The **Visualize** button appears only on algorithm steps, and opens the step-through animation in the browser.
* For a step that saves a file, the **View file** button opens the newest file the run wrote. Text files such as `.json` open in Notepad.
* Warnings from a run, such as unittest summaries, appear in amber. Uncaught errors appear in red.

#### Steps you won't see as steps

Some folders have lesson text but no runnable code. These show a `# No source script for this lesson` placeholder, and Run is disabled. Helper scripts such as S10's `main.py`, S12's `prep_tables.py`, S17's `login.py`, and S18's `main.py` are not listed as steps.

C code samples (`.c` files) are shown read-only in the Source tab. The runner doesn't compile or run C.

#### Popping out and themes

Press **Pop out** in the top-right corner to open the lesson in its own window beside the main one. Use the dock icon in that window, or close it, to return the lesson to the Lesson tab. Closing the main window also closes a popped-out lesson.

The sun and moon switch in the title bar toggles dark and light themes.

#### Keyboard shortcuts

| Key | Action |
|---|---|
| F5 | Run the current step |
| Escape | Cancel a run, or reset the editor when it has edits |
| Ctrl+Shift+Enter | Continue past a pause |

#### Troubleshooting

* **A lesson shows "could not be rendered" in the output:** the traceback follows the message. Note the step and the error, and report them.
* **Math or code colors are missing:** the `vendor/` folder is probably not set up. See the lesson runner README.
* **The code font is not Cascadia Mono:** Cascadia Mono is used when installed. Otherwise the runner falls back to Cascadia Code, JetBrains Mono, or Consolas.

The runner's source code is in the `lesson-runner/` folder. The Tkinter version it replaced is in `lesson-runner-tk/` for reference.

### Running lessons directly

Every lesson step is a standalone `.py` file. You can run any of them directly:

```bash
python part-i-basics/ch02-fundamentals/lessons/01_hello_with_variable.py
```

Or open the folder in VS Code and use the Run button or the Code Runner extension.

---

## Repository structure

```
training-python/
|- resources/
|  |- setup/                     - Workstation and Python setup guides
|- part-i-basics/                - Chapters 1-11: language fundamentals
|  |- ch01-hello/
|  |- ch02-fundamentals/
|  |- ...
|  |- ch11-testing/
|- part-ii-projects/             - Chapters 12-20: three substantial projects
|  |- making-a-game/            - Ch12-14: game development with pygame
|  |- data-visualization/        - Ch15-17: charts and APIs with matplotlib and plotly
|  |- web-applications/          - Ch18-20: web development with Django
|- part-iii-beyond-the-book/     - Supplemental topics beyond the textbook
|  |- s01-command-line-arguments/
|  |- s02-recursion/
|  |- ...                        - 19+ supplemental topics
|- lesson-runner/                - Qt desktop lesson runner application
```

### Part I - Basics (Chapters 1-11)

Each chapter folder contains:
- `lessons/` - numbered lesson `.md` and `.py` pairs, one concept per step
- `try-it-yourself/` - exercise answers (Scott's solutions to the textbook exercises)
- `textbook-downloads/` - adapted code from the textbook's downloadable samples

| Chapter | Topic |
|---|---|
| `ch01-hello` | Getting started: the Python interpreter, your first program |
| `ch02-fundamentals` | Variables, strings, numbers, type casting, comments |
| `ch03-lists` | Lists: creation, access, modification, sorting |
| `ch04-using-lists` | Looping, slicing, tuples, list comprehensions |
| `ch05-boolean-logic` | Conditionals, comparison operators, boolean expressions |
| `ch06-dictionaries` | Dictionaries: creation, access, nesting, looping |
| `ch07-more-functionality` | User input, while loops, break and continue |
| `ch08-functions` | Functions, arguments, return values, modules |
| `ch09-classes` | Classes, instances, inheritance, importing |
| `ch10-files` | File I/O, exceptions, JSON |
| `ch11-testing` | pytest: unit tests, fixtures, test organization |

### Part II - Projects

| Folder | Topic |
|---|---|
| `making-a-game/` | pygame game development - sprite-based game with a ship, bullets, and alien fleet |
| `data-visualization/` | matplotlib, plotly, and the requests library - charts, APIs, and live data |
| `web-applications/` | Django chapters 18-20: the Learning Log, with models, forms, user accounts, Bootstrap styling, and optional deployment |

### Part III - Beyond the Book

Supplemental topics added by Scott that go beyond what the textbook covers.

| Folder | Topic |
|---|---|
| `s01-command-line-arguments` | Argument parsing with `argparse` |
| `s02-recursion` | Recursive algorithms and call stack mechanics |
| `s03-regular-expressions` | Pattern matching with the `re` module |
| `s04-big-o-complexity` | Algorithmic complexity and Big-O notation |
| `s05-bitwise-operations` | Bitwise operators and common patterns |
| `s06-dataclasses` | Python dataclasses |
| `s07-string-formatting` | f-strings, format(), template strings |
| `s08-closures` | Closures and the enclosing scope |
| `s09-enumerations` | Python `Enum` and `IntEnum` |
| `s10-web-scraping` | Scraping with `BeautifulSoup` and `requests` |
| `s11-lambdas` | Lambda functions and functional patterns |
| `s12-mysql-databases` | MySQL connectivity with `mysql-connector-python` |
| `s13-publish-a-library` | Packaging and publishing to PyPI (using `sm-utils` as the example) |
| `s14-numpy` | NumPy arrays and operations |
| `s15-pandas` | Pandas DataFrames and data analysis |
| `s16-scipy` | SciPy for scientific computing |
| `s17-mongodb` | MongoDB with `pymongo` |
| `s18-trie` | Trie data structure implementation |
| `s19-tkinter` | Tkinter GUI programming: windows, widgets, layout, events, canvas, and a to-do list |
| `s20-card-games` | OOP design in practice: Card, Deck, Hand, and a Blackjack implementation |
| `s21-morse-code` | Trie-based Morse code encoder/decoder |
| `s22-rochambeau` | Rock-paper-scissors: clean OOP design in a small project |
| `s23-game-of-life` | Conway's Game of Life: simulation and data-driven design |
| `s24-built-ins` | Useful built-in functions: `copy`, `id`, `setdefault`, and more |
| `s25-flask-learning-log` | The Learning Log rebuilt with Flask and SQLAlchemy: routes, templates, accounts, ownership, public topics, and production readiness |

### Lesson Runner

| Folder | Contents |
|---|---|
| `lesson-runner/` | Qt desktop application for browsing and running lessons interactively |

---

## sm-utils

Several lessons use `sm-utils`, a small utility library published to PyPI by Scott McLean. It provides helper functions used throughout the training examples: a `@timer` decorator, relative path helpers, a `pause()` function, `clear_terminal()`, and execution counters.

- PyPI: [sm-utils](https://pypi.org/project/sm-utils/)
- Install: `pip install sm-utils`

---

## Authorship note

This training curriculum was originally developed from my personal Python learning notes and has been cleaned up, extended, and standardized for internal use at DataBank. As with the C# training, I used generative AI in places for code review, cleanup, and turning rough notes into readable documentation.

~ Scott McLean, 2026

---

## Version history

| Date | Changes |
|---|---|
| 10/10/2026 | Initial migration from personal repository. New folder structure, README, CHANGELOG. |

---

## Contact

- [Scott McLean](mailto:smclean@databankimx.com)
- [Dev Team](mailto:development@databankimx.com)
