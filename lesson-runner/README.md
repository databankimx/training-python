# Lesson Runner (Qt WebEngine)

The Qt version of the lesson runner. It has everything it needs in this folder.

The code is in three packages, all in this folder:

| Path | Purpose |
|---|---|
| `app.py` | Entry point: the main window class, which combines the `ui` mixins, and `main()` |
| `config.py` | Paths, color palettes, code fonts and the visualization table |
| `core/` | Logic that does not depend on the window (below) |
| `ui/` | The window and its widgets (below) |
| `render/` | Lesson rendering (below) |
| `vendor/` | MathJax and Prism, loaded by the lesson pages (see setup) |

`core/`:

| File | Purpose |
|---|---|
| `discovery.py` | Finds chapters and steps under Part I, Part II and Part III |
| `runner.py` | Starts a step in a child process and passes its events to the window |
| `wrapper.py` | Runs inside the child process; routes pause, clear and input |
| `files_watch.py` | Finds the files a run writes, and opens text files in Notepad |
| `source_tools.py` | Strips lint comments from source; works out a step's badges |

`ui/`:

| File | Purpose |
|---|---|
| `window_layout.py` | Builds the window's widgets and shortcuts (`LayoutMixin`) |
| `theming.py` | Applies the dark or light palette (`ThemeMixin`) |
| `navigation.py` | Chapter tree and step list (`NavigationMixin`) |
| `source_panel.py` | Loads a step into the editor and lesson; badges, reset, visualize (`SourcePanelMixin`) |
| `output_panel.py` | Output pane, clear and copy (`OutputMixin`) |
| `run_control.py` | Runs a step, answers input and pauses, reports the result (`RunMixin`) |
| `lesson_view.py` | Shows lessons, scrolls to the step, pop-out lesson (`LessonMixin`) |
| `widgets.py` | Theme switch, syntax highlighter, source editor, tree delegate, pop-out window |
| `theme.py` | Fonts and the application stylesheet |
| `icons.py` | Vector icons and the DataBank logo |
| `syntax.py` | Python and C token coloring for the source editor |
| `logo.py` | The DataBank logo, as polygons for the nav header and window icon |

`render/`:

| File | Purpose |
|---|---|
| `render.py` | Renders lesson Markdown to HTML (MathJax math, Prism code) |

## Setup

The `vendor` folder must contain `node_modules` with MathJax and Prism. It should
look like this:

```
vendor\
  node_modules\mathjax\es5\tex-svg.js
  node_modules\prismjs\prism.js
```

If it's missing, install it once (needs Node.js):

```pwsh
cd C:\Development\training\training-python\lesson-runner\vendor
npm init -y
npm install mathjax@3 prismjs@1
```

Then install the Python packages and run the app:

```pwsh
cd C:\Development\training\training-python\lesson-runner
python -m pip install -r requirements.txt
python app.py
```

## Shortcuts

| Key | Action |
|---|---|
| F5 | Run the current step |
| Escape | Cancel a run, or reset the editor when it has edits |
| Ctrl+Shift+Enter | Continue past a pause |

## Status

Built: the chapter tree and step list (60/40), title bar with theme switch and
Run, args, output with Continue, Copy and Clear, source editor with line numbers,
highlighting and reset, rendered lessons (MathJax math, Prism code in Visual
Studio colors), pop-out lesson window with dock control, input dialog, and pause
handling.

Part II: Data Visualization is shown by edition (2nd and 3rd), with each chapter's
lessons and Try it Yourself. Making a Game and Web Applications are placeholders
that say they are not yet implemented.

Badges under the step title say what a step does: Window (opens a matplotlib
window), Browser (opens a chart or an algorithm animation in the browser), Saves file, Internet (calls an
API), and Input (asks for a typed reply). Each badge and the other controls have a
tooltip. Tooltips hide themselves after a few seconds.

The tkinter version of the runner is kept in `lesson-runner-tk` for reference.

Not yet checked on your machine: the pop-out and dock controls, the first-lesson
flash, and the copy tick.
