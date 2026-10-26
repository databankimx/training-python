"""Running a step: starts it, reads its events, answers input, and reports the result.
Used as a mixin by MainWindow."""

from __future__ import annotations

import queue
import shlex
import shutil
import sys
import tempfile
import traceback
from pathlib import Path

from PySide6.QtCore import QUrl #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtGui import QDesktopServices #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWidgets import QDialog, QInputDialog, QMessageBox #pylint: disable=no-name-in-module #NOSONAR

from core.files_watch import TEXT_SUFFIXES, open_in_text_editor, snapshot, written_since
from core.runner import StepRun
from core.stages import build_with_script
from core.web_run import WebRun, free_port, port_in_use, requirements_for, web_environment_message, web_environment_problem, web_python
from ui.web_login import AdminLoginDialog

#pylint: disable=line-too-long

class RunMixin:
    """Runs the current step in a child process and shows what it does."""

    def start_run(self) -> None:
        """Run the current step with the editor's code and the args."""
        if self.step is None or not self.step.runnable:
            return
        if self.run is not None:
            self.append("[The step is still running. Close its window first.]", "muted")
            return
        if self.step.kind == "web":
            self.start_web_run()
            return
        self.clear_output()
        self.view_file_button.hide()
        self.saved_files = []
        self.run_snapshot = snapshot(self.step.code_path.parent)
        try:
            args = shlex.split(self.args_edit.text())
        except ValueError as error:
            self.append(f"[Bad arguments] {error}", "err")
            return
        if self.stage is not None:
            try:
                main_path, source = self.build_stage_for_run()
            except Exception:  # pylint: disable=broad-exception-caught
                self.append("[Could not build this step]", "err")
                self.append(traceback.format_exc(), "err")
                return
        elif self.multi_file:
            try:
                main_path, source = self.build_exercise_for_run()
            except Exception:  # pylint: disable=broad-exception-caught
                self.append("[Could not prepare this exercise]", "err")
                self.append(traceback.format_exc(), "err")
                return
        else:
            main_path, source = self.step.code_path, self.editor.toPlainText()
        if self.stage is not None:
            self.append(f"Running alien_invasion.py from {self.stage.folder.name}", "muted")
            if self.stage_texts:
                self.append("Using your edits to: " + ", ".join(sorted(self.stage_texts)), "muted")
            self.append(f"Python: {sys.executable}", "muted")
            self.append(f"Folder: {main_path.parent}", "muted")
            self.append(
                f"Built file has: bg_color={'bg_color' in source}, "
                f"settings={'Settings()' in source}, ship={'Ship(self)' in source}",
                "muted")
        self.run = StepRun(main_path, source, args)
        self.run.start()
        self.run_button.setText("Running\u2026")
        self.run_button.setEnabled(False)
        self.timer.start()

    def poll_run(self) -> None:
        """Move events from the runner thread into the window."""
        run = self.run
        if run is None:
            self.timer.stop()
            return
        while True:
            try:
                kind, value = run.events.get_nowait()
            except queue.Empty:
                break
            if kind == "out":
                self.append(value)
            elif kind == "err":
                self.append(value, "err")
            elif kind == "warn":
                self.append(value, "warn")
            elif kind == "clear":
                self.clear_output()
            elif kind == "pause":
                self.append("\u2015\u2015 Click Continue to proceed \u2015\u2015", "muted")
                self.continue_button.show()
            elif kind == "input":
                self.answer_input(str(value))
            elif kind == "ready":
                self.show_open_browser(str(value))
            elif kind == "done":
                self.finish_run(*value)
                return

    def answer_input(self, prompt: str) -> None:
        """Ask for a line of text and send it to the step."""
        if self.run is None:
            return
        if not prompt.strip():
            prompt = self.last_output_line()
        answer, ok = QInputDialog.getText(self, "Console input", prompt or "Input:")
        if not ok:
            answer = ""
        self.append(answer, "echo")
        self.run.send(answer)

    def rate_limit_hint(self) -> None:
        """After a run that GitHub refused for rate limits, point to the token setup guide."""
        text = " ".join(line.lower() for line, _kind in self.output_log)
        if "status code: 403" in text or "rate limit" in text:
            self.append("")
            self.append("GitHub's rate limit has been reached. To avoid waiting, set up a token.", "muted")
            self.append("Open Data Visualization, then Setup, in the menu.", "muted")
            self.append("It uses the GITHUB_TRAINING_TOKEN variable. Restart the runner after you set it.", "muted")

    def build_stage_for_run(self) -> tuple[Path, str]:
        """Build the stage into a temporary folder, with any edited full files applied.

        Snipped files always run from the full file on disk. Returns the main file's path and text.
        """
        target = Path(tempfile.mkdtemp(prefix="alien_stage_"))
        build_with_script(self.stage, target)
        for name, text in self.stage_texts.items():
            (target / name).write_text(text, encoding="utf-8")
        main = target / "alien_invasion.py"
        return main, main.read_text(encoding="utf-8")

    def build_exercise_for_run(self) -> tuple[Path, str]:
        """Copy the exercise folder to a temporary place, with any edited modules applied.

        The copy keeps the exercise's images, so the program finds them as it does in the folder.
        Returns the main script's path and text.
        """
        source_dir = self.step.code_path.parent
        target = Path(tempfile.mkdtemp(prefix="exercise_")) / source_dir.name
        shutil.copytree(source_dir, target, ignore=shutil.ignore_patterns("__pycache__"))
        for name, text in self.stage_texts.items():
            (target / name).write_text(text, encoding="utf-8")
        main = target / self.step.code_path.name
        return main, main.read_text(encoding="utf-8")

    def start_web_run(self) -> None:
        """Build the web step and start its server. The server runs until Escape stops it."""
        chapter, number = self.step.web_build
        modules, requirements = requirements_for(chapter)
        problem = web_environment_problem(modules)
        if problem is not None:
            self.clear_output()
            self.append("[The web applications environment isn't ready.]", "err")
            for line in web_environment_message(problem, requirements).splitlines():
                self.append(line)
            return
        credentials = self.web_credentials()
        if credentials is None:
            return
        username, password = credentials
        if port_in_use(8000):
            answer = QMessageBox.question(
                self, "Port 8000 is in use",
                "Something is already listening on port 8000, probably from an earlier run.\n\n"
                "Stop it and continue?")
            if answer != QMessageBox.StandardButton.Yes:
                return
            free_port(8000)
        self.clear_output()
        self.open_browser_button.hide()
        self.web_url = None
        self.run = WebRun([web_python(), "build_stage.py", chapter, str(number), "--run"],
                          {"STUDENT_ADMIN_USERNAME": username, "STUDENT_ADMIN_PASSWORD": password})
        self.append(f"Building {chapter} step {number}, then starting the server.", "muted")
        self.append("Press Escape to stop the server.", "muted")
        self.run.start()
        self.run_button.setText("Running\u2026")
        self.run_button.setEnabled(False)
        self.timer.start()

    def web_credentials(self) -> tuple[str, str] | None:
        """The admin account details for this session. The dialog runs once, and the answers stay in memory."""
        existing = getattr(self, "web_admin", None)
        if existing is None:
            dialog = AdminLoginDialog(self)
            if dialog.exec() != QDialog.DialogCode.Accepted:
                return None
            existing = dialog.credentials()
            self.web_admin = existing
        return existing

    def show_open_browser(self, url: str) -> None:
        """Show the Open in browser button, open the step's first page, and say where the site is running."""
        self.web_url = url
        self.open_browser_button.show()
        self.append(f"The site is running at {url}", "muted")
        QDesktopServices.openUrl(QUrl(url.rstrip("/") + self.start_path()))

    def start_path(self) -> str:
        """The page the step opens first, from its start.txt file. The home page when there's no start.txt."""
        if self.step is None or self.step.lesson_md is None:
            return "/"
        start = self.step.lesson_md.parent / "start.txt"
        if not start.is_file():
            return "/"
        path = start.read_text(encoding="utf-8").strip()
        return path if path.startswith("/") else "/" + path

    def stop_run_on_leaving(self, *_args) -> None:
        """Leaving a step stops its run, as though Escape had been pressed.

        The window is reset at once, rather than waiting for the process to report that it has stopped.
        """
        if self.run is None:
            return
        self.run.cancel()
        self.run = None
        self.timer.stop()
        self.continue_button.hide()
        self.open_browser_button.hide()
        self.saved_files = []
        self.run_button.setText("\u25B6  Run")
        self.run_button.setEnabled(bool(self.step and self.step.runnable))

    def open_running_site(self) -> None:
        """Open the running site in the default browser."""
        url = getattr(self, "web_url", None)
        if url:
            QDesktopServices.openUrl(QUrl(url))

    def update_view_file(self) -> None:
        """Offer to open the file this step saved, when its badges say it saves one and it did."""
        saves = any(label == "Saves file" for label, _tip in self.badge_items)
        self.view_file_button.setVisible(bool(saves and self.saved_files))

    def view_saved_file(self) -> None:
        """Open the newest file the step saved, in its default application."""
        if self.saved_files:
            path = self.saved_files[0]
            if path.suffix.lower() in TEXT_SUFFIXES:
                open_in_text_editor(path)
            else:
                QDesktopServices.openUrl(QUrl.fromLocalFile(str(path)))

    def last_output_line(self) -> str:
        """The last non-blank line of output, used as an input prompt."""
        for text, _kind in reversed(self.output_log):
            if text.strip():
                return text.strip()
        return ""

    def continue_run(self) -> None:
        """Resume a step waiting at a pause."""
        if self.run is not None and self.continue_button.isVisible():
            self.continue_button.hide()
            self.run.send("")

    def on_escape(self) -> None:
        """Cancel a run, or reset the editor when it has edits."""
        if self.run is not None:
            self.run.cancel()
        elif self.reset_bar.isVisible():
            self.reset_source()

    def finish_run(self, returncode: int, seconds: float) -> None:
        """Report the result and restore the Run button."""
        cancelled = self.run is not None and self.run.cancelled
        self.run = None
        self.timer.stop()
        self.continue_button.hide()
        self.saved_files = (written_since(self.step.code_path.parent, self.run_snapshot)
                            if self.step and self.step.kind != "web" else [])
        self.open_browser_button.hide()
        self.update_view_file()
        self.rate_limit_hint()
        self.run_button.setText("\u25B6  Run")
        self.run_button.setEnabled(bool(self.step and self.step.runnable))
        if cancelled:
            self.append("[Run cancelled]", "err")
        elif returncode != 0:
            self.append("")
            self.append("\u2500\u2500 Errors " + "\u2500" * 40, "err")
        self.append("")
        self.append(f"\u2500\u2500 Finished in {seconds * 1000:.0f} ms \u2500\u2500", "muted")
