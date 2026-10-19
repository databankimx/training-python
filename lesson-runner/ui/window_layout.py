"""Window layout: builds the widgets for the main window. Used as a mixin by MainWindow."""

#pylint: disable=line-too-long

from __future__ import annotations

from PySide6.QtCore import QTimer, Qt #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtGui import QColor, QKeySequence, QShortcut #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWebEngineCore import QWebEngineSettings #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWebEngineWidgets import QWebEngineView #pylint: disable=no-name-in-module #NOSONAR
from PySide6.QtWidgets import (QComboBox, QFrame, QHBoxLayout, QLabel, QLineEdit, QListWidget, QPlainTextEdit, #pylint: disable=no-name-in-module #NOSONAR
                               QPushButton, QSplitter, QStackedWidget, QTabWidget, QToolButton, #pylint: disable=no-name-in-module #NOSONAR
                               QTreeWidget, QVBoxLayout, QWidget) #pylint: disable=no-name-in-module #NOSONAR

from config import DARK
from ui.icons import logo_pixmap
from ui.theme import code_font
from ui.widgets import PythonHighlighter, SourceEditor, ThemeSwitch, TreeDelegate


class LayoutMixin:
    """Creates the widgets and lays them out. Expects the window to provide the handlers it connects to."""

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
        self.header_logo.setToolTip("DataBank IMX Python Training")
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
        self.tree.setItemDelegate(TreeDelegate(self.tree))
        self.tree.currentItemChanged.connect(self.on_tree_changed)
        self.tree.currentItemChanged.connect(self.stop_run_on_leaving)
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
        self.step_list.currentRowChanged.connect(self.stop_run_on_leaving)
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
        title_bar = QFrame()
        layout = QHBoxLayout(title_bar)
        layout.setContentsMargins(12, 8, 12, 8)
        titles = QVBoxLayout()
        self.title_label = QLabel("Select a step from the left panel")
        self.title_label.setObjectName("title")
        self.subtitle_label = QLabel("")
        self.subtitle_label.setObjectName("subtitle")
        titles.addWidget(self.title_label)
        titles.addWidget(self.subtitle_label)
        self.badge_row = QHBoxLayout()
        self.badge_row.setSpacing(6)
        titles.addLayout(self.badge_row)
        layout.addLayout(titles, 1)

        self.moon_label = QLabel()
        self.moon_label.setToolTip("Dark theme")
        layout.addWidget(self.moon_label)
        self.theme_switch = ThemeSwitch()
        self.theme_switch.setToolTip("Switch between the dark and light theme")
        self.theme_switch.toggled.connect(self.on_theme_switch)
        layout.addWidget(self.theme_switch)
        self.sun_label = QLabel()
        self.sun_label.setToolTip("Light theme")
        layout.addWidget(self.sun_label)
        layout.addSpacing(12)

        self.visualize_button = QPushButton("Visualize")
        self.visualize_button.setToolTip("Open this algorithm's step-through visualization in the browser")
        self.visualize_button.hide()
        self.visualize_button.clicked.connect(self.open_visualization)
        layout.addWidget(self.visualize_button)
        layout.addSpacing(8)
        self.run_button = QPushButton("\u25B6  Run")
        self.run_button.setObjectName("run")
        self.run_button.setToolTip("Run this step (F5)")
        self.run_button.setEnabled(False)
        self.run_button.clicked.connect(self.start_run)
        layout.addWidget(self.run_button)
        return title_bar

    def build_args_bar(self) -> QWidget:
        """Command-line arguments passed to the step."""
        args_bar = QFrame()
        layout = QHBoxLayout(args_bar)
        layout.setContentsMargins(12, 4, 12, 6)
        label = QLabel("args:")
        label.setFont(code_font(10))
        label.setToolTip("Command-line arguments passed to the step. Quotes work as in a shell.")
        layout.addWidget(label)
        self.args_edit = QLineEdit()
        self.args_edit.setFont(code_font(10))
        self.args_edit.setToolTip("Command-line arguments passed to the step when it runs")
        layout.addWidget(self.args_edit, 1)
        return args_bar

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
        self.continue_button.setToolTip("Continue the paused run (Ctrl+Shift+Enter)")
        self.continue_button.clicked.connect(self.continue_run)
        self.continue_button.hide()
        header_layout.addWidget(self.continue_button)
        self.output_copy = QToolButton()
        self.output_copy.setToolTip("Copy output")
        self.output_copy.clicked.connect(lambda: self.copy_text(self.output.toPlainText(), self.output_copy))
        header_layout.addWidget(self.output_copy)
        self.view_file_button = QPushButton("View file")
        self.view_file_button.setToolTip("Open the file this step saved")
        self.view_file_button.clicked.connect(self.view_saved_file)
        self.view_file_button.hide()
        header_layout.addWidget(self.view_file_button)
        self.open_browser_button = QPushButton("Open in browser")
        self.open_browser_button.setToolTip("Open the running site in your browser")
        self.open_browser_button.clicked.connect(self.open_running_site)
        self.open_browser_button.hide()
        header_layout.addWidget(self.open_browser_button)
        clear = QPushButton("Clear")
        clear.setToolTip("Clear the output")
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

        self.file_picker = QComboBox()
        self.file_picker.setToolTip("Choose which of this step's files to view")
        self.file_picker.setVisible(False)
        self.file_picker.currentTextChanged.connect(self.on_file_picked)
        layout.addWidget(self.file_picker)

        self.reset_bar = QFrame()
        self.reset_bar.setObjectName("resetBar")
        reset_layout = QHBoxLayout(self.reset_bar)
        reset_layout.setContentsMargins(8, 3, 8, 3)
        self.edited_label = QLabel("\u25CF Code has been edited")
        self.edited_label.setToolTip("The code differs from the original file. Runs use the edited code.")
        reset_layout.addWidget(self.edited_label)
        reset_layout.addStretch(1)
        reset = QPushButton("Reset to original")
        reset.setToolTip("Restore the original code (Esc)")
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
        self.lesson_view.loadFinished.connect(self.on_lesson_loaded)
        placeholder = QWidget()
        place_layout = QVBoxLayout(placeholder)
        place_layout.addStretch(1)
        note = QLabel("The lesson is open in a separate window.")
        note.setAlignment(Qt.AlignmentFlag.AlignCenter)
        place_layout.addWidget(note)
        dock = QPushButton("Dock lesson back here")
        dock.setObjectName("continue")
        dock.setToolTip("Show the lesson in the main window again")
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
