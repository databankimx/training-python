# Lesson Runner (Qt WebEngine)

The Qt version of the lesson runner. It has the same features as the tkinter
runner in `lesson-runner`, with lessons rendered in Qt WebEngine by MathJax and
Prism, using the same Markdown renderer as the spike.

## Setup

1. Install the vendor files once (needs Node.js), as for the spike:

   ```pwsh
   cd C:\Development\training\training-python\lesson-runner-qt-spike\vendor
   npm init -y
   npm install mathjax@3 prismjs@1
   ```

2. Install the Python packages:

   ```pwsh
   cd C:\Development\training\training-python\lesson-runner-qt
   python -m pip install -r requirements.txt
   ```

3. Run:

   ```pwsh
   python app.py
   ```

## Shared code

For now this app imports from two sibling folders:

- `lesson-runner`: discovery, the child-process runner and wrapper, and the Python
  syntax rules
- `lesson-runner-qt-spike`: the Markdown renderer and the vendor files

Once this version matches the tkinter runner, move those files into this folder
and delete `lesson-runner` and the spike.

## Shortcuts

| Key | Action |
|---|---|
| F5 | Run the current step |
| Escape | Cancel a run, or reset the editor when it has edits |
| Ctrl+Shift+Enter | Continue past a pause |

## Status

Built: the chapter tree and step list (60/40), title bar with theme switch and
Run, args, output with Continue, Copy and Clear, source editor with line numbers,
highlighting and reset, rendered lessons with MathJax, Prism, and the lesson's
own CSS, pop-out lesson window, input dialog, and pause handling.

Not yet checked: everything above has not been run. Expect a round of fixes on
the first run.
