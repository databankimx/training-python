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

### Changed

- Lesson runner: the Qt version replaces the Tkinter runner as the main runner. The Tkinter version is kept in `lesson-runner-tk/` for reference
- Lesson runner: step titles use the lesson's first heading with Markdown markup removed; leading numbers and letter prefixes are dropped from file-name titles
- Lesson runner: a Python script with a matching lesson file is a step, even without a `__main__` guard
- Lesson runner: Part I lessons are attached to their scripts, including scripts that share one lesson file (for example S09 importing classes)
- Lesson runner: chapter tree starts collapsed; selecting a chapter with no steps of its own moves to its first sub-chapter
- Lesson runner: C samples are highlighted as C in the source editor
- Lesson runner: the DataBank logo is drawn from its SVG paths as vector graphics, for the nav header and window icon

### Fixed

- Lesson runner: lesson text now updates when moving between steps in Part I chapters
- Lesson runner: inline code in headings takes the heading's size
- Lesson runner: LaTeX that MathJax doesn't define (`\Larr`, `\Z`, `\N`, `\R`, `\Q`, and `\^`) now renders
- Lesson runner: empty spacer rows at the top of Markdown tables are no longer shown
- Lesson runner: closing the main window also closes a popped-out lesson
- `s05-bitwise-operations`: LaTeX expression `\^` replaced by the XOR symbol inside maths; note added to `16_bitwise_xor.md` explaining the symbol

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
