"""Chapter tree and step list. Used as a mixin by MainWindow."""

# pylint: disable=line-too-long

from __future__ import annotations

from typing import TYPE_CHECKING

from PySide6.QtCore import QSize, Qt #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWidgets import QListWidgetItem, QTreeWidgetItem #pylint: disable=no-name-in-module #NOSONAR

if TYPE_CHECKING:
    from core.discovery import Chapter


class NavigationMixin:
    """Fills the chapter tree and moves between chapters and steps."""

    def populate_tree(self) -> None:
        """Fill the chapter tree. Each chapter stores its Chapter object in the item."""
        for scope in self.scopes:
            scope_item = QTreeWidgetItem([scope.name])
            scope_item.setFlags(Qt.ItemFlag.ItemIsEnabled)
            scope_item.setSizeHint(0, QSize(0, 26))
            self.tree.addTopLevelItem(scope_item)
            for chapter in scope.chapters:
                scope_item.addChild(self.chapter_item(chapter))
            scope_item.setExpanded(False)

    def chapter_item(self, chapter: Chapter) -> QTreeWidgetItem:
        """A tree item for a chapter, with its nested children (such as Try it Yourself)."""
        item = QTreeWidgetItem([chapter.name])
        item.setData(0, Qt.ItemDataRole.UserRole, chapter)
        item.setSizeHint(0, QSize(0, 24))
        for child in chapter.children:
            item.addChild(self.chapter_item(child))
        item.setExpanded(False)
        return item

    def first_child_with_steps(self, item: QTreeWidgetItem) -> QTreeWidgetItem | None:
        """The first child (searching down) whose chapter has steps of its own."""
        for index in range(item.childCount()):
            child = item.child(index)
            chapter = child.data(0, Qt.ItemDataRole.UserRole)
            if chapter is not None and chapter.steps:
                return child
            found = self.first_child_with_steps(child)
            if found is not None:
                return found
        return None

    def on_tree_changed(self, current: QTreeWidgetItem | None, _previous: QTreeWidgetItem | None) -> None:
        """Load the chapter's steps when a chapter is selected."""
        if current is None:
            return
        chapter = current.data(0, Qt.ItemDataRole.UserRole)
        if chapter is None:
            return
        if not chapter.steps:
            # A chapter with no steps of its own (such as Ch11) moves to its first sub-chapter.
            first = self.first_child_with_steps(current)
            if first is not None:
                current.setExpanded(True)
                self.tree.setCurrentItem(first)
                return
        self.chapter = chapter
        self.step_list.blockSignals(True)
        self.step_list.clear()
        for step in chapter.steps:
            item = QListWidgetItem(("\u2003\u2003" if step.indented else "") + step.title)
            item.setSizeHint(QSize(0, 26))
            self.step_list.addItem(item)
        if chapter.steps:
            self.step_list.setCurrentRow(0)
        self.step_list.blockSignals(False)
        if chapter.steps:
            # Called once, here, so each selection loads the step exactly once.
            self.on_step_changed(0)

    def on_step_changed(self, row: int) -> None:
        """Show the chosen step."""
        if self.chapter is None or row < 0 or row >= len(self.chapter.steps):
            return
        self.show_step(self.chapter.steps[row])
