"""Qt WebEngine spike: render a few lessons with MathJax, tables and the lesson's CSS.

Run from this folder, after installing requirements.txt:

    python spike.py
"""

from __future__ import annotations

import sys
from pathlib import Path

#pylint: disable=no-name-in-module
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QComboBox, QMainWindow, QVBoxLayout, QWidget
#pylint: disable=no-name-in-module
from PySide6.QtWebEngineCore import QWebEnginePage
#pylint: disable=no-name-in-module
from PySide6.QtWebEngineCore import QWebEngineSettings
#pylint: disable=no-name-in-module
from PySide6.QtWebEngineWidgets import QWebEngineView

from render import render_lesson

REPO = Path(__file__).resolve().parents[1]
VENDOR = Path(__file__).resolve().parent / "vendor"
BITWISE = REPO / "part-iii-beyond-the-book" / "s05-bitwise-operations"

LESSONS = [
    ("S05 - Base 10", BITWISE / "02_base_ten.md"),
    ("S05 - Binary addition", BITWISE / "06_binary_addition.md"),
    ("S05 - Intuitive but wrong", BITWISE / "07_intuitive_but_wrong.md"),
    ("S05 - Bitwise AND", BITWISE / "11_bitwise_and.md"),
]


class ConsolePage(QWebEnginePage):
    """Sends the page's JavaScript console messages to the terminal."""

    def javaScriptConsoleMessage(self, level, message, line, source):  # pylint: disable=invalid-name,too-many-arguments
        print(f"[page console] {message} ({source}:{line})")


class SpikeWindow(QMainWindow):
    """A dropdown of lessons above a web view that shows the selected one."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Lesson renderer spike (Qt WebEngine)")
        self.resize(1100, 820)

        self.picker = QComboBox()
        for name, _path in LESSONS:
            self.picker.addItem(name)
        self.picker.currentIndexChanged.connect(self.show_lesson)

        self.view = QWebEngineView()
        self.view.setPage(ConsolePage(self.view))
        # Let the lesson page load MathJax and Prism from the local vendor folder.
        self.view.settings().setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        self.view.loadFinished.connect(self.typeset)

        layout = QVBoxLayout()
        layout.addWidget(self.picker)
        layout.addWidget(self.view, 1)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.show_lesson(0)

    def typeset(self, ok: bool) -> None:
        """After a page loads, ask MathJax to typeset it, and report if MathJax is missing."""
        print(f"[spike] page loaded: {ok}")
        self.view.page().runJavaScript(
            "if (window.MathJax && MathJax.typesetPromise) {"
            "  MathJax.typesetPromise().then(() => console.log('MathJax typeset done'));"
            "} else { console.log('MathJax not loaded'); }"
        )

    def show_lesson(self, index: int) -> None:
        """Render the chosen lesson and load it into the view."""
        _name, path = LESSONS[index]
        markdown = path.read_text(encoding="utf-8")
        html = render_lesson(markdown, VENDOR)
        self.view.setHtml(html, QUrl.fromLocalFile(str(path.parent) + "/"))


def main() -> int:
    app = QApplication(sys.argv)
    window = SpikeWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
