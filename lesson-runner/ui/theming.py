"""Theme handling: applies the dark or light palette everywhere. Used as a mixin by MainWindow."""

from __future__ import annotations

from PySide6.QtGui import QColor, QTextCharFormat #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWidgets import QApplication #pylint: disable=no-name-in-module #NOSONAR

from config import DARK, LIGHT
from ui.icons import draw_icon, logo_pixmap
from ui.theme import stylesheet, tooltip_style


class ThemeMixin:
    """Applies and switches the color palette."""

    def apply_theme(self) -> None:
        """Apply the current palette everywhere, including the output log and lesson page."""
        c = self.colors
        self.setStyleSheet(stylesheet(c))
        QApplication.instance().setStyleSheet(tooltip_style(c))
        self.theme_switch.blockSignals(True)
        self.theme_switch.setChecked(not self.dark)
        self.theme_switch.blockSignals(False)
        self.theme_switch.set_colors(DARK["border"], DARK["accent"])
        self.sun_label.setPixmap(draw_icon("sun", c["muted"], 18).pixmap(18, 18))
        self.moon_label.setPixmap(draw_icon("moon", c["muted"], 18).pixmap(18, 18))
        self.header_logo.setPixmap(logo_pixmap(22, "#FFFFFF"))
        self.popout_button.setIcon(draw_icon("popout", c["muted"]))
        self.copy_button.setIcon(draw_icon("copy", c["muted"]))
        self.output_copy.setIcon(draw_icon("copy", c["muted"]))
        self.editor.colors = c
        self.editor.setStyleSheet(f"background: {c['bg']}; color: {c['fg']}; border: none;")
        self.highlighter.apply_palette(c)
        self.output.setStyleSheet(f"background: {c['bg']}; color: {c['fg']}; border: none;")
        self.output_formats = {}
        for name, color in (("text", c["fg"]), ("err", c["error"]), ("muted", c["muted"]),
                            ("echo", c["success"]), ("heading", c["accent"]), ("warn", c["warn"])):
            fmt = QTextCharFormat()
            fmt.setForeground(QColor(color))
            self.output_formats[name] = fmt
        self.redraw_output()
        self.lesson_view.page().setBackgroundColor(QColor(c["bg"]))
        self.rebuild_badges()
        self.render_lesson_page()

    def on_theme_switch(self, checked: bool) -> None:
        """The switch was moved: checked means light."""
        self.dark = not checked
        self.colors = DARK if self.dark else LIGHT
        self.apply_theme()
