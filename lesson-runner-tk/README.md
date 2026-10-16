# Lesson Runner (Python)

A tkinter port of the WPF `LessonRunner` app, for the Python training lessons in
`part-i-basics` and `part-iii-beyond-the-book`. Part II is not included.

## Running it

Use the interpreter that has `sm_utils` installed (the one you run the lessons with):

```pwsh
cd C:\Development\training\training-python\lesson-runner
python app.py
```

Each step runs in its own child process, in the step's folder, with the same
interpreter. Pauses and `input()` prompts are routed to the window.

## Files

| File | Purpose |
|---|---|
| `app.py` | The main window: navigation, title bar, args, output, source, lesson |
| `discovery.py` | Finds chapters and steps under Part I and Part III |
| `runner.py` | Starts a step in a child process and passes its events to the window |
| `wrapper.py` | Runs inside the child process. Routes `pause`, `clear_terminal`, and `input` |

## What a step is

Part I: a step is a runnable `.py` file in a folder. A file is runnable if its
name is numbered (`01_command_args.py`), it is `main.py`, or it has an
`if __name__ == "__main__":` guard. Support modules such as `utilities.py` and
`trie.py` are not steps. The lesson text for a step is the `.md` file with the
same name.

Part III: every lesson `.md` file in a folder is a step, in file-name order.

- A lesson with a matching `.py` script is a runnable step.
- A lesson with no script shows `# No source script for this lesson` and has no Run.
- A lesson with a matching `.c` sample shows the C code read-only, with no Run.
- A script with no lesson file is still a runnable step.

## Shortcuts

| Key | Action |
|---|---|
| F5 | Run the current step |
| Escape | Cancel a run, or reset the editor when it has edits |
| Ctrl+Shift+Enter | Continue past a pause |
| Up / Down | Move between steps when the step list has focus |

## Status

Done: discovery, running, output and errors, args, input dialog, pause and
Continue, editable source with highlighting, line numbers, dirty state and reset,
dark and light themes, copy for output, source and lesson, rendered lesson
Markdown, and the pop-out lesson window (Pop out / Dock).

Not yet done: the Copy confirmation is a label change on the button rather than
a toast, and the source tab has no dot (the edited marker is in the reset bar).

Not carried over: the visualization button and browser steps. The Python lessons
have neither.
