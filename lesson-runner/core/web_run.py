"""Run a web applications step: build it with build_stage.py, then keep its development server running.

The window polls ``WebRun.events`` in the same way as ``StepRun``. The events are:

* ``("out", text)``: a line of output
* ``("ready", url)``: the server has started at this address
* ``("done", (returncode, seconds))``: the build or server has stopped
"""

from __future__ import annotations

import os
import queue
import re
import socket
import subprocess
import sys
import threading
import time
from pathlib import Path

from core.job_object import contain

#pylint: disable=line-too-long

WEB_ROOT = Path(__file__).resolve().parents[2] / "part-ii-projects" / "web-applications"
NO_WINDOW = getattr(subprocess, "CREATE_NO_WINDOW", 0)
READY = re.compile(r"Starting development server at (http://\S+)")


def web_python() -> str:
    """The Python that runs the build: the web applications virtual environment when it exists.

    Django is installed there, not in the runner's own environment. Without it, the build fails with
    a message that says Django is missing.
    """
    venv_python = WEB_ROOT / ".venv" / "Scripts" / "python.exe"
    return str(venv_python) if venv_python.exists() else sys.executable


class WebRun:
    """One build-and-run of a web step, with the server's output streamed to the window."""

    def __init__(self, command: list[str], env: dict[str, str]) -> None:
        self.events: queue.Queue = queue.Queue()
        self._command = command
        self._extra_env = env
        self._proc: subprocess.Popen | None = None
        self._started = 0.0
        self.cancelled = False
        self.url: str | None = None

    def start(self) -> None:
        """Launch the build in the web applications folder."""
        env = os.environ.copy()
        env.update(self._extra_env)
        env["PYTHONUNBUFFERED"] = "1"
        env["PYTHONIOENCODING"] = "utf-8"

        self._started = time.perf_counter()
        self._proc = subprocess.Popen(
            self._command,
            cwd=WEB_ROOT,
            env=env,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            creationflags=NO_WINDOW,
        )
        contain(self._proc)
        threading.Thread(target=self._read_output, daemon=True).start()

    def send(self, text: str) -> None:
        """Web runs don't take input, so there's nothing to send."""

    def cancel(self) -> None:
        """Stop the build and the server. On Windows the whole process tree is stopped, so the server goes too."""
        if self._proc is None or self._proc.poll() is not None:
            return
        self.cancelled = True
        if sys.platform == "win32":
            subprocess.run(["taskkill", "/PID", str(self._proc.pid), "/T", "/F"],
                           check=False, capture_output=True, creationflags=NO_WINDOW)
        else:
            self._proc.kill()

    def _read_output(self) -> None:
        for line in self._proc.stdout:
            line = line.rstrip("\r\n")
            match = READY.search(line)
            if match and self.url is None:
                self.url = match.group(1)
                self.events.put(("ready", self.url))
            self.events.put(("out", line))
        returncode = self._proc.wait()
        elapsed = time.perf_counter() - self._started
        self.events.put(("done", (returncode, elapsed)))


def port_in_use(port: int = 8000) -> bool:
    """True when something is already listening on this port on this computer."""
    with socket.socket() as probe:
        probe.settimeout(0.5)
        return probe.connect_ex(("127.0.0.1", port)) == 0


def port_owner_pids(port: int = 8000) -> set[int]:
    """The process IDs listening on this port, from netstat (Windows)."""
    result = subprocess.run(["netstat", "-ano", "-p", "TCP"], capture_output=True, text=True,
                            check=False, creationflags=NO_WINDOW)
    pids: set[int] = set()
    for line in result.stdout.splitlines():
        parts = line.split()
        if len(parts) >= 5 and parts[0] == "TCP" and parts[1].endswith(f":{port}") and parts[3] == "LISTENING":
            pids.add(int(parts[4]))
    return pids


def free_port(port: int = 8000) -> None:
    """Stop whatever is listening on this port, with the processes it started."""
    for pid in port_owner_pids(port):
        subprocess.run(["taskkill", "/PID", str(pid), "/T", "/F"], check=False,
                       capture_output=True, creationflags=NO_WINDOW)
