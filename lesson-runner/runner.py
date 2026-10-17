"""Run one lesson step in a child process and stream its events to the window.

The window polls ``StepRun.events`` on the Tk thread. Each event is a
``(kind, value)`` tuple:

* ``("out", text)``: a line of normal output
* ``("warn", text)``: a line of warning output, such as a unittest summary or a warning
* ``("err", text)``: a line of error output, such as an uncaught traceback
* ``("clear", "")``: clear the output pane
* ``("pause", "")``: the step is waiting for Continue
* ``("input", prompt)``: the step is waiting for a line of text
* ``("done", (returncode, seconds))``: the step has finished
"""

from __future__ import annotations

import json
import os
import queue
import subprocess
import sys
import tempfile
import threading
import time
from pathlib import Path

#pylint: disable=attribute-defined-outside-init, line-too-long, too-many-instance-attributes

WRAPPER = Path(__file__).resolve().with_name("wrapper.py")
CONTROL = "##LRUN##"
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)


class StepRun:
    """One execution of one step, possibly with edited source."""

    def __init__(self, step_path: Path, source: str, args: list[str]) -> None:
        self.step_path = step_path
        self.events: queue.Queue = queue.Queue()
        self._source = source
        self._args = args
        self._temp: Path | None = None
        self._proc: subprocess.Popen | None = None
        self._started = 0.0
        self.cancelled = False
        self._in_error = False

    def start(self) -> None:
        """Write the source to a temporary file and launch the wrapper."""
        handle, name = tempfile.mkstemp(suffix=".py", prefix="lesson_src_")
        with os.fdopen(handle, "w", encoding="utf-8") as file:
            file.write(self._source)
        self._temp = Path(name)

        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        env["PYTHONUNBUFFERED"] = "1"
        command = [sys.executable, "-u", str(WRAPPER), str(self.step_path),
                   str(self._temp), *self._args]

        self._started = time.perf_counter()
        self._proc = subprocess.Popen(
            command,
            cwd=self.step_path.parent,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            env=env,
            creationflags=NO_WINDOW,
        )
        self._readers = [
            threading.Thread(target=self._pump, args=(self._proc.stdout, self._on_stdout), daemon=True),
            threading.Thread(target=self._pump, args=(self._proc.stderr, self._on_stderr), daemon=True),
        ]
        for reader in self._readers:
            reader.start()
        threading.Thread(target=self._wait, daemon=True).start()

    def send(self, text: str) -> None:
        """Send one line of text to the step's standard input."""
        if self._proc is None or self._proc.poll() is not None:
            return
        try:
            self._proc.stdin.write(text + "\n")
            self._proc.stdin.flush()
        except (OSError, ValueError):
            pass

    def cancel(self) -> None:
        """Stop the running step."""
        if self._proc is not None and self._proc.poll() is None:
            self.cancelled = True
            self._proc.kill()

    # Background threads -------------------------------------------------

    def _pump(self, stream, handler) -> None:
        for line in stream:
            handler(line.rstrip("\r\n"))

    def _on_stdout(self, line: str) -> None:
        if not line.startswith(CONTROL):
            # ESC c is the terminal "clear screen" code. The output pane clears instead of printing it.
            if "\x1bc" in line:
                self.events.put(("clear", ""))
                line = line.rpartition("\x1bc")[2]
                if not line:
                    return
            self.events.put(("out", line))
            return
        try:
            message = json.loads(line[len(CONTROL):])
        except ValueError:
            self.events.put(("out", line))
            return
        kind = message.get("kind", "")
        if kind == "input":
            self.events.put(("input", message.get("prompt", "")))
        elif kind == "pause":
            self.events.put(("pause", ""))
        elif kind == "clear":
            self.events.put(("clear", ""))

    def _on_stderr(self, line: str) -> None:
        if line.startswith(CONTROL):
            # An uncaught error: its traceback follows, and is shown in the error color.
            self._in_error = True
            return
        self.events.put(("err" if self._in_error else "warn", line))

    def _wait(self) -> None:
        returncode = self._proc.wait()
        for reader in self._readers:
            reader.join()
        elapsed = time.perf_counter() - self._started
        if self._temp is not None:
            try:
                self._temp.unlink()
            except OSError:
                pass
        self.events.put(("done", (returncode, elapsed)))
