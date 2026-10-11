# DataBank IMX - Python Developer Training

## License and Support

This repository is provided under the [MIT License](LICENSE). You are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell the materials in this repository, subject to the terms of that license.

This repository is provided for training and reference purposes only. DataBank IMX does not provide warranties, guarantees, maintenance, troubleshooting, implementation assistance, or technical support for this code or its use. Use it in any way permitted by the MIT License, but you are responsible for evaluating, adapting, testing, and supporting any use of it in your own environment.

---

## What is this repository for?

- Python developer training curriculum for DataBank IMX
- Chapter-by-chapter lesson files, code samples, and exercises covering Python fundamentals through advanced topics, based on the *Python Crash Course* textbook (3rd edition) by Eric Matthes
- Extended with a substantial "Beyond the Book" supplemental track covering topics not addressed in the textbook
- Includes a Python/Tkinter lesson runner for navigating and running lessons interactively

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

See the [Workstation Setup](resources/setup/01-workstation-setup.md) and [Python Setup](resources/setup/02-python-setup.md) guides in the `resources/setup/` folder for full step-by-step instructions.

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
| `django` | Part II - Web Applications (Ch18-20) | `pip install django` |

You can wait until the relevant chapter to install each library, or install everything up front. There is no harm in installing all of them now.

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

The lesson runner is a Python/Tkinter desktop application that lets you browse chapters, read lesson notes, and run code examples interactively.

```bash
python lesson-runner/main.py
```

Select a chapter in the left panel, choose a lesson step, and click Run. The lesson notes and code output appear side by side.

See [lesson-runner/README.md](lesson-runner/README.md) for full documentation. The lesson runner's own source code is also covered as a supplemental lesson in Part III, making it a practical Tkinter example in its own right.

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
|  |- alien-invasion/            - Ch12-14: game development with pygame
|  |- data-visualization/        - Ch15-17: charts and APIs with matplotlib and plotly
|  |- web-applications/          - Ch18-20: web development with Django
|- part-iii-beyond-the-book/     - Supplemental topics beyond the textbook
|  |- s01-command-line-args/
|  |- s02-recursion/
|  |- ...                        - 19+ supplemental topics
|- lesson-runner/                - Python/Tkinter lesson runner application
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
| `alien-invasion/` | pygame game development - sprite-based game with a ship, bullets, and alien fleet |
| `data-visualization/` | matplotlib, plotly, and the requests library - charts, APIs, and live data |
| `web-applications/` | Django - models, views, templates, user authentication, deployment |

### Part III - Beyond the Book

Supplemental topics added by Scott that go beyond what the textbook covers.

| Folder | Topic |
|---|---|
| `s01-command-line-args` | Argument parsing with `argparse` |
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
| `s19-filter` | The `filter()` function and functional filtering patterns |
| `s20-card-games` | OOP design in practice: Card, Deck, Hand, and a Blackjack implementation |
| `s21-morse-code` | Trie-based Morse code encoder/decoder |
| `s22-rochambeau` | Rock-paper-scissors: clean OOP design in a small project |
| `s23-game-of-life` | Conway's Game of Life: simulation and data-driven design |
| `s24-useful-builtins` | Useful built-in functions: `copy`, `id`, `setdefault`, and more |

### Lesson Runner

| Folder | Contents |
|---|---|
| `lesson-runner/` | Tkinter desktop application for browsing and running lessons interactively |

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
