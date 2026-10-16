"""DataBank IMX - Python Training (Qt version).

Same features as the tkinter runner, with lessons shown in Qt WebEngine.

Run:  python app.py

Shared code, imported from the sibling folders for now:
  lesson-runner           discovery.py, runner.py, syntax.py, logo.py
  lesson-runner-qt-spike  render.py and vendor/ (MathJax and Prism)
"""

from __future__ import annotations

import queue
import shlex
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "lesson-runner"))
sys.path.insert(0, str(HERE.parent / "lesson-runner-qt-spike"))

import discovery  # noqa: E402  pylint: disable=wrong-import-position
import logo  # noqa: E402  pylint: disable=wrong-import-position
from render import render_lesson  # noqa: E402  pylint: disable=wrong-import-position
from runner import StepRun  # noqa: E402  pylint: disable=wrong-import-position
from syntax import SYNTAX_TAGS, python_spans  # noqa: E402  pylint: disable=wrong-import-position

#pylint: disable=no-name-in-module
from PySide6.QtCore import Qt, QPointF, QRect, QRectF, QSize, QTimer, QUrl
#pylint: disable=no-name-in-module
from PySide6.QtGui import (QColor, QFont, QFontDatabase, QIcon, QKeySequence, QPainter,
                           QPainterPath, QPen, QPixmap, QPolygonF, QShortcut,
                           QSyntaxHighlighter, QTextCharFormat, QTextCursor)
#pylint: disable=no-name-in-module
from PySide6.QtWidgets import (QAbstractButton, QApplication, QFrame, QHBoxLayout, QInputDialog,
                               QLabel, QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
                               QPlainTextEdit, QPushButton, QSplitter, QStackedWidget,
                               QTabWidget, QToolButton, QTreeWidget, QTreeWidgetItem,
                               QVBoxLayout, QWidget)
#pylint: disable=no-name-in-module
from PySide6.QtWebEngineCore import QWebEngineSettings
#pylint: disable=no-name-in-module
from PySide6.QtWebEngineWidgets import QWebEngineView

VENDOR = HERE.parent / "lesson-runner-qt-spike" / "vendor"

DARK = {
    "bg": "#1E1E1E", "panel": "#252526", "border": "#3F3F46", "fg": "#D4D4D4",
    "accent": "#007ACC", "accent_hover": "#1C97EA", "success": "#4EC9B0",
    "error": "#F44747", "muted": "#858585", "selection": "#264F78",
    "kw": "#569CD6", "ctl": "#C586C0", "str": "#CE9178", "com": "#6A9955", "num": "#B5CEA8",
    "typ": "#4EC9B0", "fn": "#DCDCAA", "var": "#9CDCFE",
}
LIGHT = {
    "bg": "#FFFFFF", "panel": "#F3F3F3", "border": "#CCCEDB", "fg": "#1E1E1E",
    "accent": "#007ACC", "accent_hover": "#1C97EA", "success": "#007F5F",
    "error": "#CC0000", "muted": "#717171", "selection": "#ADD6FF",
    "kw": "#0000FF", "ctl": "#AF00DB", "str": "#A31515", "com": "#008000", "num": "#098658",
    "typ": "#267F99", "fn": "#795E26", "var": "#001080",
}

CODE_FAMILIES = ["Cascadia Mono", "Cascadia Code", "JetBrains Mono", "Consolas"]
UI_FAMILY = "Segoe UI"


def code_font(size: int) -> QFont:
    """The first installed monospace font from CODE_FAMILIES, with a fixed-pitch fallback."""
    installed = set(QFontDatabase.families())
    family = next((name for name in CODE_FAMILIES if name in installed), "Consolas")
    font = QFont(family, size)
    font.setStyleHint(QFont.StyleHint.Monospace)
    font.setFixedPitch(True)
    return font


def draw_icon(kind: str, colour: str, size: int = 18) -> QIcon:
    """Vector icons, drawn in code so they don't depend on any font."""
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    pen = QPen(QColor(colour), 1.6)
    pen.setCapStyle(Qt.PenCapStyle.RoundCap)
    pen.setJoinStyle(Qt.PenJoinStyle.RoundJoin)
    painter.setPen(pen)
    painter.setBrush(Qt.BrushStyle.NoBrush)
    s = size / 18.0
    if kind == "copy":
        painter.drawRoundedRect(QRectF(3.5 * s, 5.5 * s, 9 * s, 9.5 * s), 2 * s, 2 * s)
        painter.drawRoundedRect(QRectF(6.5 * s, 2.5 * s, 9 * s, 9.5 * s), 2 * s, 2 * s)
    elif kind == "popout":
        painter.drawLine(QPointF(5 * s, 13 * s), QPointF(13 * s, 5 * s))
        painter.drawLine(QPointF(7 * s, 5 * s), QPointF(13 * s, 5 * s))
        painter.drawLine(QPointF(13 * s, 5 * s), QPointF(13 * s, 11 * s))
    elif kind == "dock":
        painter.drawLine(QPointF(13 * s, 5 * s), QPointF(5 * s, 13 * s))
        painter.drawLine(QPointF(5 * s, 7 * s), QPointF(5 * s, 13 * s))
        painter.drawLine(QPointF(5 * s, 13 * s), QPointF(11 * s, 13 * s))
    elif kind == "check":
        painter.drawPolyline(QPolygonF([QPointF(3.5 * s, 9.5 * s), QPointF(7.5 * s, 13.5 * s),
                                        QPointF(14.5 * s, 5.5 * s)]))
    elif kind == "sun":
        painter.drawEllipse(QPointF(9 * s, 9 * s), 3.5 * s, 3.5 * s)
        for angle in range(0, 360, 45):
            import math  # pylint: disable=import-outside-toplevel
            rad = math.radians(angle)
            inner = QPointF(9 * s + 6 * s * math.cos(rad), 9 * s + 6 * s * math.sin(rad))
            outer = QPointF(9 * s + 8 * s * math.cos(rad), 9 * s + 8 * s * math.sin(rad))
            painter.drawLine(inner, outer)
    elif kind == "moon":
        painter.setPen(Qt.PenStyle.NoPen)
        painter.setBrush(QColor(colour))
        outer = QPainterPath()
        outer.addEllipse(QPointF(9 * s, 9 * s), 6.5 * s, 6.5 * s)
        cut = QPainterPath()
        cut.addEllipse(QPointF(12.5 * s, 6.5 * s), 5.5 * s, 5.5 * s)
        painter.drawPath(outer.subtracted(cut))
    painter.end()
    return QIcon(pixmap)


def logo_pixmap(size: int, colour: str) -> QPixmap:
    """The DataBank logo as a transparent, antialiased pixmap."""
    pixmap = QPixmap(size, size)
    pixmap.fill(Qt.GlobalColor.transparent)
    painter = QPainter(pixmap)
    painter.setRenderHint(QPainter.RenderHint.Antialiasing)
    painter.setPen(Qt.PenStyle.NoPen)
    painter.setBrush(QColor(colour))
    scale = size / logo.SIZE
    for polygon in logo.shapes():
        painter.drawPolygon(QPolygonF([QPointF(x * scale, y * scale) for x, y in polygon]))
    painter.end()
    return pixmap


class ThemeSwitch(QAbstractButton):
    """Sliding dark/light switch. Checked means light."""

    def __init__(self) -> None:
        super().__init__()
        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedSize(44, 22)
        self.track_colour = QColor("#3F3F46")
        self.checked_colour = QColor("#007ACC")

    def set_colors(self, track: str, checked: str) -> None:
        """Colours for the unchecked and checked track."""
        self.track_colour = QColor(track)
        self.checked_colour = QColor(checked)
        self.update()

    def paintEvent(self, event) -> None:  # pylint: disable=invalid-name
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        width, height = self.width(), self.height()
        painter.setBrush(self.checked_colour if self.isChecked() else self.track_colour)
        painter.drawRoundedRect(0, 0, width, height, height / 2, height / 2)
        thumb_x = width - height + 2 if self.isChecked() else 2
        painter.setBrush(QColor("#FFFFFF"))
        painter.drawEllipse(thumb_x, 2, height - 4, height - 4)
        painter.end()


def stylesheet(c: dict) -> str:
    """Application stylesheet for one palette. Fonts are set in code, not here."""
    return f"""
    QMainWindow, QWidget#root {{ background: {c['bg']}; }}
    QWidget {{ color: {c['fg']}; }}
    QLabel#title {{ font-size: 14pt; font-weight: bold; }}
    QLabel#subtitle, QLabel#section {{ color: {c['muted']}; }}
    QLabel#section {{ font-size: 8pt; font-weight: bold; padding: 4px 10px; }}
    QFrame#header {{ background: {c['accent']}; }}
    QLabel#headerText {{ color: white; font-size: 13pt; font-weight: bold; }}
    QTreeWidget, QListWidget {{ background: {c['panel']}; border: none; outline: 0; }}
    QTreeWidget::item {{ padding: 0px 2px; }}
    QTreeWidget::item:selected, QListWidget::item:selected {{
        background: {c['accent']}; color: white; }}
    QListWidget::item {{ padding: 0px 10px; }}
    QPlainTextEdit {{ background: {c['bg']}; border: none; }}
    QLineEdit {{ background: {c['bg']}; border: 1px solid {c['border']}; padding: 3px 6px; }}
    QPushButton {{ background: transparent; border: none; color: {c['muted']}; padding: 4px 8px; }}
    QPushButton#run {{ background: {c['accent']}; color: white; font-weight: bold;
                       padding: 6px 16px; border-radius: 3px; }}
    QPushButton#run:disabled {{ background: {c['border']}; color: {c['fg']}; }}
    QPushButton#continue {{ background: {c['accent']}; color: white; font-weight: bold;
                            padding: 4px 12px; }}
    QToolButton {{ background: transparent; border: none; padding: 4px; border-radius: 3px; }}
    QToolButton:hover {{ background: {c['border']}; }}
    QTabWidget::pane {{ border: none; }}
    QTabBar::tab {{ background: {c['panel']}; color: {c['muted']}; padding: 6px 14px; }}
    QTabBar::tab:selected {{ background: {c['bg']}; color: {c['fg']}; font-weight: bold; }}
    QFrame#resetBar {{ background: {c['panel']}; }}
    QSplitter::handle {{ background: {c['border']}; }}
    """


class PythonHighlighter(QSyntaxHighlighter):
    """Colours the source editor using the shared Python token rules."""

    def __init__(self, document, colors: dict) -> None:
        super().__init__(document)
        self.formats: dict[str, QTextCharFormat] = {}
        self._text: str | None = None
        self._spans: list = []
        self.apply_palette(colors)

    def apply_palette(self, colors: dict) -> None:
        """Rebuild the text formats for a new theme."""
        self.formats = {}
        for tag in SYNTAX_TAGS:
            fmt = QTextCharFormat()
            fmt.setForeground(QColor(colors[tag]))
            self.formats[tag] = fmt
        self._text = None
        self.rehighlight()

    def highlightBlock(self, text: str) -> None:  # pylint: disable=invalid-name
        document_text = self.document().toPlainText()
        if document_text != self._text:
            self._text = document_text
            self._spans = python_spans(document_text)
        row = self.currentBlock().blockNumber() + 1
        for (start_row, start_col), (end_row, end_col), tag in self._spans:
            if not start_row <= row <= end_row:
                continue
            start = start_col if start_row == row else 0
            end = end_col if end_row == row else len(text)
            if end > start:
                self.setFormat(start, end - start, self.formats[tag])


class LineGutter(QWidget):
    """The line-number strip beside the source editor. The editor does the painting."""

    def __init__(self, editor) -> None:
        super().__init__(editor)
        self.editor = editor

    def paintEvent(self, event) -> None:  # pylint: disable=invalid-name
        self.editor.paint_gutter(event)


class SourceEditor(QPlainTextEdit):
    """Code editor with a line-number gutter."""

    def __init__(self, colors: dict) -> None:
        super().__init__()
        self.colors = colors
        self.setFont(code_font(11))
        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.gutter = LineGutter(self)
        self.blockCountChanged.connect(self.update_margin)
        self.updateRequest.connect(self.update_gutter)
        self.update_margin()

    def gutter_width(self) -> int:
        """Width of the line-number gutter, based on the number of lines."""
        digits = max(3, len(str(max(1, self.blockCount()))))
        return 12 + self.fontMetrics().horizontalAdvance("9") * digits

    def update_margin(self) -> None:
        """Reserve space for the gutter on the left of the text."""
        self.setViewportMargins(self.gutter_width(), 0, 0, 0)

    def update_gutter(self, rect, dy) -> None:
        """Scroll or repaint the gutter with the text."""
        if dy:
            self.gutter.scroll(0, dy)
        else:
            self.gutter.update(0, rect.y(), self.gutter.width(), rect.height())
        if rect.contains(self.viewport().rect()):
            self.update_margin()

    def resizeEvent(self, event) -> None:  # pylint: disable=invalid-name
        super().resizeEvent(event)
        contents = self.contentsRect()
        self.gutter.setGeometry(QRect(contents.left(), contents.top(),
                                      self.gutter_width(), contents.height()))

    def paint_gutter(self, event) -> None:
        """Draw the line numbers for the visible lines."""
        from PySide6.QtGui import QPainter as _Painter  # pylint: disable=import-outside-toplevel
        painter = _Painter(self.gutter)
        painter.fillRect(event.rect(), QColor(self.colors["bg"]))
        painter.setFont(self.font())
        painter.setPen(QColor(self.colors["muted"]))
        block = self.firstVisibleBlock()
        number = block.blockNumber()
        top = round(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + round(self.blockBoundingRect(block).height())
        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                painter.drawText(0, top, self.gutter.width() - 6, self.fontMetrics().height(),
                                 Qt.AlignmentFlag.AlignRight, str(number + 1))
            block = block.next()
            top = bottom
            bottom = top + round(self.blockBoundingRect(block).height())
            number += 1
        painter.end()


class PopoutWindow(QWidget):
    """The pop-out lesson window, with a dock control. Closing it also docks the lesson."""

    def __init__(self, on_dock) -> None:
        super().__init__()
        self.on_dock = on_dock
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        bar = QHBoxLayout()
        bar.setContentsMargins(8, 4, 8, 4)
        bar.addStretch(1)
        dock = QToolButton()
        dock.setIcon(draw_icon("dock", DARK["muted"]))
        dock.setToolTip("Dock lesson back into the main window")
        dock.clicked.connect(self.on_dock)
        bar.addWidget(dock)
        layout.addLayout(bar)
        self.view = QWebEngineView()
        self.view.settings().setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        layout.addWidget(self.view, 1)

    def closeEvent(self, event) -> None:  # pylint: disable=invalid-name
        self.on_dock()
        super().closeEvent(event)


class MainWindow(QMainWindow):
    """Chapters and steps on the left; title, output, source and lesson on the right."""

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
        self.lesson_markdown = ""
        self.run: StepRun | None = None
        self.popout: PopoutWindow | None = None
        self.output_log: list[tuple[str, str]] = []
        self.output_formats: dict[str, QTextCharFormat] = {}

        self.build_ui()
        self.populate_tree()
        self.bind_keys()
        self.apply_theme()

    # ------------------------------------------------------------------ layout

    def build_ui(self) -> None:
        """Create the widgets and lay them out."""
        root = QWidget()
        root.setObjectName("root")
        self.setCentralWidget(root)
        outer = QHBoxLayout(root)
        outer.setContentsMargins(0, 0, 0, 0)
        outer.setSpacing(0)

        left_panel = QWidget()
        left = QVBoxLayout(left_panel)
        left.setContentsMargins(0, 0, 0, 0)
        left.setSpacing(0)
        header = QFrame()
        header.setObjectName("header")
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(12, 10, 12, 10)
        self.header_logo = QLabel()
        self.header_logo.setPixmap(logo_pixmap(22, "#FFFFFF"))
        header_layout.addWidget(self.header_logo)
        header_text = QLabel("Python Training")
        header_text.setObjectName("headerText")
        header_layout.addWidget(header_text)
        header_layout.addStretch(1)
        left.addWidget(header)

        left_splitter = QSplitter(Qt.Orientation.Vertical)
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.setIndentation(16)
        self.tree.currentItemChanged.connect(self.on_tree_changed)
        left_splitter.addWidget(self.tree)

        steps_box = QWidget()
        steps_layout = QVBoxLayout(steps_box)
        steps_layout.setContentsMargins(0, 0, 0, 0)
        steps_layout.setSpacing(0)
        steps_label = QLabel("STEPS")
        steps_label.setObjectName("section")
        steps_layout.addWidget(steps_label)
        self.step_list = QListWidget()
        self.step_list.setSpacing(0)
        self.step_list.currentRowChanged.connect(self.on_step_changed)
        steps_layout.addWidget(self.step_list, 1)
        left_splitter.addWidget(steps_box)

        left_splitter.setStretchFactor(0, 6)   # chapters: 60%
        left_splitter.setStretchFactor(1, 4)   # steps: 40%
        left.addWidget(left_splitter, 1)
        left_panel.setMinimumWidth(220)
        left_panel.setMaximumWidth(340)
        outer.addWidget(left_panel)

        right = QWidget()
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        right_layout.addWidget(self.build_title_bar())
        right_layout.addWidget(self.build_args_bar())

        body = QSplitter(Qt.Orientation.Vertical)
        body.addWidget(self.build_output())
        body.addWidget(self.build_tabs())
        body.setSizes([220, 520])
        right_layout.addWidget(body, 1)
        outer.addWidget(right, 1)

        self.timer = QTimer(self)
        self.timer.setInterval(30)
        self.timer.timeout.connect(self.poll_run)

    def build_title_bar(self) -> QWidget:
        """Step title on the left; sun, switch, moon and Run on the right."""
        bar = QFrame()
        layout = QHBoxLayout(bar)
        layout.setContentsMargins(12, 8, 12, 8)
        titles = QVBoxLayout()
        self.title_label = QLabel("Select a step from the left panel")
        self.title_label.setObjectName("title")
        self.subtitle_label = QLabel("")
        self.subtitle_label.setObjectName("subtitle")
        titles.addWidget(self.title_label)
        titles.addWidget(self.subtitle_label)
        layout.addLayout(titles, 1)

        self.sun_label = QLabel()
        layout.addWidget(self.sun_label)
        self.theme_switch = ThemeSwitch()
        self.theme_switch.toggled.connect(self.on_theme_switch)
        layout.addWidget(self.theme_switch)
        self.moon_label = QLabel()
        layout.addWidget(self.moon_label)
        layout.addSpacing(12)

        self.run_button = QPushButton("\u25B6  Run")
        self.run_button.setObjectName("run")
        self.run_button.setEnabled(False)
        self.run_button.clicked.connect(self.start_run)
        layout.addWidget(self.run_button)
        return bar

    def build_args_bar(self) -> QWidget:
        """Command-line arguments passed to the step."""
        bar = QFrame()
        layout = QHBoxLayout(bar)
        layout.setContentsMargins(12, 4, 12, 6)
        label = QLabel("args:")
        label.setFont(code_font(10))
        layout.addWidget(label)
        self.args_edit = QLineEdit()
        self.args_edit.setFont(code_font(10))
        layout.addWidget(self.args_edit, 1)
        return bar

    def build_output(self) -> QWidget:
        """Output pane with Continue, Copy and Clear."""
        box = QWidget()
        layout = QVBoxLayout(box)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        header = QFrame()
        header_layout = QHBoxLayout(header)
        header_layout.setContentsMargins(12, 2, 12, 2)
        section = QLabel("OUTPUT")
        section.setObjectName("section")
        header_layout.addWidget(section)
        header_layout.addStretch(1)
        self.continue_button = QPushButton("\u25B6  Continue")
        self.continue_button.setObjectName("continue")
        self.continue_button.clicked.connect(self.continue_run)
        self.continue_button.hide()
        header_layout.addWidget(self.continue_button)
        self.output_copy = QToolButton()
        self.output_copy.setToolTip("Copy output")
        self.output_copy.clicked.connect(lambda: self.copy_text(self.output.toPlainText(), self.output_copy))
        header_layout.addWidget(self.output_copy)
        clear = QPushButton("Clear")
        clear.clicked.connect(self.clear_output)
        header_layout.addWidget(clear)
        layout.addWidget(header)
        self.output = QPlainTextEdit()
        self.output.setReadOnly(True)
        self.output.setFont(code_font(10))
        layout.addWidget(self.output, 1)
        return box

    def build_tabs(self) -> QWidget:
        """Source and Lesson tabs. Pop out and Copy sit together in the top-right corner."""
        self.tabs = QTabWidget()
        self.tabs.addTab(self.build_source_tab(), "Source")
        self.tabs.addTab(self.build_lesson_tab(), "Lesson")

        corner = QWidget()
        corner_layout = QHBoxLayout(corner)
        corner_layout.setContentsMargins(0, 2, 8, 0)
        corner_layout.setSpacing(2)
        self.popout_button = QToolButton()
        self.popout_button.setToolTip("Pop out lesson")
        self.popout_button.clicked.connect(self.toggle_popout)
        corner_layout.addWidget(self.popout_button)
        self.copy_button = QToolButton()
        self.copy_button.setToolTip("Copy source or lesson, whichever tab is open")
        self.copy_button.clicked.connect(self.copy_current_tab)
        corner_layout.addWidget(self.copy_button)
        self.tabs.setCornerWidget(corner, Qt.Corner.TopRightCorner)
        return self.tabs

    def build_source_tab(self) -> QWidget:
        """Editable source with line numbers, highlighting and a reset bar."""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.reset_bar = QFrame()
        self.reset_bar.setObjectName("resetBar")
        reset_layout = QHBoxLayout(self.reset_bar)
        reset_layout.setContentsMargins(8, 3, 8, 3)
        self.edited_label = QLabel("\u25CF Code has been edited")
        reset_layout.addWidget(self.edited_label)
        reset_layout.addStretch(1)
        reset = QPushButton("Reset to original")
        reset.clicked.connect(self.reset_source)
        reset_layout.addWidget(reset)
        self.reset_bar.hide()
        layout.addWidget(self.reset_bar)

        self.editor = SourceEditor(DARK)
        self.editor.textChanged.connect(self.on_source_changed)
        self.highlighter = PythonHighlighter(self.editor.document(), DARK)
        layout.addWidget(self.editor, 1)
        return tab

    def build_lesson_tab(self) -> QWidget:
        """Rendered lesson. Shows a placeholder while the lesson is popped out."""
        tab = QWidget()
        layout = QVBoxLayout(tab)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.lesson_stack = QStackedWidget()
        self.lesson_view = QWebEngineView()
        self.lesson_view.page().setBackgroundColor(QColor(DARK["bg"]))
        self.lesson_view.settings().setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        self.lesson_stack.addWidget(self.lesson_view)
        placeholder = QWidget()
        place_layout = QVBoxLayout(placeholder)
        place_layout.addStretch(1)
        note = QLabel("The lesson is open in a separate window.")
        note.setAlignment(Qt.AlignmentFlag.AlignCenter)
        place_layout.addWidget(note)
        dock = QPushButton("Dock lesson back here")
        dock.setObjectName("continue")
        dock.clicked.connect(self.dock_lesson)
        place_layout.addWidget(dock, 0, Qt.AlignmentFlag.AlignCenter)
        place_layout.addStretch(1)
        self.lesson_stack.addWidget(placeholder)
        layout.addWidget(self.lesson_stack, 1)
        return tab

    def bind_keys(self) -> None:
        """Keyboard shortcuts, matching the tkinter runner."""
        QShortcut(QKeySequence("F5"), self, activated=self.start_run)
        QShortcut(QKeySequence("Escape"), self, activated=self.on_escape)
        QShortcut(QKeySequence("Ctrl+Shift+Return"), self, activated=self.continue_run)

    # ----------------------------------------------------------------- theme

    def apply_theme(self) -> None:
        """Apply the current palette everywhere, including the output log and lesson page."""
        c = self.colors
        self.setStyleSheet(stylesheet(c))
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
        for name, colour in (("text", c["fg"]), ("err", c["error"]), ("muted", c["muted"]),
                             ("echo", c["success"]), ("heading", c["accent"])):
            fmt = QTextCharFormat()
            fmt.setForeground(QColor(colour))
            self.output_formats[name] = fmt
        self.redraw_output()
        self.lesson_view.page().setBackgroundColor(QColor(c["bg"]))
        self.render_lesson_page()

    def on_theme_switch(self, checked: bool) -> None:
        """The switch was moved: checked means light."""
        self.dark = not checked
        self.colors = DARK if self.dark else LIGHT
        self.apply_theme()

    # ------------------------------------------------------------ navigation

    def populate_tree(self) -> None:
        """Fill the chapter tree. Each chapter stores its Chapter object in the item."""
        for scope in self.scopes:
            scope_item = QTreeWidgetItem([scope.name])
            scope_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
            scope_item.setSizeHint(0, QSize(0, 26))
            self.tree.addTopLevelItem(scope_item)
            for chapter in scope.chapters:
                item = QTreeWidgetItem([chapter.name])
                item.setData(0, Qt.ItemDataRole.UserRole, chapter)
                item.setSizeHint(0, QSize(0, 24))
                scope_item.addChild(item)
            scope_item.setExpanded(True)

    def on_tree_changed(self, current, _previous) -> None:
        """Load the chapter's steps when a chapter is selected."""
        if current is None:
            return
        chapter = current.data(0, Qt.ItemDataRole.UserRole)
        if chapter is None:
            return
        self.chapter = chapter
        self.step_list.blockSignals(True)
        self.step_list.clear()
        for step in chapter.steps:
            item = QListWidgetItem(step.title)
            item.setSizeHint(QSize(0, 26))
            self.step_list.addItem(item)
        self.step_list.blockSignals(False)
        if chapter.steps:
            self.step_list.setCurrentRow(0)
            self.on_step_changed(0)

    def on_step_changed(self, row: int) -> None:
        """Show the chosen step."""
        if self.chapter is None or row < 0 or row >= len(self.chapter.steps):
            return
        self.show_step(self.chapter.steps[row])

    def show_step(self, step: discovery.Step) -> None:
        """Load a step's source, lesson and title into the window."""
        self.step = step
        self.title_label.setText(step.title)
        name = (step.code_path or step.lesson_md).name
        self.subtitle_label.setText(f"{self.chapter.name}  \u00b7  {name}")
        self.args_edit.clear()
        if step.code_path is None:
            source = discovery.NO_SOURCE_TEXT
        else:
            source = step.code_path.read_text(encoding="utf-8")
        self.editor.blockSignals(True)
        self.editor.setPlainText(source)
        self.editor.blockSignals(False)
        self.original_source = source
        self.set_dirty(False)
        lesson_path = step.lesson_md or (self.chapter.intro_md if self.chapter else None)
        self.lesson_markdown = (lesson_path.read_text(encoding="utf-8") if lesson_path
                                else "No lesson text for this step.")
        self.render_lesson_page()
        self.clear_output()
        self.run_button.setEnabled(step.runnable)

    def render_lesson_page(self) -> None:
        """Render the current lesson in the current theme, into the main view and any pop-out.

        With no lesson selected, a blank page in the theme colour is loaded. This starts the
        web engine at launch, so the first real lesson doesn't flash white while it starts.
        """
        if not self.lesson_markdown:
            blank = f"<!doctype html><html><body style='background:{self.colors['bg']}'></body></html>"
            self.lesson_view.setHtml(blank)
            return
        html = render_lesson(self.lesson_markdown, VENDOR, dark=self.dark)
        base_folder = self.step.lesson_md.parent if self.step and self.step.lesson_md else HERE
        base = QUrl.fromLocalFile(str(base_folder) + "/")
        self.lesson_view.setHtml(html, base)
        if self.popout is not None:
            self.popout.view.setHtml(html, base)

    # ---------------------------------------------------------------- source

    def on_source_changed(self) -> None:
        """Show the edited marker when the code differs from the original."""
        self.set_dirty(self.editor.toPlainText() != self.original_source)

    def set_dirty(self, dirty: bool) -> None:
        """Show or hide the reset bar."""
        self.reset_bar.setVisible(dirty)

    def reset_source(self) -> None:
        """Restore the original code."""
        self.editor.setPlainText(self.original_source)
        self.set_dirty(False)

    def copy_current_tab(self) -> None:
        """Copy the source or the lesson, whichever tab is open."""
        if self.tabs.currentIndex() == 0:
            self.copy_text(self.editor.toPlainText(), self.copy_button)
        else:
            self.copy_text(self.lesson_markdown, self.copy_button)

    # ---------------------------------------------------------------- output

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

    # ----------------------------------------------------------------- running

    def start_run(self) -> None:
        """Run the current step with the editor's code and the args."""
        if self.step is None or not self.step.runnable or self.run is not None:
            return
        self.clear_output()
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
        self.run_button.setText("\u25B6  Run")
        self.run_button.setEnabled(bool(self.step and self.step.runnable))
        if cancelled:
            self.append("[Run cancelled]", "err")
        elif returncode != 0:
            self.append("")
            self.append("\u2500\u2500 Errors " + "\u2500" * 40, "err")
        self.append("")
        self.append(f"\u2500\u2500 Finished in {seconds * 1000:.0f} ms \u2500\u2500", "muted")

    # ----------------------------------------------------------------- pop-out

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


def main() -> int:
    """Start the application."""
    app = QApplication(sys.argv)
    app.setFont(QFont(UI_FAMILY, 10))
    window = MainWindow()
    window.show()
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
