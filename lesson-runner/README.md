# Lesson Runner (Qt WebEngine)

The Qt version of the lesson runner. It has everything it needs in this folder.

| File | Purpose |
|---|---|
| `app.py` | The main window: navigation, title bar, output, source and lesson |
| `discovery.py` | Finds chapters and steps under Part I and Part III |
| `runner.py` | Starts a step in a child process and passes its events to the window |
| `wrapper.py` | Runs inside the child process; routes pause, clear and input |
| `syntax.py` | Python token colouring for the source editor |
| `logo.py` | The DataBank logo, as polygons for the nav header and window icon |
| `render.py` | Renders lesson Markdown to HTML (MathJax maths, Prism code) |
| `vendor/` | MathJax and Prism, loaded by the lesson pages (see setup) |

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
highlighting and reset, rendered lessons (MathJax maths, Prism code in Visual
Studio colours), pop-out lesson window with dock control, input dialog, and pause
handling.

The tkinter version of the runner is kept in `lesson-runner-tk` for reference.

Not yet checked on your machine: the pop-out and dock controls, the first-lesson
flash, and the copy tick.
