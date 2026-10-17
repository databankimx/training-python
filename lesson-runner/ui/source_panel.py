"""Source panel: loads a step into the editor and lesson view, and handles the source controls.
Used as a mixin by MainWindow."""

from __future__ import annotations

from PySide6.QtCore import QUrl #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtGui import QDesktopServices #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel #pylint: disable=no-name-in-module #NOSONAR

from core import discovery
from config import C_NOTE, HERE, VISUALIZATIONS
from core.source_tools import BADGE_GLYPHS, step_badges, strip_lint_comments
from ui.icons import draw_icon

#pylint: disable=line-too-long

class SourcePanelMixin:
    """Shows a step's source, its badges, and its edit and visualization controls."""

    def show_step(self, step: discovery.Step) -> None:
        """Load a step's source, lesson and title into the window."""
        self.step = step
        self.title_label.setText(step.title)
        origin = step.code_path or step.lesson_md
        name = origin.name if origin else ""
        self.subtitle_label.setText(f"{self.chapter.name}  \u00b7  {name}" if name else self.chapter.name)
        self.args_edit.clear()
        if step.code_path is None:
            source = discovery.NO_SOURCE_TEXT
        else:
            source = strip_lint_comments(step.code_path.read_text(encoding="utf-8"))
            if step.kind == "source":
                # C samples: highlight as C, and say that this runner can't compile or run them.
                source = C_NOTE + source
        self.highlighter.set_language("c" if step.kind == "source" else "python")
        self.editor.blockSignals(True)
        self.editor.setPlainText(source)
        self.editor.blockSignals(False)
        self.original_source = source
        self.set_badges(source)
        self.set_dirty(False)
        if step.note:
            self.lesson_markdown = step.note
            self.lesson_base = HERE
        else:
            lesson_path = step.lesson_md or (self.chapter.intro_md if self.chapter else None)
            self.lesson_markdown = (lesson_path.read_text(encoding="utf-8") if lesson_path
                                    else "No lesson text for this step.")
            self.lesson_base = lesson_path.parent if lesson_path else HERE
        self.render_lesson_page()
        self.clear_output()
        self.view_file_button.hide()
        self.saved_files = []
        self.run_button.setEnabled(step.runnable)
        self.visualize_button.setVisible(self.visualization_key() is not None)

    def set_badges(self, source: str) -> None:
        """Remember the badges for this step, then show them."""
        badges = step_badges(source)
        if self.visualization_key() is not None and "Browser" not in dict(badges):
            # Algorithm steps open their animation from the Visualize button, not from the code.
            badges.insert(0, ("Browser", "Opens in browser"))
        self.badge_items = badges
        self.rebuild_badges()

    def rebuild_badges(self) -> None:
        """Show the current step's badges in the current theme."""
        while self.badge_row.count():
            item = self.badge_row.takeAt(0)
            if item.widget() is not None:
                item.widget().deleteLater()
        for label, tip in self.badge_items:
            self.badge_row.addWidget(self.make_badge(label, tip))
        self.badge_row.addStretch(1)

    def make_badge(self, label: str, tip: str) -> QFrame:
        """A badge: an optional glyph and its label, on the accent background, with the tooltip."""
        badge = QFrame()
        badge.setObjectName("badge")
        layout = QHBoxLayout(badge)
        layout.setContentsMargins(8, 2, 8, 2)
        layout.setSpacing(5)
        glyph = BADGE_GLYPHS.get(label)
        if glyph is not None:
            icon = QLabel()
            icon.setPixmap(draw_icon(glyph, self.colors["fg"], 14).pixmap(14, 14))
            icon.setToolTip(tip)
            layout.addWidget(icon)
        text = QLabel(label)
        text.setObjectName("badgeText")
        text.setToolTip(tip)
        layout.addWidget(text)
        badge.setToolTip(tip)
        return badge

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

    def visualization_key(self) -> str | None:
        """The VISUALIZATIONS key for the current step, or None if it has no visualization."""
        if self.step is None or self.step.code_path is None:
            return None
        key = f"{self.step.code_path.parent.name}/{self.step.code_path.stem}"
        return key if key in VISUALIZATIONS else None

    def open_visualization(self) -> None:
        """Open the current step's algorithm in the visualization player, in the default browser."""
        key = self.visualization_key()
        if key is None:
            return
        visualizations = self.step.code_path.parent / "visualizations"
        # Windows drops the query string when a file:// address is opened, so the chosen
        # algorithm is written to current-algorithm.js, which the player reads.
        (visualizations / "current-algorithm.js").write_text(
            f'window.CURRENT_ALGORITHM = "{VISUALIZATIONS[key]}";\n', encoding="utf-8")
        QDesktopServices.openUrl(QUrl.fromLocalFile(str(visualizations / "player.html")))
