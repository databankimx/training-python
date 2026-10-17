"""
Custom widgets: theme switch, syntax highlighter, source editor, tree delegate
and pop-out window.
"""

#pylint: disable=line-too-long

from __future__ import annotations

from PySide6.QtCore import QRect, Qt #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtGui import QColor, QPainter, QSyntaxHighlighter, QTextCharFormat #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWebEngineCore import QWebEngineSettings #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWebEngineWidgets import QWebEngineView #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWidgets import (QAbstractButton, QHBoxLayout, QPlainTextEdit, QStyledItemDelegate, #pylint: disable=no-name-in-module #NOSONAR
                               QToolButton, QVBoxLayout, QWidget) #pylint: disable=no-name-in-module #NOSONAR

from config import DARK, FLUSH_ROLE
from ui.icons import draw_icon
from ui.syntax import SYNTAX_TAGS, c_spans, python_spans
from ui.theme import code_font


class ThemeSwitch(QAbstractButton):
    """Sliding dark/light switch. Checked means light."""

    def __init__(self) -> None:
        super().__init__()
        self.setCheckable(True)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setFixedSize(44, 22)
        self.track_color = QColor("#3F3F46")
        self.checked_color = QColor("#007ACC")

    def set_colors(self, track: str, checked: str) -> None:
        """Colors for the unchecked and checked track."""
        self.track_color = QColor(track)
        self.checked_color = QColor(checked)
        self.update()

    def paintEvent(self, event) -> None:  # pylint: disable=invalid-name, unused-argument
        """Paint the theme switch."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setPen(Qt.PenStyle.NoPen)
        width, height = self.width(), self.height()
        painter.setBrush(self.checked_color if self.isChecked() else self.track_color)
        painter.drawRoundedRect(0, 0, width, height, height / 2, height / 2)
        thumb_x = width - height + 2 if self.isChecked() else 2
        painter.setBrush(QColor("#FFFFFF"))
        painter.drawEllipse(thumb_x, 2, height - 4, height - 4)
        painter.end()


class PythonHighlighter(QSyntaxHighlighter):
    """Colours the source editor using the shared Python token rules."""

    def __init__(self, document, colors: dict) -> None:
        super().__init__(document)
        self.formats: dict[str, QTextCharFormat] = {}
        self._text: str | None = None
        self._spans: list = []
        self.language = "python"
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

    def set_language(self, language: str) -> None:
        """Highlight the source as Python or C."""
        self.language = language
        self._text = None
        self.rehighlight()

    def highlightBlock(self, text: str) -> None:  # pylint: disable=invalid-name
        """Apply syntax highlighting to the current block of text."""
        document_text = self.document().toPlainText()
        if document_text != self._text:
            self._text = document_text
            self._spans = (c_spans if self.language == "c" else python_spans)(document_text)
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
        """Paint the line-number gutter."""
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
        """Handle the resize event to adjust the gutter geometry."""
        super().resizeEvent(event)
        contents = self.contentsRect()
        self.gutter.setGeometry(QRect(contents.left(), contents.top(),
                                      self.gutter_width(), contents.height()))

    def paint_gutter(self, event) -> None:
        """Draw the line numbers for the visible lines."""
        painter = QPainter(self.gutter)
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


class TreeDelegate(QStyledItemDelegate):
    """Moves flagged items one indent step left, so their names line up with the nesting arrows."""

    def __init__(self, tree) -> None:
        super().__init__(tree)
        self.tree = tree

    def initStyleOption(self, option, index) -> None:  # pylint: disable=invalid-name
        """Adjust the style option for items that should be flushed with the nesting arrows."""
        super().initStyleOption(option, index)
        if index.data(FLUSH_ROLE):
            option.rect = option.rect.adjusted(-self.tree.indentation(), 0, 0, 0)


class PopoutWindow(QWidget):
    """The pop-out lesson window, with a dock control. Closing it also docks the lesson."""

    def __init__(self, on_dock) -> None:
        super().__init__()
        self.on_dock = on_dock
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        dock_bar = QHBoxLayout()
        dock_bar.setContentsMargins(8, 4, 8, 4)
        dock_bar.addStretch(1)
        dock = QToolButton()
        dock.setIcon(draw_icon("dock", DARK["muted"]))
        dock.setToolTip("Dock lesson back into the main window")
        dock.clicked.connect(self.on_dock)
        dock_bar.addWidget(dock)
        layout.addLayout(dock_bar)
        self.view = QWebEngineView()
        self.view.settings().setAttribute(
            QWebEngineSettings.WebAttribute.LocalContentCanAccessFileUrls, True)
        layout.addWidget(self.view, 1)

    def closeEvent(self, event) -> None:  # pylint: disable=invalid-name
        """Closing the pop-out window also docks the lesson back into the main window."""
        self.on_dock()
        super().closeEvent(event)
