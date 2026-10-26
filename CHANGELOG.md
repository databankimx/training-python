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

## [1.0.0] - 2026-10-23

### Added

- `part-iii-beyond-the-book/s26-itertools/` - new chapter: an introduction and seven lessons on the `itertools` module (infinite iterators, `chain` and `islice`, `accumulate`, combinations and permutations, `groupby`, filtering, and `zip_longest` and `starmap`)
- `part-iii-beyond-the-book/s27-functools/` - new chapter: an introduction and five lessons on the `functools` module (`lru_cache`, `partial`, `reduce`, `wraps`, and `singledispatch`)
- `part-iii-beyond-the-book/s16-scipy/` - six new lessons: `09_integrate`, `10_linalg`, `11_stats_distributions`, `12_fft`, `13_signal_peaks`, and `14_special`. The introduction lists all fourteen lessons, and the study warning has been removed
- `part-iii-beyond-the-book/s24-built-ins/` - three new lessons: `the_collections_module`, `any_and_all`, and `the_datetime_module`
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
- Lesson runner: window code split out of `app.py` into the `ui/` package, and logic that doesn't need the window into `core/` (discovery, runner, wrapper, files watch, source tools). Lesson rendering is in `render/`

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

- `sm-utils` 0.2.9 published to PyPI and Test PyPI. The `set_path()` fix and the call-time default resolution are described under Fixed. `part-iii-beyond-the-book/s13-publish-a-library/` is updated to match
- Part III `s24-built-ins` examples restructured into named functions with a `main()` entry point and a double-quoted `__name__` guard, matching the `s26-itertools` and `s27-functools` scripts
- Lesson runner: type hints added across `config.py`, `core/`, `render/`, and `ui/`, and `logo.py` no longer imports `tkinter`. The Tkinter-only helpers `draw_on_canvas()` and `icon_photo()` were removed, since nothing called them
- `00_beyond_the_book.md`: the topic list now includes Tkinter, Flask, Itertools, and Functools, and the SciPy entry no longer shows the incomplete-lesson marker
- Lesson runner: modules grouped into `core/`, `ui/` and `render/` packages, with `config.py` and `app.py` at the top. `discovery.py` finds the repository root from its new location
- Lesson runner: Part II sits between Part I and Part III in the chapter tree
- Lesson runner: top-level Part menus start collapsed
- Lesson runner: code blocks wrap at the pane edge instead of scrolling sideways, and lesson images scale to the pane width
- Lesson runner: a clear-screen code (`ESC c`) clears the output pane
- Lesson runner: warnings from a run (stderr that is not an uncaught error) appear in amber, not red
- Lesson runner: the Visualize button appears only on algorithm steps
- `part-iii-beyond-the-book/s04-big-o-complexity/html/` removed and replaced by `visualizations/`. The S04 lessons now point to the Visualize button instead of the old HTML files
- Lesson runner: the Qt version replaces the earlier Tkinter runner as the main runner
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

- Lesson runner: Part III chapters are in numerical order. The Flask chapter (S25) was listed after S24 and S26, and now sits in sequence
- `s13-publish-a-library` / `sm-utils` 0.2.9: `set_path(folder)` returned without setting the default folder; `dir_path()` and `file_path()` captured the default when the module was imported; `RelativePath` raised `AttributeError` when no JSON file existed. All three are fixed
- `s14-numpy/03-numpy-ufunc`: `ord_suffix()` in `utility_functions.py` returned `suf[n]` instead of `suf[m]`, so numbers such as 23 raised `IndexError`
- `s15-pandas`: `clean_csv.py`'s `drop_duplicates()` did not modify the DataFrame (missing `inplace=True`), so duplicate rows stayed in the cleaned data
- `s18-trie`: `list_words()` called without a prefix passed `None` to `show_all_words()`, which raised `TypeError`
- `s20-card-games`: `Hand.value` had a setter that took no argument. The property is now read-only
- `s21-morse-code`: `decode_code()` raised an error for input whose path runs off the tree (such as `......`) or ends at a node with no character (such as `----`). It now returns the unknown-character symbol `□`
- `s24-built-ins`: the clipboard lesson said that pasting could return text copied elsewhere. The script copies `"Hello"` first, so the lesson now describes that behavior
- `00_beyond_the_book.md`: the Filter link pointed to a folder that doesn't exist (`s19-filter`). It now points to `s19-tkinter`
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
---

## [0.0.9] - 2026-10-10

### Added

- Repository structure: `part-i-basics/`, `part-ii-projects/`, `part-iii-beyond-the-book/`, `lesson-runner/`, `resources/setup/`
- `README.md` - full project README modelled on the C# training repository
- `CHANGELOG.md` - this file
- `development-rules-of-engagement.md` - shared policy document covering custom code obligations
- Migrated from personal repository (`python-crash-course`) to DataBank IMX organization

[1.0.0]: https://github.com/databankimx/training-python/compare/v0.0.9...v1.0.0
[0.0.9]: https://github.com/databankimx/training-python/releases/tag/v0.0.9
