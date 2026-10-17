"""DataBank IMX - Python Training (Qt version).

Same features as the tkinter runner, with lessons shown in Qt WebEngine.

Run:  python app.py

The code is split into three packages, next to this file:
  config.py           paths, palettes, fonts, visualization table
  core/               logic with no window code: discovery, the step runner,
                      file tracking, and source helpers
  render/             lesson Markdown to HTML (MathJax and Prism; vendor/ holds
                      the JavaScript)
  ui/                 the window: layout, theme, navigation, source, output,
                      run and lesson views, plus widgets, icons, syntax, logo

app.py holds the main window class, which combines the ui mixins.
"""

#pylint: disable=line-too-long, wrong-import-position, unused-argument, attribute-defined-outside-init
#pylint: disable=too-many-public-methods, too-few-public-methods
#pylint: disable=too-many-instance-attributes, too-many-statements

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from config import DARK, UI_FAMILY  # noqa: E402  pylint: disable=wrong-import-position
from core import discovery  # noqa: E402  pylint: disable=wrong-import-position
from ui.icons import logo_pixmap  # noqa: E402  pylint: disable=wrong-import-position
from ui.lesson_view import LessonMixin  # noqa: E402  pylint: disable=wrong-import-position
from ui.navigation import NavigationMixin  # noqa: E402  pylint: disable=wrong-import-position
from ui.output_panel import OutputMixin  # noqa: E402  pylint: disable=wrong-import-position
from ui.run_control import RunMixin  # noqa: E402  pylint: disable=wrong-import-position
from ui.source_panel import SourcePanelMixin  # noqa: E402  pylint: disable=wrong-import-position
from ui.theming import ThemeMixin  # noqa: E402  pylint: disable=wrong-import-position
from ui.window_layout import LayoutMixin  # noqa: E402  pylint: disable=wrong-import-position

#pylint: disable=no-name-in-module
from PySide6.QtGui import QFont, QIcon
#pylint: disable=no-name-in-module
from PySide6.QtWidgets import QApplication, QMainWindow

WELCOME_LESSON = discovery.REPO_ROOT / "part-i-basics" / "00_what_is_python.md"


class MainWindow(LayoutMixin, ThemeMixin, NavigationMixin, SourcePanelMixin, OutputMixin,
                 RunMixin, LessonMixin, QMainWindow):
    """Chapters and steps on the left; title, output, source and lesson on the right.

    The behavior is split across the mixins above. This class holds the state they share.
    """

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("DataBank IMX - Python Training")
        self.setWindowIcon(QIcon(logo_pixmap(64, DARK["accent"])))
        self.resize(1280, 820)
        self.dark = True
        self.colors = DARK
        self.scopes = discovery.discover()
        self.chapter: discovery.Chapter | None = None
        self.step: discovery.Step | None = None
        self.original_source = ""
        self.lesson_markdown = WELCOME_LESSON.read_text(encoding="utf-8") if WELCOME_LESSON.exists() else ""
        self.lesson_base = WELCOME_LESSON.parent
        self.run = None
        self.popout = None
        self.output_log: list[tuple[str, str]] = []
        self.output_formats: dict = {}
        self.badge_items: list = []
        self.saved_files: list = []
        self.run_snapshot: dict = {}

        self.build_ui()
        self.populate_tree()
        self.bind_keys()
        self.apply_theme()
        self.tabs.setCurrentIndex(1)  # open on the Lesson tab, so the welcome lesson shows

    def closeEvent(self, event) -> None:  # pylint: disable=invalid-name
        """Closing the main window also closes a popped-out lesson."""
        popout = self.popout
        self.popout = None
        if popout is not None:
            popout.close()
        super().closeEvent(event)


def main() -> int:
    """Start the application."""
    app = QApplication(sys.argv)
    app.setFont(QFont(UI_FAMILY, 10))
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
