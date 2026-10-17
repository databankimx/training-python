# Changelog

All notable changes to the DataBank IMX Python Developer Training repository are documented here.

## Rules and Conventions

This file follows the [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) format.
Versions follow [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

### What gets a changelog entry

- New files, chapters, or supplemental topics
- Structural or organizational changes to the repository
- Lesson runner changes
- Major content updates (new Python version coverage, significant lesson rewrites)
- Major policy changes

### What does not

- Prose edits, typo fixes, and minor wording improvements within existing documents
- Formatting-only changes

---

## [Unreleased]

### Added

- `part-ii-projects/data-visualization/` - 2nd and 3rd Editions: lessons and try-it-yourself steps for Ch15 (generating data), Ch16 (downloading data), and Ch17 (working with APIs), with the matching data files and images
- `part-ii-projects/data-visualization/github-token-setup.md` - guide to creating a classic GitHub token and setting the `GITHUB_TRAINING_TOKEN` user environment variable
- Chapter 17 scripts that call the GitHub API read `GITHUB_TRAINING_TOKEN` when it is set, which raises the rate limit from 60 to 5,000 requests per hour. They run without it as before
- Lesson runner: Part II - Projects in the chapter tree, between Part I and Part III. Making a Game and Web Applications show a "Not yet implemented" placeholder
- Lesson runner: a Setup entry under Data Visualization that shows the GitHub token guide
- Lesson runner: badges under the step title (Window, Browser, Saves file, Internet, Input), with glyphs, a background color, and tooltips
- Lesson runner: a View file button after a run that saves a file. Text files open in Notepad
- Lesson runner: a hint in the output pane when a run fails because GitHub refused a request for rate limits
- Lesson runner: tooltips on the glyph controls and buttons
- Lesson runner: `files_watch.py` for finding the files a run writes
- Lesson runner: `config.py`, `theme.py`, `icons.py`, `source_tools.py`, `widgets.py`, `window_layout.py`, `theming.py`, `navigation.py`, `source_panel.py`, `output_panel.py`, `run_control.py`, and `lesson_view.py`, split out of `app.py`

- `.github/` structure: `CODEOWNERS`, `instructions/copilot-instructions.md`, `instructions/sonarqube_mcp.instructions.md`, `workflows/sonarqube.yml`, `workflows/standards-policy.yml`, `standards.yml`
- `sonar-project.properties` - excludes all `textbook-downloads/` folders from SonarQube analysis and coverage
- `.github/standards.yml` - excludes all `textbook-downloads/` folders from the standards-policy checker
- `part-iii-beyond-the-book/s19-tkinter/` - new chapter: introduction and nine Tkinter lessons (windows, labels and buttons, `pack()`, `grid()`, text entry, events, canvas and animation, menus and dialogs, and a to-do list)
- `part-iii-beyond-the-book/s20-card-games/blackjack.md` and `test.md` - lesson files for the Blackjack and Test steps
- `lesson-runner/` - Qt-based lesson runner (`app.py`): chapter and step navigation, source editing with line numbers and highlighting, run and input handling, rendered lessons with MathJax and Prism, pop-out lesson window, and dark and light themes
- Lesson runner: syntax highlighting for C samples, with a note that the runner cannot compile or run C
- Lesson runner: Part I chapter tree nests `try-it-yourself` and the chapter 11 editions under each chapter
- Lesson runner: Part III chapter tree nests sub-folders under their chapter (for example S13 and S14)
- Lesson runner: helper scripts hidden from the step list (S10 `main.py`, S12 `prep_tables.py`, S17 `login.py`, S18 `main.py`)
- `part-iii-beyond-the-book/s04-big-o-complexity/visualizations/` - step-through algorithm visualizations for the nine S04 algorithms (player, theme, and one step generator per algorithm), opened from the lesson runner's Visualize button
- Lesson runner: Visualize button opens a step's algorithm in the browser, for the S04 steps

### Changed

- Lesson runner: `app.py` is now the entry point. The window's behavior is split across the modules listed under Added
- Lesson runner: Part II sits between Part I and Part III in the chapter tree
- Lesson runner: top-level Part menus start collapsed
- Lesson runner: code blocks wrap at the pane edge instead of scrolling sideways, and lesson images scale to the pane width
- Lesson runner: a clear-screen code (`ESC c`) clears the output pane
- Lesson runner: warnings from a run (stderr that is not an uncaught error) appear in amber, not red
- Lesson runner: the Visualize button appears only on algorithm steps
- `part-iii-beyond-the-book/s04-big-o-complexity/html/` removed and replaced by `visualizations/`. The S04 lessons now point to the Visualize button instead of the old HTML files
- Lesson runner: the Qt version replaces the Tkinter runner as the main runner. The Tkinter version is kept in `lesson-runner-tk/` for reference
- Lesson runner: step titles use the lesson's first heading with Markdown markup removed; leading numbers and letter prefixes are dropped from file-name titles
- Lesson runner: a Python script with a matching lesson file is a step, even without a `__main__` guard
- Lesson runner: Part I lessons are attached to their scripts, including scripts that share one lesson file (for example S09 importing classes)
- Lesson runner: chapter tree starts collapsed; selecting a chapter with no steps of its own moves to its first sub-chapter
- Lesson runner: C samples are highlighted as C in the source editor
- Lesson runner: the DataBank logo is drawn from its SVG paths as vector graphics, for the nav header and window icon
- Lesson runner: the source pane omits `#pylint` and `#NOSONAR` comments
- Lesson runner: the Lesson tab opens on `part-i-basics/00_what_is_python.md` at launch, before any step is selected
- Lesson runner: steps that share a lesson file are indented under the first one in the step list
- Lesson runner: Part I lessons whose names contain "bonus" appear as steps even without a script
- Lesson runner: Part III chapter names no longer shift left, so the tree uses the same layout as Part I

### Fixed

- Part II unittest step runs its tests: `unittest.main()` searched the runner's `__main__` module and found no tests. The script now runs its test case directly, with output to stdout
- Part II plotly charts use the current title syntax (`title={"text": ..., "font": ...}`), because `titlefont` is no longer accepted
- Part II data files are read from the lowercase `data` folder
- Part II random-walk scripts: the figure variable `fix` is now `fig`
- Part II ch17 try-it-yourself: an `input()` call with two arguments no longer raises `TypeError`
- 3rd Edition ch17 lesson 2.13: stories without a comment count no longer stop the script with a `KeyError`
- 3rd Edition ch15 lesson 2.4: added a note on the `c=` warning from matplotlib and how to remove it
- Lesson runner: lesson text now updates when moving between steps in Part I chapters
- Lesson runner: inline code in headings takes the heading's size
- Lesson runner: LaTeX that MathJax doesn't define (`\Larr`, `\Z`, `\N`, `\R`, `\Q`, and `\^`) now renders
- Lesson runner: empty spacer rows at the top of Markdown tables are no longer shown
- Lesson runner: closing the main window also closes a popped-out lesson
- `s05-bitwise-operations`: LaTeX expression `\^` replaced by the XOR symbol inside math; note added to `16_bitwise_xor.md` explaining the symbol
- Lesson runner: Python scripts without a numbered name or `__main__` guard (for example S24's built-in examples) show their code when they have a matching lesson file
- Lesson runner: the Visualize button writes the chosen algorithm to `current-algorithm.js` before opening the player, because Windows drops query strings in file addresses
- `s04-big-o-complexity/09_shell_sort.md`: the gap sequence text now matches the code (the smallest power of two at or above *n*, minus one)
- Lesson runner: Python scripts without a numbered name or `__main__` guard (for example S24's built-in examples) show their code when they have a matching lesson file
- Lesson runner: the Visualize button writes the chosen algorithm to `current-algorithm.js` before opening the player, because Windows drops query strings in file addresses
- `s04-big-o-complexity/09_shell_sort.md`: the gap sequence text now matches the code (the smallest power of two at or above *n*, minus one)

---

## [1.0.0] - 2026-10-10

### Added

- Repository structure: `part-i-basics/`, `part-ii-projects/`, `part-iii-beyond-the-book/`, `lesson-runner/`, `resources/setup/`
- `README.md` - full project README modelled on the C# training repository
- `CHANGELOG.md` - this file
- `development-rules-of-engagement.md` - shared policy document covering custom code obligations
- Migrated from personal repository (`python-crash-course`) to DataBank IMX organization

[Unreleased]: https://github.com/databankimx/training-python/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/databankimx/training-python/releases/tag/v1.0.0
