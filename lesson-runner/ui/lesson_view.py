"""Lesson view: renders the lesson, scrolls to the step's heading, and handles the pop-out window.
Used as a mixin by MainWindow."""

from __future__ import annotations

import json
import traceback

from PySide6.QtGui import QColor, QIcon #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtCore import QUrl #pylint: disable=no-name-in-module #NOSONAR

from config import DARK, VENDOR
from render.render import render_lesson
from ui.icons import logo_pixmap
from ui.widgets import PopoutWindow

#pylint: disable=line-too-long

class LessonMixin:
    """Shows lessons in the window or in a separate pop-out window."""

    def render_lesson_page(self) -> None:
        """Render the current lesson in the current theme, into the main view and any pop-out.

        With no lesson selected, a blank page in the theme color is loaded. This starts the
        web engine at launch, so the first real lesson doesn't flash white while it starts.
        """
        if not self.lesson_markdown:
            blank = f"<!doctype html><html><body style='background:{self.colors['bg']}'></body></html>"
            self.lesson_view.setHtml(blank)
            return
        try:
            html = render_lesson(self.lesson_markdown, VENDOR, dark=self.dark)
            base = QUrl.fromLocalFile(str(self.lesson_base) + "/")
            self.lesson_view.setHtml(html, base)
            if self.popout is not None:
                self.popout.view.setHtml(html, base)
        except Exception:  # pylint: disable=broad-exception-caught
            # Qt swallows exceptions raised in slots, so report them here.
            self.append("[Lesson could not be rendered]", "err")
            self.append(traceback.format_exc(), "err")

    def on_lesson_loaded(self, _ok: bool) -> None:
        """After a lesson loads, scroll to the heading that matches the current step's title.

        Part I chapters share one lesson file, so the step's section is found by its heading.
        If no heading matches, the page stays where it is.
        """
        if self.step is None:
            return
        title = json.dumps(self.step.title)
        script = (
            "(function () {"
            f"  var target = {title}.trim().toLowerCase();"
            "  var heads = Array.from(document.querySelectorAll('h1,h2,h3,h4,h5,h6'));"
            "  var hit = heads.find(function (h) { return h.textContent.trim().toLowerCase() === target; });"
            "  if (hit) { hit.scrollIntoView({block: 'start'}); }"
            "})();"
        )
        self.lesson_view.page().runJavaScript(script)

    def toggle_popout(self) -> None:
        """Open the lesson in its own window, or dock it back."""
        if self.popout is None:
            self.pop_out_lesson()
        else:
            self.dock_lesson()

    def pop_out_lesson(self) -> None:
        """Show the lesson in a separate window beside the main one."""
        self.popout = PopoutWindow(self.dock_lesson)
        self.popout.view.page().setBackgroundColor(QColor(self.colors["bg"]))
        self.popout.setWindowTitle(f"Lesson - {self.chapter.name}" if self.chapter else "Lesson")
        self.popout.setWindowIcon(QIcon(logo_pixmap(64, DARK["accent"])))
        self.popout.resize(620, self.height())
        geometry = self.geometry()
        self.popout.move(geometry.right() + 8, geometry.top())
        self.render_lesson_page()
        self.popout.show()
        self.lesson_stack.setCurrentIndex(1)

    def dock_lesson(self) -> None:
        """Close the pop-out window and show the lesson in the main window again."""
        if self.popout is None:
            return
        popout = self.popout
        self.popout = None
        self.lesson_stack.setCurrentIndex(0)
        popout.close()
