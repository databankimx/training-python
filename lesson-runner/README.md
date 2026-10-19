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

## Web chapters (Django and Flask)

The web chapters are the Learning Log in Django (Part II, Web Applications, chapters 18 to 20) and in Flask (Part III, S25). Each step is built and run by
`part-ii-projects\web-applications\build_stage.py`, and the runner shows the build in the Output pane.

* **Environment:** the web chapters use `part-ii-projects\web-applications\.venv`, not the environment that runs the runner. Before each build, the runner
  checks that the environment exists, runs, and has the packages it needs. If not, the Output pane shows the commands to fix it, which can be copied.
  Activating the environment isn't needed. See the root QUICKSTART, step 7.
* **Admin account:** the first web run in a session asks for an admin username and password. The build creates that account in the local database.
* **Start page:** when the server is ready, the browser opens at the step's `start.txt` page. A step that needs sign-in opens its login page.
* **Try it Yourself:** each web chapter has a **Try it Yourself** node. Exercises that are projects or updates run from there. Text-only exercises open as lessons.
* **Source tab:** web steps show a read-only listing of what the step adds or changes. New files appear in full, and changed files as diffs with `--snip--`
  between changes. The Python steps keep their editable source.
* **Stopping:** Escape, selecting another step or chapter, or closing the window stops a running server. A server is also stopped if the runner crashes,
  because its processes are tied to the runner.
* **Port 8000:** if something is already listening on port 8000, the runner asks before stopping it.

## Shortcuts

| Key | Action |
|---|---|
| F5 | Run the current step |
| Escape | Cancel a run, or reset the editor when it has edits |
| Ctrl+Shift+Enter | Continue past a pause |

