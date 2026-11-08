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
import traceback

CONTROL = "##LRUN##"
# Written to stderr just before an uncaught error's traceback, so the runner can show it
#     in the error color.
ERROR_MARK = CONTROL + json.dumps({"kind": "error"})


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


def _prepare_audio(source: str) -> None:
    """Let pygame's sound calls succeed on a machine with no sound device, such as a virtual machine.

    If the lesson uses pygame and the sound device can't start, pygame is told to use its silent driver. The mixer
    still starts, so music and sound calls work and play nothing. A machine with a sound device is unchanged.
    """
    if "pygame" not in source or "SDL_AUDIODRIVER" in os.environ:
        return
    try:
        import pygame  # pylint: disable=import-outside-toplevel
    except ImportError:
        return
    try:
        pygame.mixer.init()
        pygame.mixer.quit()
    except pygame.error:
        os.environ["SDL_AUDIODRIVER"] = "dummy"


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
    _prepare_audio(source)
    namespace: dict[str, object] = {"__name__": "__main__", "__file__": original, "__builtins__": builtins}
    try:
        code = compile(source, original, "exec")
        #pylint: disable=exec-used
        exec(code, namespace)  # noqa: S102 - running lesson code is the purpose of this tool
    except SystemExit as exit_request: #pylint: disable=catching-non-exception
        code_value = exit_request.code
        return code_value if isinstance(code_value, int) else 0
    except BaseException:  # pylint: disable=broad-exception-caught
        sys.stderr.write(ERROR_MARK + "\n")
        sys.stderr.flush()
        traceback.print_exc()
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
