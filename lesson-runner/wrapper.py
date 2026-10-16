"""Child-process wrapper: runs one lesson step and routes pause, clear and input to the runner.

Usage (called by runner.py, not by hand):

    python wrapper.py <original_step_path> <source_file> [args...]

``source_file`` holds the code to run. It may be an edited copy of the step,
but ``original_step_path`` is used as the filename, so ``__file__`` and any
relative paths still point at the real lesson folder.

Control messages are written to stdout as a single line that starts with
``##LRUN##`` followed by JSON. Ordinary output is passed through unchanged.
"""

from __future__ import annotations

import builtins
import json
import os
import sys

CONTROL = "##LRUN##"


def _emit(kind: str, **fields: str) -> None:
    """Send one control message to the runner."""
    sys.stdout.write(CONTROL + json.dumps({"kind": kind, **fields}) + "\n")
    sys.stdout.flush()


def _input(prompt: object = "") -> str:
    """Replacement for input(): ask the runner for a line of text."""
    _emit("input", prompt=str(prompt))
    line = sys.stdin.readline()
    if line == "":
        raise EOFError("No input available")
    return line.rstrip("\r\n")


def _pause(*_args: object, **_kwargs: object) -> None:
    """Replacement for sm_utils.pause(): wait for the Continue button."""
    _emit("pause")
    sys.stdin.readline()


def _clear(*_args: object, **_kwargs: object) -> None:
    """Replacement for sm_utils.clear_terminal(): clear the output pane."""
    _emit("clear")


def _patch_sm_utils() -> None:
    """Route the sm_utils helpers used by the lessons to the runner."""
    try:
        import sm_utils #pylint: disable=import-outside-toplevel
    except ImportError:
        return
    sm_utils.pause = _pause
    sm_utils.clear_terminal = _clear


def main() -> int:
    """Run the step inside this process and return its exit status."""
    original, source_file, *rest = sys.argv[1:]
    folder = os.path.dirname(original)

    sys.argv = [original, *rest]
    sys.path.insert(0, folder)
    _patch_sm_utils()
    builtins.input = _input

    with open(source_file, encoding="utf-8") as handle:
        source = handle.read()
    code = compile(source, original, "exec")
    namespace = {"__name__": "__main__", "__file__": original, "__builtins__": builtins}
    try:
        #pylint: disable=exec-used
        exec(code, namespace)  # noqa: S102 - running lesson code is the purpose of this tool
    except SystemExit as exit_request: #pylint: disable=catching-non-exception
        code_value = exit_request.code
        return code_value if isinstance(code_value, int) else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
