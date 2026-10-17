"""
Output pane: writes lines in their colours, clears them, and copies text.
Used as a mixin by MainWindow.
"""

from __future__ import annotations

from PySide6.QtCore import QTimer #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtGui import QTextCursor #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWidgets import QApplication, QToolButton #pylint: disable=no-name-in-module #NOSONAR

from icons import draw_icon


class OutputMixin:
    """Keeps the output log and the output pane in step."""

    def append(self, text: str, kind: str = "text") -> None:
        """Add one line to the output log and the output pane."""
        self.output_log.append((text, kind))
        self.write_output_line(text, kind)

    def write_output_line(self, text: str, kind: str) -> None:
        """Write one line in the colour for its kind."""
        cursor = self.output.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        cursor.insertText(text + "\n", self.output_formats.get(kind, self.output_formats["text"]))
        self.output.setTextCursor(cursor)
        self.output.ensureCursorVisible()

    def redraw_output(self) -> None:
        """Rewrite the whole output in the current theme's colours."""
        self.output.clear()
        for text, kind in self.output_log:
            self.write_output_line(text, kind)

    def clear_output(self) -> None:
        """Empty the output pane and its log."""
        self.output_log = []
        self.output.clear()

    def copy_text(self, text: str, button: QToolButton | None = None) -> None:
        """Copy text to the clipboard, and show a tick on the button that was pressed."""
        if not text.strip():
            return
        QApplication.clipboard().setText(text)
        if button is not None:
            button.setIcon(draw_icon("check", "#4EC9B0"))
            button.setToolTip("Copied")
            QTimer.singleShot(1500, lambda: self.reset_copy_icon(button))

    def reset_copy_icon(self, button: QToolButton) -> None:
        """Return a copy button to its normal icon."""
        button.setIcon(draw_icon("copy", self.colors["muted"]))
        button.setToolTip("Copy")
