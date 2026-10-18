"""Source panel: loads a step into the editor and lesson, and handles the source controls.
Used as a mixin by MainWindow."""

from __future__ import annotations

import traceback

from PySide6.QtCore import QUrl
from PySide6.QtGui import QDesktopServices
from PySide6.QtWidgets import QFrame, QHBoxLayout, QLabel

from config import C_NOTE, HERE, VISUALIZATIONS
from core import discovery
from core.source_tools import BADGE_GLYPHS, step_badges, strip_lint_comments
from core.stages import stage_files, strip_front_matter
from ui.icons import draw_icon

#pylint: disable=line-too-long

MAIN_FILE = "alien_invasion.py"


class SourcePanelMixin:
    """Shows a step's source, its badges, and its edit and visualization controls."""

    def show_step(self, step: discovery.Step) -> None:
        """Load a step into the window: its source, lesson, badges and buttons."""
        self.step = step
        self.title_label.setText(step.title)
        origin = step.code_path or step.lesson_md
        name = origin.name if origin else ""
        self.subtitle_label.setText(f"{self.chapter.name}  \u00b7  {name}" if name else self.chapter.name)
        self.args_edit.clear()
        self.set_dirty(False)

        if step.stage is not None:
            badge_source = self.show_stage(step)
        elif step.kind == "exercise":
            badge_source = self.show_exercise(step)
        else:
            badge_source = self.show_single_file(step)
        self.set_badges(badge_source)

        if step.note:
            self.lesson_markdown = step.note
            self.lesson_base = HERE
        else:
            lesson_path = step.lesson_md or (self.chapter.intro_md if self.chapter else None)
            if lesson_path:
                self.lesson_markdown = strip_front_matter(lesson_path.read_text(encoding="utf-8"))
            else:
                self.lesson_markdown = "No lesson text for this step."
            self.lesson_base = lesson_path.parent if lesson_path else HERE
        self.render_lesson_page()
        self.clear_output()
        self.view_file_button.hide()
        self.saved_files = []
        self.run_button.setEnabled(step.runnable)
        self.visualize_button.setVisible(self.visualization_key() is not None)

    def show_single_file(self, step: discovery.Step) -> str:
        """A step with one file: the whole file, editable, as before."""
        self.stage = None
        self.multi_file = False
        self.stage_base = {}
        self.stage_texts = {}
        self.current_file = None
        self.file_picker.setVisible(False)
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
        return source

    def show_stage(self, step: discovery.Step) -> str:
        """A stage: a file menu of every project file at this step. Returns the main file's text."""
        self.stage = step.stage
        try:
            base = stage_files(self.stage)
        except Exception:  # pylint: disable=broad-exception-caught
            # Show the error in the editor, so a failed build is visible rather than silent.
            self.multi_file = True
            self.stage_base = {}
            self.stage_texts = {}
            self.current_file = None
            self.file_picker.setVisible(False)
            self.highlighter.set_language("python")
            self.editor.setReadOnly(False)
            self.editor.blockSignals(True)
            self.editor.setPlainText("Could not build this step:\n\n" + traceback.format_exc())
            self.editor.blockSignals(False)
            self.original_source = ""
            return ""
        return self.show_file_set(base, MAIN_FILE, self.default_stage_file(base))

    def show_exercise(self, step: discovery.Step) -> str:
        """An exercise: every .py file in its folder, editable. Returns the main file's text."""
        self.stage = None
        folder = step.code_path.parent
        base = {}
        for path in sorted(folder.glob("*.py")):
            base[path.name] = path.read_text(encoding="utf-8")
        return self.show_file_set(base, step.code_path.name, step.code_path.name)

    def show_file_set(self, base: dict[str, str], main: str, default: str) -> str:
        """Show a set of files in the drop-down, opening on default. Returns the main file's text."""
        # Lint comments are never shown in the runner, so strip them from every file in the set.
        base = {name: strip_lint_comments(text) for name, text in base.items()}
        self.multi_file = True
        self.stage_base = base
        self.stage_texts = {}
        self.current_file = None
        names = sorted(base, key=lambda n: (n != main, n))
        self.file_picker.blockSignals(True)
        self.file_picker.clear()
        self.file_picker.addItems(names)
        self.file_picker.setVisible(len(names) > 1)
        self.file_picker.blockSignals(False)
        if names:
            self.show_stage_file(default if default in base else names[0])
        return base.get(main, "")

    def default_stage_file(self, base: dict[str, str]) -> str:
        """The file to open first: a file this step adds, if it adds one; otherwise alien_invasion.py."""
        added = sorted(p.name for p in self.stage.folder.glob("*.py") if p.name != MAIN_FILE)
        for name in added:
            if name in base:
                return name
        return MAIN_FILE if MAIN_FILE in base else sorted(base)[0]

    def show_stage_file(self, name: str) -> None:
        """Show one file of the set, and keep the file menu in step with it.

        The editor and the menu change together, with signals blocked, so the menu can't
        trigger a second switch while the text is being set.
        """
        if not self.multi_file or name not in self.stage_base:
            return
        self.current_file = name
        base = self.stage_base[name]
        text = self.stage_texts.get(name, base)

        self.file_picker.blockSignals(True)
        self.file_picker.setCurrentText(name)
        self.file_picker.blockSignals(False)

        self.highlighter.set_language("python")
        self.editor.setReadOnly(False)
        self.editor.blockSignals(True)
        self.editor.setPlainText(text)
        self.editor.blockSignals(False)
        self.shown_text = self.editor.toPlainText()
        self.original_source = base
        self.set_dirty(text != base)

    def on_file_picked(self, name: str) -> None:
        """The file menu changed: show that file."""
        if self.multi_file and name:
            self.show_stage_file(name)

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
        """Track typed edits per file. The reset bar shows while a file differs from this step's version."""
        if self.multi_file:
            if self.current_file is None:
                return
            text = self.editor.toPlainText()
            if text == self.shown_text:
                # Nothing was typed: the editor is showing what we loaded, so it is not an edit.
                return
            self.shown_text = text
            base = self.stage_base.get(self.current_file, "")
            if text == base:
                self.stage_texts.pop(self.current_file, None)
            else:
                self.stage_texts[self.current_file] = text
            self.set_dirty(text != base)
            return
        self.set_dirty(self.editor.toPlainText() != self.original_source)

    def set_dirty(self, dirty: bool) -> None:
        """Show or hide the reset bar."""
        self.reset_bar.setVisible(dirty)

    def reset_source(self) -> None:
        """Restore the original code, for the current file when the step has several."""
        if self.multi_file and self.current_file:
            self.stage_texts.pop(self.current_file, None)
            self.show_stage_file(self.current_file)
            return
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
