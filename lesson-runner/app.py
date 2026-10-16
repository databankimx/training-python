"""DataBank IMX Developer Training - Python lesson runner (tkinter).

Run from the lesson-runner folder with the same interpreter that runs the
training lessons (the one with ``sm_utils`` installed):

    python app.py
"""

from __future__ import annotations

import builtins
import io
import keyword
import queue
import shlex
import tkinter as tk
import tokenize
from tkinter import ttk

import discovery
import logo
from discovery import Chapter, Step
from runner import StepRun
from lesson_view import LessonWindow, MarkdownText
from syntax import SYNTAX_TAGS, python_spans

DARK = {
    "bg": "#1E1E1E", "panel": "#252526", "border": "#3F3F46", "fg": "#D4D4D4",
    "accent": "#007ACC", "accent_hover": "#1C97EA", "success": "#4EC9B0",
    "error": "#F44747", "muted": "#858585", "selection": "#264F78",
    "row_hover": "#2A2D2E", "white": "#FFFFFF",
    "heading": "#569CD6", "code_bg": "#0A0A0A", "code_fg": "#D4D4D4", "rule": "#3F3F46",
    "kw": "#569CD6", "ctl": "#C586C0", "str": "#CE9178", "com": "#6A9955", "num": "#B5CEA8",
    "typ": "#4EC9B0", "fn": "#DCDCAA", "var": "#9CDCFE",
}
LIGHT = {
    "bg": "#FFFFFF", "panel": "#F3F3F3", "border": "#CCCEDB", "fg": "#1E1E1E",
    "accent": "#007ACC", "accent_hover": "#1C97EA", "success": "#007F5F",
    "error": "#CC0000", "muted": "#717171", "selection": "#ADD6FF",
    "row_hover": "#E8E8E8", "white": "#FFFFFF",
    "heading": "#0451A5", "code_bg": "#F5F5F5", "code_fg": "#1E1E1E", "rule": "#CCCEDB",
    "kw": "#0000FF", "ctl": "#AF00DB", "str": "#A31515", "com": "#008000", "num": "#098658",
    "typ": "#267F99", "fn": "#795E26", "var": "#001080",
}

BUILTIN_NAMES = set(dir(builtins))

UI_FONT = ("Segoe UI", 10)
UI_BOLD = ("Segoe UI", 10, "bold")
CODE_FONT = ("Consolas", 11)


class ToggleSwitch(tk.Canvas):
    """Pill-shaped light/dark switch, matching the WPF title bar toggle."""

    def __init__(self, master: tk.Misc, command) -> None:
        super().__init__(master, width=40, height=20, highlightthickness=0, bd=0, cursor="hand2")
        self.command = command
        self.light = False
        self.bind("<Button-1>", lambda _event: self.command())

    def set_state(self, light: bool, colors: dict) -> None:
        """Redraw the switch for the given state and palette."""
        self.light = light
        self.delete("all")
        track = colors["accent"] if light else colors["border"]
        self.create_oval(0, 0, 20, 20, fill=track, outline=track)
        self.create_oval(20, 0, 40, 20, fill=track, outline=track)
        self.create_rectangle(10, 0, 30, 20, fill=track, outline=track)
        x = 22 if light else 2
        self.create_oval(x, 2, x + 16, 18, fill=colors["white"], outline=colors["white"])


class App(tk.Tk):
    """Main window: chapter and step navigation, step title, output, and source."""

    def __init__(self) -> None:
        super().__init__()
        self.title("DataBank IMX - Python Training")
        self.icon_image = logo.icon_photo(self, 32, DARK["accent"])
        self.iconphoto(True, self.icon_image)
        self.geometry("1280x768")
        self.minsize(800, 500)

        self.theme = "dark"
        self.colors = DARK
        self.paint: list[tuple[tk.Misc, dict[str, str]]] = []
        self.scopes = discovery.discover()
        self.chapters: dict[str, Chapter] = {}
        self.chapter: Chapter | None = None
        self.step: Step | None = None
        self.original_source = ""
        self.run: StepRun | None = None
        self.waiting_for_continue = False
        self.suppress_modified = False
        self.lesson_markdown = ""
        self.popout: LessonWindow | None = None

        self.style = ttk.Style(self)
        self.style.theme_use("clam")

        self.build_layout()
        self.populate_tree()
        self.bind_keys()
        self.apply_theme()
        self.after(150, self.set_chapter_split)

    # ------------------------------------------------------------------
    # Layout
    # ------------------------------------------------------------------

    def set_chapter_split(self) -> None:
        """Give the chapter tree 60% of the left panel's height and the step list 40%."""
        height = self.left_paned.winfo_height()
        if height > 1:
            self.left_paned.sash_place(0, 0, int(height * 0.6))
        else:
            self.after(100, self.set_chapter_split)

    def refresh_run_button(self) -> None:
        """Solid accent with white text when Run is available. When it is not, a neutral
        background with readable text, so the disabled state does not look like dim text on blue."""
        c = self.colors
        enabled = str(self.run_button.cget("state")) == "normal"
        if enabled:
            background, foreground = c["accent"], c["white"]
        else:
            background, foreground = c["border"], c["fg"]
        self.run_button.configure(bg=background, fg=foreground, disabledforeground=foreground,
                                  activebackground=c["accent_hover"] if enabled else background,
                                  activeforeground=foreground)

    def track(self, widget: tk.Misc, **options: str) -> tk.Misc:
        """Remember which palette keys a widget uses, so the theme can repaint it."""
        self.paint.append((widget, options))
        return widget

    def build_layout(self) -> None:
        """Create every widget in the window."""
        self.left = self.track(tk.Frame(self, width=240), bg="panel")
        self.left.pack(side="left", fill="y")
        self.left.pack_propagate(False)

        header = self.track(tk.Frame(self.left, padx=10, pady=8), bg="accent")
        header.pack(fill="x")
        self.logo_canvas = self.track(tk.Canvas(header, width=22, height=22, bd=0, highlightthickness=0),
                                      bg="accent")
        self.logo_canvas.pack(side="left", padx=(0, 8))
        logo.draw_on_canvas(self.logo_canvas, 22, "#FFFFFF")
        self.track(tk.Label(header, text="Python Training", font=("Segoe UI", 13, "bold")),
                   bg="accent", fg="white").pack(side="left")

        self.track(tk.Label(self.left, text="CHAPTERS", font=("Segoe UI", 8, "bold"), anchor="w",
                            padx=10, pady=4), bg="panel", fg="muted").pack(fill="x")

        left_paned = tk.PanedWindow(self.left, orient="vertical", sashwidth=4, bd=0, sashrelief="flat")
        self.left_paned = left_paned
        self.track(left_paned, bg="border")
        left_paned.pack(fill="both", expand=True)

        tree_frame = self.track(tk.Frame(left_paned), bg="panel")
        self.tree = ttk.Treeview(tree_frame, show="tree", selectmode="browse", style="Lesson.Treeview")
        tree_scroll = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=tree_scroll.set)
        self.tree.pack(side="left", fill="both", expand=True)
        tree_scroll.pack(side="right", fill="y")
        self.tree.bind("<<TreeviewSelect>>", self.on_chapter_selected)
        left_paned.add(tree_frame, minsize=80)

        steps_frame = self.track(tk.Frame(left_paned), bg="panel")
        self.track(tk.Label(steps_frame, text="STEPS", font=("Segoe UI", 8, "bold"), anchor="w",
                            padx=10, pady=4), bg="panel", fg="muted").pack(fill="x")
        step_box = tk.Frame(steps_frame)
        self.step_list = tk.Listbox(step_box, exportselection=False, activestyle="none", borderwidth=0,
                                    highlightthickness=0, font=UI_FONT)
        step_scroll = ttk.Scrollbar(step_box, orient="vertical", command=self.step_list.yview)
        self.step_list.configure(yscrollcommand=step_scroll.set)
        self.step_list.pack(side="left", fill="both", expand=True)
        step_scroll.pack(side="right", fill="y")
        step_box.pack(fill="both", expand=True, padx=(8, 0))
        self.step_list.bind("<<ListboxSelect>>", self.on_step_selected)
        self.track(self.step_list, bg="panel", fg="fg", selectbackground="selection",
                   selectforeground="fg")
        left_paned.add(steps_frame, minsize=80)

        self.right = self.track(tk.Frame(self), bg="bg")
        self.right.pack(side="left", fill="both", expand=True)
        self.build_title_bar()
        self.build_args_bar()
        self.build_body()

    def build_title_bar(self) -> None:
        """Step title on the left; theme switch and Run on the right."""
        bar = self.track(tk.Frame(self.right, padx=12, pady=8), bg="panel")
        bar.pack(fill="x")

        titles = self.track(tk.Frame(bar), bg="panel")
        titles.pack(side="left", fill="x", expand=True)
        self.title_text = self.track(tk.Label(titles, text="Select a step from the left panel",
                                              font=("Segoe UI", 14, "bold"), anchor="w"),
                                     bg="panel", fg="fg")
        self.title_text.pack(fill="x")
        self.subtitle_text = self.track(tk.Label(titles, text="", font=("Segoe UI", 9), anchor="w"),
                                        bg="panel", fg="muted")
        self.subtitle_text.pack(fill="x")

        controls = self.track(tk.Frame(bar), bg="panel")
        controls.pack(side="right")
        self.track(tk.Label(controls, text="\U0001F319", font=("Segoe UI", 10)),
                   bg="panel", fg="muted").pack(side="left", padx=(0, 4))
        self.theme_switch = ToggleSwitch(controls, self.toggle_theme)
        self.theme_switch.configure(bg=self.colors["panel"])
        self.theme_switch.pack(side="left")
        self.track(tk.Label(controls, text="\u2600", font=("Segoe UI", 10)),
                   bg="panel", fg="muted").pack(side="left", padx=(4, 16))

        self.run_button = tk.Button(controls, text="\u25B6  Run", font=UI_BOLD, state="disabled",
                                    command=self.start_run, relief="flat", padx=12, pady=4,
                                    cursor="hand2", bd=0)
        self.run_button.pack(side="left")
        self.track(self.run_button, bg="accent", fg="white", activebackground="accent_hover",
                   activeforeground="white", disabledforeground="muted")

    def build_args_bar(self) -> None:
        """Command-line arguments passed to the step's sys.argv."""
        bar = self.track(tk.Frame(self.right, padx=12, pady=6), bg="panel")
        bar.pack(fill="x")
        self.track(tk.Label(bar, text="args:", font=("Consolas", 10)), bg="panel", fg="muted").pack(side="left")
        self.args_entry = tk.Entry(bar, font=("Consolas", 10), relief="flat", bd=0, highlightthickness=1)
        self.args_entry.pack(side="left", fill="x", expand=True, padx=(8, 0), ipady=3)
        self.track(self.args_entry, bg="bg", fg="fg", insertbackground="fg",
                   highlightbackground="border", highlightcolor="border")

    def build_body(self) -> None:
        """Output pane above; Source and Lesson tabs below."""
        body = tk.PanedWindow(self.right, orient="vertical", sashwidth=4, bd=0, sashrelief="flat")
        self.track(body, bg="border")
        body.pack(fill="both", expand=True)

        output_frame = self.track(tk.Frame(body), bg="bg")
        header = self.track(tk.Frame(output_frame, padx=12, pady=4), bg="panel")
        header.pack(fill="x")
        self.track(tk.Label(header, text="OUTPUT", font=("Segoe UI", 8, "bold")),
                   bg="panel", fg="muted").pack(side="left")

        self.clear_button = tk.Button(header, text="Clear", command=self.clear_output, relief="flat",
                                      bd=0, font=("Segoe UI", 8), padx=6)
        self.clear_button.pack(side="right")
        self.track(self.clear_button, bg="panel", fg="muted", activebackground="panel")
        self.copy_button = tk.Button(header, text="Copy", command=self.copy_output, relief="flat",
                                     bd=0, font=("Segoe UI", 8), padx=6)
        self.copy_button.pack(side="right")
        self.track(self.copy_button, bg="panel", fg="muted", activebackground="panel")
        self.continue_button = tk.Button(header, text="\u25B6  Continue", command=self.continue_run,
                                         relief="flat", bd=0, font=UI_BOLD, padx=10, pady=2,
                                         cursor="hand2")
        self.track(self.continue_button, bg="accent", fg="white", activebackground="accent_hover",
                   activeforeground="white")

        self.output = tk.Text(output_frame, wrap="word", font=CODE_FONT, bd=0, padx=12, pady=8,
                              highlightthickness=0, state="disabled", height=10)
        output_scroll = ttk.Scrollbar(output_frame, orient="vertical", command=self.output.yview)
        self.output.configure(yscrollcommand=output_scroll.set)
        output_scroll.pack(side="right", fill="y")
        self.output.pack(fill="both", expand=True)
        self.track(self.output, bg="bg", fg="fg", insertbackground="fg")
        body.add(output_frame, minsize=80)

        tabs = ttk.Notebook(body, style="Lesson.TNotebook")
        body.add(tabs, minsize=120)
        self.build_source_tab(tabs)
        self.build_lesson_tab(tabs)

    def build_source_tab(self, tabs: ttk.Notebook) -> None:
        """Editable source with line numbers, highlighting, and a reset bar."""
        frame = self.track(tk.Frame(tabs), bg="bg")
        tabs.add(frame, text="Source")

        toolbar = self.track(tk.Frame(frame, padx=8, pady=3), bg="panel")
        toolbar.pack(fill="x")
        self.copy_source_button = self.make_copy_button(toolbar, self.copy_source)

        self.reset_bar = self.track(tk.Frame(frame, padx=8, pady=4), bg="panel")
        self.track(tk.Label(self.reset_bar, text="\u25CF Code has been edited", font=("Segoe UI", 9)),
                   bg="panel", fg="muted").pack(side="left")
        self.reset_button = tk.Button(self.reset_bar, text="Reset to original", command=self.reset_source,
                                      relief="flat", bd=0, font=("Segoe UI", 9), padx=8, pady=2)
        self.reset_button.pack(side="right")
        self.track(self.reset_button, bg="panel", fg="fg", activebackground="panel")

        editor = tk.Frame(frame)
        editor.pack(fill="both", expand=True)
        self.gutter = self.track(tk.Text(editor, width=4, font=CODE_FONT, bd=0, padx=6, pady=8,
                                         highlightthickness=0, state="disabled", cursor="arrow",
                                         takefocus=0), bg="bg", fg="muted")
        self.gutter.pack(side="left", fill="y")
        self.gutter.tag_configure("right", justify="right")

        self.source = tk.Text(editor, wrap="word", font=CODE_FONT, bd=0, padx=8, pady=8,
                              highlightthickness=0, undo=True, maxundo=-1)
        source_scroll = ttk.Scrollbar(editor, orient="vertical", command=self.scroll_source)
        self.source.configure(yscrollcommand=lambda first, last: self.on_source_scrolled(source_scroll, first, last))
        source_scroll.pack(side="right", fill="y")
        self.source.pack(side="left", fill="both", expand=True)
        self.track(self.source, bg="bg", fg="fg", insertbackground="fg", selectbackground="selection")
        self.source.bind("<<Modified>>", self.on_source_modified)
        self.source_scroll = source_scroll

    def build_lesson_tab(self, tabs: ttk.Notebook) -> None:
        """Lesson Markdown. Phase 3 replaces this plain view with a rendered one."""
        frame = self.track(tk.Frame(tabs), bg="bg")
        tabs.add(frame, text="Lesson")
        toolbar = self.track(tk.Frame(frame, padx=8, pady=3), bg="panel")
        toolbar.pack(fill="x")
        self.copy_lesson_button = self.make_copy_button(toolbar, self.copy_lesson)
        self.popout_button = self.make_copy_button(toolbar, self.toggle_popout)
        self.popout_button.configure(text="Pop out")
        self.lesson_body = self.track(tk.Frame(frame), bg="bg")
        self.lesson_body.pack(fill="both", expand=True)
        self.lesson = MarkdownText(self.lesson_body, self.colors)
        lesson_scroll = ttk.Scrollbar(self.lesson_body, orient="vertical", command=self.lesson.yview)
        self.lesson.configure(yscrollcommand=lesson_scroll.set)
        lesson_scroll.pack(side="right", fill="y")
        self.lesson.pack(fill="both", expand=True)

        self.placeholder = self.track(tk.Frame(frame), bg="bg")
        self.track(tk.Label(self.placeholder, text="The lesson is open in a separate window.",
                            font=UI_FONT), bg="bg", fg="muted").pack(pady=(60, 12))
        self.track(tk.Button(self.placeholder, text="Dock lesson back here", command=self.dock_lesson,
                             relief="flat", bd=0, font=UI_BOLD, padx=14, pady=6, cursor="hand2"),
                   bg="accent", fg="white", activebackground="accent_hover").pack()

    def bind_keys(self) -> None:
        """Keyboard shortcuts, matching the WPF app."""
        self.bind("<F5>", lambda _event: self.start_run() or "break")
        self.bind("<Escape>", self.on_escape)
        self.bind("<Control-Shift-Return>", self.on_continue_key)

    # ------------------------------------------------------------------
    # Theme
    # ------------------------------------------------------------------

    def apply_theme(self) -> None:
        """Repaint every tracked widget and the tree and notebook styles."""
        c = self.colors
        self.configure(bg=c["bg"])
        for widget, options in self.paint:
            values = {option: c[key] for option, key in options.items()}
            try:
                widget.configure(**values)
            except tk.TclError:
                pass

        self.style.configure("Lesson.Treeview", background=c["panel"], fieldbackground=c["panel"],
                             foreground=c["fg"], rowheight=24, borderwidth=0, font=UI_FONT)
        self.style.map("Lesson.Treeview", background=[("selected", c["accent"])],
                       foreground=[("selected", c["white"])])
        self.style.configure("Lesson.TNotebook", background=c["bg"], borderwidth=0)
        self.style.configure("Lesson.TNotebook.Tab", background=c["panel"], foreground=c["muted"],
                             padding=(14, 6), font=("Segoe UI", 9, "bold"), borderwidth=0)
        self.style.map("Lesson.TNotebook.Tab", background=[("selected", c["bg"])],
                       foreground=[("selected", c["fg"])])
        self.style.configure("Vertical.TScrollbar", background=c["border"], troughcolor=c["bg"],
                             bordercolor=c["bg"], arrowcolor=c["muted"])

        self.continue_button.configure(bg=c["accent"], fg=c["white"])
        self.refresh_run_button()
        self.theme_switch.configure(bg=c["panel"])
        self.theme_switch.set_state(self.theme == "light", c)
        self.apply_syntax_colors()
        self.lesson.apply_palette(self.colors)
        if self.popout is not None:
            self.popout.apply_palette(self.colors)
        self.update_gutter()

    def apply_syntax_colors(self) -> None:
        """Tag colours for highlighted source and the output pane."""
        for name in SYNTAX_TAGS:
            self.source.tag_configure(name, foreground=self.colors[name])
        self.output.tag_configure("err", foreground=self.colors["error"])
        self.output.tag_configure("muted", foreground=self.colors["muted"])
        self.output.tag_configure("echo", foreground=self.colors["success"])
        self.output.tag_configure("heading", foreground=self.colors["accent"], font=UI_BOLD)
        self.gutter.tag_configure("right", foreground=self.colors["muted"])

    def toggle_theme(self) -> None:
        """Switch between dark and light."""
        self.theme = "light" if self.theme == "dark" else "dark"
        self.colors = LIGHT if self.theme == "light" else DARK
        self.apply_theme()

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------

    def populate_tree(self) -> None:
        """Fill the chapter tree from the discovered scopes."""
        for scope_index, scope in enumerate(self.scopes):
            scope_id = self.tree.insert("", "end", text=scope.name, open=True)
            for chapter_index, chapter in enumerate(scope.chapters):
                iid = f"chapter-{scope_index}-{chapter_index}"
                self.chapters[iid] = chapter
                self.tree.insert(scope_id, "end", iid=iid, text=chapter.name)

    def on_chapter_selected(self, _event=None) -> None:
        """Load the chapter's steps when a chapter is clicked."""
        selection = self.tree.selection()
        if not selection or selection[0] not in self.chapters:
            return
        self.load_chapter(self.chapters[selection[0]])

    def load_chapter(self, chapter: Chapter) -> None:
        """Show a chapter's steps and select the first one."""
        self.chapter = chapter
        self.step_list.delete(0, "end")
        for step in chapter.steps:
            self.step_list.insert("end", step.title)
        if chapter.steps:
            self.step_list.selection_clear(0, "end")
            self.step_list.selection_set(0)
            self.step_list.activate(0)
            self.show_step(chapter.steps[0])

    def on_step_selected(self, _event=None) -> None:
        """Show the step chosen in the list."""
        if self.chapter is None:
            return
        selection = self.step_list.curselection()
        if selection:
            self.show_step(self.chapter.steps[selection[0]])

    def show_step(self, step: Step) -> None:
        """Load a step's source, lesson text, and title into the window."""
        self.step = step
        self.title_text.configure(text=step.title)
        self.subtitle_text.configure(text=f"{self.chapter.name}  \u00b7  {(step.code_path or step.lesson_md).name}")
        self.args_entry.delete(0, "end")

        source = discovery.NO_SOURCE_TEXT if step.code_path is None else step.code_path.read_text(encoding="utf-8")
        self.set_source(source)
        self.original_source = self.source.get("1.0", "end-1c")
        self.set_dirty(False)

        lesson_path = step.lesson_md or (self.chapter.intro_md if self.chapter else None)
        text = lesson_path.read_text(encoding="utf-8") if lesson_path else "No lesson text for this step."
        self.set_lesson_text(text)

        self.clear_output()
        self.hide_continue()
        self.run_button.configure(state="normal" if step.runnable else "disabled")
        self.refresh_run_button()

    # ------------------------------------------------------------------
    # Source editor
    # ------------------------------------------------------------------

    def set_source(self, text: str) -> None:
        """Replace the editor text without treating it as an edit."""
        self.suppress_modified = True
        self.source.delete("1.0", "end")
        self.source.insert("1.0", text)
        self.source.edit_reset()
        self.source.edit_modified(False)
        self.suppress_modified = False
        self.highlight()
        self.update_gutter()

    def on_source_modified(self, _event=None) -> None:
        """Runs when the editor's modified flag changes."""
        if not self.source.edit_modified():
            return
        self.source.edit_modified(False)
        if self.suppress_modified:
            return
        self.highlight()
        self.update_gutter()
        self.set_dirty(self.source.get("1.0", "end-1c") != self.original_source)

    def set_dirty(self, dirty: bool) -> None:
        """Show or hide the reset bar, which also carries the edited marker."""
        if dirty:
            self.reset_bar.pack(fill="x", before=self.source.master)
        else:
            self.reset_bar.pack_forget()

    def reset_source(self) -> None:
        """Discard edits and restore the step's original code."""
        if self.step is None:
            return
        self.set_source(self.original_source)
        self.set_dirty(False)

    def highlight(self) -> None:
        """Colour the source using the shared Python highlighter."""
        for tag in SYNTAX_TAGS:
            self.source.tag_remove(tag, "1.0", "end")
        code = self.source.get("1.0", "end-1c")
        for start, end, tag in python_spans(code):
            self.source.tag_add(tag, f"{start[0]}.{start[1]}", f"{end[0]}.{end[1]}")

    def update_gutter(self) -> None:
        """Line numbers beside the source, right-aligned."""
        count = int(self.source.index("end-1c").split(".")[0])
        numbers = "\n".join(str(number) for number in range(1, count + 1))
        self.gutter.configure(state="normal")
        self.gutter.delete("1.0", "end")
        self.gutter.insert("1.0", numbers, "right")
        self.gutter.configure(state="disabled")

    def scroll_source(self, *args) -> None:
        """Scrollbar command for the source editor, kept in step with the gutter."""
        self.source.yview(*args)
        self.gutter.yview(*args)

    def on_source_scrolled(self, scrollbar: ttk.Scrollbar, first: str, last: str) -> None:
        """Keep the scrollbar and the gutter in step with the source."""
        scrollbar.set(first, last)
        self.gutter.yview_moveto(first)

    def set_lesson_text(self, text: str) -> None:
        """Show the lesson Markdown in the Lesson tab and, if open, in the pop-out window."""
        self.lesson_markdown = text
        self.lesson.set_markdown(text)
        if self.popout is not None:
            self.popout.set_markdown(text, self.popout_title())

    def popout_title(self) -> str:
        """Title for the lesson window."""
        return f"Lesson - {self.chapter.name}" if self.chapter else "Lesson"

    def toggle_popout(self) -> None:
        """Pop the lesson out into its own window, or dock it back."""
        if self.popout is None:
            self.pop_out_lesson()
        else:
            self.dock_lesson()

    def pop_out_lesson(self) -> None:
        """Open the lesson beside the main window."""
        self.update_idletasks()
        width, height = 620, self.winfo_height()
        x = self.winfo_rootx() + self.winfo_width() + 8
        if x + width > self.winfo_screenwidth():
            x = max(0, self.winfo_rootx() - width - 8)
        y = self.winfo_rooty()
        self.popout = LessonWindow(self, self.colors, self.popout_title(), self.dock_lesson, self.copy_lesson)
        self.popout.geometry(f"{width}x{height}+{x}+{y}")
        self.popout.set_markdown(self.lesson_markdown, self.popout_title())
        self.lesson_body.pack_forget()
        self.placeholder.pack(fill="both", expand=True)
        self.popout_button.configure(text="Dock")

    def dock_lesson(self) -> None:
        """Close the pop-out window and show the lesson in the Lesson tab again."""
        if self.popout is None:
            return
        self.popout.destroy()
        self.popout = None
        self.placeholder.pack_forget()
        self.lesson_body.pack(fill="both", expand=True)
        self.popout_button.configure(text="Pop out")

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------

    def append(self, text: str, tag: str | None = None) -> None:
        """Add one line to the output pane and scroll to the end."""
        self.output.configure(state="normal")
        if tag:
            self.output.insert("end", text + "\n", tag)
        else:
            self.output.insert("end", text + "\n")
        self.output.configure(state="disabled")
        self.output.see("end")

    def clear_output(self) -> None:
        """Empty the output pane."""
        self.output.configure(state="normal")
        self.output.delete("1.0", "end")
        self.output.configure(state="disabled")

    def make_copy_button(self, parent: tk.Misc, command) -> tk.Button:
        """A flat Copy button on the right of a tab's toolbar."""
        button = tk.Button(parent, text="Copy", command=command, relief="flat", bd=0,
                           font=("Segoe UI", 9), padx=8, pady=1, cursor="hand2")
        button.pack(side="right")
        self.track(button, bg="panel", fg="muted", activebackground="panel")
        return button

    def copy_text(self, button: tk.Button, text: str) -> None:
        """Copy text to the clipboard and show Copied on the button briefly."""
        if not text.strip():
            return
        self.clipboard_clear()
        self.clipboard_append(text)
        button.configure(text="Copied")
        self.after(1500, lambda: button.configure(text="Copy"))

    def copy_source(self) -> None:
        """Copy the code in the Source tab."""
        self.copy_text(self.copy_source_button, self.source.get("1.0", "end-1c"))

    def copy_lesson(self) -> None:
        """Copy the raw Markdown shown in the Lesson tab."""
        self.copy_text(self.copy_lesson_button, self.lesson_markdown)

    def copy_output(self) -> None:
        """Copy the whole output pane to the clipboard."""
        self.copy_text(self.copy_button, self.output.get("1.0", "end-1c"))

    def show_continue(self) -> None:
        """Show the Continue button for a pause."""
        self.waiting_for_continue = True
        self.continue_button.pack(side="right", padx=(0, 6))

    def hide_continue(self) -> None:
        """Hide the Continue button."""
        self.waiting_for_continue = False
        self.continue_button.pack_forget()

    def continue_run(self) -> None:
        """Resume a step that is waiting at a pause."""
        if self.run is not None and self.waiting_for_continue:
            self.hide_continue()
            self.run.send("")

    def on_continue_key(self, _event=None) -> str:
        """Ctrl+Shift+Enter continues a pause."""
        self.continue_run()
        return "break"

    def on_escape(self, _event=None) -> str:
        """Cancel a running step, or reset the editor if it has edits."""
        if self.run is not None:
            self.run.cancel()
        elif self.reset_bar.winfo_ismapped():
            self.reset_source()
        return "break"

    # ------------------------------------------------------------------
    # Running
    # ------------------------------------------------------------------

    def start_run(self) -> None:
        """Run the current step with the editor's code and the args bar."""
        if self.step is None or not self.step.runnable or self.run is not None:
            return
        self.clear_output()
        try:
            args = shlex.split(self.args_entry.get())
        except ValueError as error:
            self.append(f"[Bad arguments] {error}", "err")
            return

        self.run = StepRun(self.step.code_path, self.source.get("1.0", "end-1c"), args)
        self.run.start()
        self.run_button.configure(text="Running\u2026", state="disabled")
        self.refresh_run_button()
        self.after(30, self.poll_run)

    def poll_run(self) -> None:
        """Move events from the runner thread into the window."""
        run = self.run
        if run is None:
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
                self.show_continue()
            elif kind == "input":
                self.answer_input(str(value))
            elif kind == "done":
                self.finish_run(*value)
                return
        self.after(30, self.poll_run)

    def answer_input(self, prompt: str) -> None:
        """Ask the user for a line of text and send it to the step."""
        if self.run is None:
            return
        if not prompt.strip():
            prompt = self.last_output_line()
        answer = self.ask_text(prompt or "The program is waiting for input:")
        self.append(answer, "echo")
        self.run.send(answer)

    def last_output_line(self) -> str:
        """Return the last non-blank line of output, used as an input prompt."""
        lines = self.output.get("1.0", "end-1c").splitlines()
        for line in reversed(lines):
            if line.strip():
                return line.strip()
        return ""

    def ask_text(self, prompt: str) -> str:
        """Modal dialog that collects one line of text."""
        dialog = tk.Toplevel(self)
        dialog.title("Console input")
        dialog.configure(bg=self.colors["panel"])
        dialog.transient(self)
        dialog.resizable(False, False)

        tk.Label(dialog, text=prompt, font=UI_FONT, bg=self.colors["panel"], fg=self.colors["fg"],
                 wraplength=460, justify="left", padx=16, pady=12).pack(anchor="w")
        entry = tk.Entry(dialog, font=CODE_FONT, width=48, relief="flat", bg=self.colors["bg"],
                         fg=self.colors["fg"], insertbackground=self.colors["fg"])
        entry.pack(fill="x", padx=16)
        result = {"value": ""}

        def submit(_event=None) -> None:
            result["value"] = entry.get()
            dialog.destroy()

        ok = tk.Button(dialog, text="OK", command=submit, bg=self.colors["accent"], fg="white",
                       relief="flat", bd=0, padx=16, pady=4, font=UI_BOLD)
        ok.pack(anchor="e", padx=16, pady=12)
        entry.bind("<Return>", submit)
        dialog.protocol("WM_DELETE_WINDOW", submit)
        dialog.grab_set()
        entry.focus_set()
        self.wait_window(dialog)
        return result["value"]

    def finish_run(self, returncode: int, seconds: float) -> None:
        """Report the result and restore the Run button."""
        cancelled = self.run is not None and self.run.cancelled
        self.run = None
        self.hide_continue()
        self.run_button.configure(text="\u25B6  Run", state="normal")
        self.refresh_run_button()
        if cancelled:
            self.append("[Run cancelled]", "err")
        elif returncode != 0:
            self.append("", None)
            self.append("\u2500\u2500 Errors " + "\u2500" * 40, "err")
        self.append("")
        self.append(f"\u2500\u2500 Finished in {seconds * 1000:.0f} ms \u2500\u2500", "muted")


def main() -> None:
    """Start the lesson runner."""
    App().mainloop()


if __name__ == "__main__":
    main()
