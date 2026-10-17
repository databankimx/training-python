"""DataBank IMX - Python Training (Qt version).

Same features as the tkinter runner, with lessons shown in Qt WebEngine.

Run:  python app.py

The window is split across modules in this folder:
  config.py           paths, palettes, fonts, visualization table
  theme.py            fonts and the stylesheet
  icons.py            vector icons and the logo
  source_tools.py     lint-comment stripping and step badges
  widgets.py          theme switch, highlighter, source editor, pop-out window
  window_layout.py    builds the widgets (LayoutMixin)
  theming.py          applies dark or light (ThemeMixin)
  navigation.py       chapter tree and step list (NavigationMixin)
  source_panel.py     loads a step into the editor and lesson (SourcePanelMixin)
  output_panel.py     output pane and copy (OutputMixin)
  run_control.py      running a step (RunMixin)
  lesson_view.py      lesson rendering and pop-out (LessonMixin)

Shared code, imported from the sibling folders for now:
  lesson-runner           discovery.py, runner.py, syntax.py, logo.py
  lesson-runner-qt-spike  render.py and vendor/ (MathJax and Prism)
"""

#pylint: disable=line-too-long, wrong-import-position, unused-argument, attribute-defined-outside-init
#pylint: disable=too-many-public-methods, too-few-public-methods
#pylint: disable=too-many-instance-attributes, too-many-statements

from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import discovery  # noqa: E402  pylint: disable=wrong-import-position
from config import DARK, UI_FAMILY  # noqa: E402  pylint: disable=wrong-import-position
from icons import logo_pixmap  # noqa: E402  pylint: disable=wrong-import-position
from lesson_view import LessonMixin  # noqa: E402  pylint: disable=wrong-import-position
from navigation import NavigationMixin  # noqa: E402  pylint: disable=wrong-import-position
from output_panel import OutputMixin  # noqa: E402  pylint: disable=wrong-import-position
from run_control import RunMixin  # noqa: E402  pylint: disable=wrong-import-position
from source_panel import SourcePanelMixin  # noqa: E402  pylint: disable=wrong-import-position
from theming import ThemeMixin  # noqa: E402  pylint: disable=wrong-import-position
from window_layout import LayoutMixin  # noqa: E402  pylint: disable=wrong-import-position

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
