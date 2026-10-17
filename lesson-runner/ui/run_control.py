"""Running a step: starts it, reads its events, answers input, and reports the result.
Used as a mixin by MainWindow."""

from __future__ import annotations

import queue
import shlex

from PySide6.QtCore import QUrl #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtGui import QDesktopServices #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWidgets import QInputDialog #pylint: disable=no-name-in-module #NOSONAR

from core.files_watch import TEXT_SUFFIXES, open_in_text_editor, snapshot, written_since
from core.runner import StepRun

#pylint: disable=line-too-long

class RunMixin:
    """Runs the current step in a child process and shows what it does."""

    def start_run(self) -> None:
        """Run the current step with the editor's code and the args."""
        if self.step is None or not self.step.runnable or self.run is not None:
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
        self.run = StepRun(self.step.code_path, self.editor.toPlainText(), args)
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
        self.saved_files = written_since(self.step.code_path.parent, self.run_snapshot) if self.step else []
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
