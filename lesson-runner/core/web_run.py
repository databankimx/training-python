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
DJANGO_MODULES = ("django", "django_bootstrap5")
DJANGO_REQUIREMENTS = "ch20-styling-and-deploying\\lessons\\01-bootstrap-setup\\requirements.txt"
FLASK_MODULES = ("flask", "sqlalchemy")
FLASK_REQUIREMENTS = "..\\..\\part-iii-beyond-the-book\\s25-flask-learning-log\\01-flask-setup\\requirements.txt"

READY = re.compile(r"Starting development server at (http://\S+)")


def web_python() -> str:
    """The Python that runs the build: the web applications virtual environment.

    The runner checks the environment with web_environment_problem before it calls this, so the path is known to exist.
    """
    return str(WEB_ROOT / ".venv" / "Scripts" / "python.exe")


def requirements_for(chapter: str) -> tuple[tuple[str, ...], str]:
    """The packages a chapter needs to be checked for, and the requirements file that installs them. The Flask chapter is s25."""
    if chapter == "s25":
        return FLASK_MODULES, FLASK_REQUIREMENTS
    return DJANGO_MODULES, DJANGO_REQUIREMENTS


def web_environment_problem(modules: tuple[str, ...] = DJANGO_MODULES) -> str | None:
    """Check the web applications environment before a build. Returns None when it's ready, or a short reason.

    The reasons are "missing" (no .venv folder), "broken" (the folder can't start Python, usually because it was moved or
    renamed), and "packages" (Python starts, but Django or django-bootstrap5 isn't installed). Activating the environment is
    not needed: the runner calls its Python directly.
    """
    venv_python = WEB_ROOT / ".venv" / "Scripts" / "python.exe"
    if not venv_python.exists():
        return "missing"
    try:
        result = subprocess.run([str(venv_python), "-c", "import " + ", ".join(modules)],
                                capture_output=True, text=True, check=False, creationflags=NO_WINDOW)
    except OSError:
        return "broken"
    if result.returncode != 0:
        return "packages"
    return None


RECOVERY_INSTALL = (
    "  .venv\\Scripts\\python.exe -m pip install -r ch20-styling-and-deploying\\lessons\\01-bootstrap-setup\\requirements.txt"
)


def web_environment_text(problem: str) -> str:
    """The message to show the user, with the commands that fix the problem. Each command is run in the web-applications folder."""
    footer = ("\n\nYou don't need to activate it. The runner uses the environment's Python directly.\n"
              "When it's done, click Run again.")
    if problem == "missing":
        return ("The web applications environment (.venv) doesn't exist yet.\n\n"
                "To create it, open PowerShell in the web-applications folder, and run:\n\n"
                "  python -m venv .venv\n" + RECOVERY_INSTALL + footer)
    if problem == "packages":
        return ("The web applications environment (.venv) is there, but Django or django-bootstrap5 isn't installed in it.\n\n"
                "To install them, open PowerShell in the web-applications folder, and run:\n\n" + RECOVERY_INSTALL + footer)
    return ("The web applications environment (.venv) is there, but it can't start. It may have been moved or renamed after it was created.\n\n"
            "To rebuild it, open PowerShell in the web-applications folder, and run:\n\n"
            "  Remove-Item -Recurse -Force .venv\n"
            "  python -m venv .venv\n" + RECOVERY_INSTALL + footer)


def web_environment_message(problem: str, requirements: str = DJANGO_REQUIREMENTS) -> str:
    """The message for a problem, with the install command for this chapter's requirements file."""
    return web_environment_text(problem).replace(DJANGO_REQUIREMENTS, requirements)


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
