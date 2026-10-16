"""Render lesson Markdown into a tkinter Text widget, and the pop-out lesson window.

Covers the Markdown the training lessons use: headings, paragraphs, bullet and
numbered lists, block quotes, horizontal rules, fenced code, simple pipe tables,
inline code, bold, italic, links and image placeholders. Web links open in the
default browser. Relative links (for example to another lesson) show as text.
"""

from __future__ import annotations

import re
import tkinter as tk
import webbrowser

CODE_FONT = ("Consolas", 11)
BODY_FONT = ("Segoe UI", 10)

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
RULE = re.compile(r"^([-*_])(\s*\1){2,}\s*$")
BLOCK_QUOTE = re.compile(r"^\s*>\s?(.*)$")
BULLET = re.compile(r"^(\s*)[-*+]\s+(.*)$")
NUMBERED = re.compile(r"^(\s*)(\d+)[.)]\s+(.*)$")
TABLE_SEPARATOR = re.compile(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?$")
INLINE = re.compile(r"(`[^`]+`)|(\*\*.+?\*\*)|(__.+?__)|(\*[^*\s][^*]*?\*)|(!?\[[^\]]*\]\([^)]*\))")
BLOCK_START = re.compile(r"^(#{1,6}\s|```|~~~|>|\s*[-*+]\s|\s*\d+[.)]\s|\|)")


def configure_tags(widget: tk.Text, colors: dict) -> None:
    """Set every tag's look from the palette."""
    widget.configure(background=colors["bg"], foreground=colors["fg"], font=BODY_FONT)
    widget.tag_configure("h1", font=("Segoe UI", 20, "bold"), foreground=colors["heading"],
                         spacing1=12, spacing3=8)
    widget.tag_configure("h2", font=("Segoe UI", 16, "bold"), foreground=colors["heading"],
                         spacing1=10, spacing3=6)
    widget.tag_configure("h3", font=("Segoe UI", 13, "bold"), foreground=colors["heading"],
                         spacing1=8, spacing3=4)
    widget.tag_configure("p", spacing3=6)
    widget.tag_configure("bold", font=("Segoe UI", 10, "bold"))
    widget.tag_configure("italic", font=("Segoe UI", 10, "italic"))
    widget.tag_configure("inline_code", font=("Consolas", 10), background=colors["code_bg"],
                         foreground=colors["code_fg"])
    widget.tag_configure("code_block", font=CODE_FONT, background=colors["code_bg"],
                         foreground=colors["code_fg"], lmargin1=12, lmargin2=12, rmargin=12)
    widget.tag_configure("table", font=CODE_FONT, background=colors["code_bg"],
                         foreground=colors["fg"], lmargin1=12, lmargin2=12)
    widget.tag_configure("quote", foreground=colors["muted"], font=("Segoe UI", 10, "italic"),
                         lmargin1=16, lmargin2=16)
    widget.tag_configure("bullet", lmargin1=24, lmargin2=40, spacing3=2)
    widget.tag_configure("rule", foreground=colors["rule"])
    widget.tag_configure("muted", foreground=colors["muted"], font=("Segoe UI", 10, "italic"))
    widget.tag_configure("link", foreground=colors["accent"], underline=True)


class MarkdownText(tk.Text):
    """A read-only Text widget that shows rendered lesson Markdown."""

    def __init__(self, master: tk.Misc, colors: dict, **options) -> None:
        super().__init__(master, wrap="word", bd=0, padx=16, pady=12, highlightthickness=0,
                         state="disabled", cursor="arrow", **options)
        self.colors = colors
        self.markdown = ""
        self.link_count = 0
        configure_tags(self, colors)

    def set_markdown(self, text: str) -> None:
        """Replace the displayed lesson."""
        self.markdown = text
        self.render()

    def apply_palette(self, colors: dict) -> None:
        """Switch colours for a new theme and render again."""
        self.colors = colors
        configure_tags(self, colors)
        self.render()

    def render(self) -> None:
        """Rebuild the document from the stored Markdown."""
        self.configure(state="normal")
        self.delete("1.0", "end")
        render_markdown(self, self.markdown)
        self.configure(state="disabled")

    def insert_inline(self, text: str, base_tags: tuple[str, ...] = ()) -> None:
        """Insert text with bold, italic, code, links and image placeholders."""
        position = 0
        for match in INLINE.finditer(text):
            if match.start() > position:
                self.insert("end", text[position:match.start()], base_tags)
            token = match.group(0)
            if match.group(1):
                self.insert("end", token[1:-1], base_tags + ("inline_code",))
            elif match.group(2) or match.group(3):
                self.insert("end", token[2:-2], base_tags + ("bold",))
            elif match.group(4):
                self.insert("end", token[1:-1], base_tags + ("italic",))
            elif token.startswith("!"):
                alt = token[2:token.index("]")]
                self.insert("end", f"[Image: {alt or 'untitled'}]", base_tags + ("muted",))
            else:
                label = token[1:token.index("]")]
                url = token[token.index("](") + 2:-1]
                self.insert_link(label, url, base_tags)
            position = match.end()
        if position < len(text):
            self.insert("end", text[position:], base_tags)

    def insert_link(self, label: str, url: str, base_tags: tuple[str, ...]) -> None:
        """A link; web addresses open in the browser, other links are shown as text."""
        if url.lower().startswith(("http://", "https://")):
            self.link_count += 1
            tag = f"link{self.link_count}"
            self.tag_configure(tag, foreground=self.colors["accent"], underline=True)
            self.tag_bind(tag, "<Button-1>", lambda _event, target=url: webbrowser.open(target))
            self.tag_bind(tag, "<Enter>", lambda _event: self.configure(cursor="hand2"))
            self.tag_bind(tag, "<Leave>", lambda _event: self.configure(cursor="arrow"))
            self.insert("end", label, base_tags + ("link", tag))
        else:
            self.insert("end", label, base_tags + ("link",))


def render_markdown(widget: MarkdownText, text: str) -> None:
    """Walk the Markdown line by line and insert formatted blocks."""
    lines = text.replace("\r\n", "\n").split("\n")
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if not stripped:
            index += 1
            continue

        if stripped.startswith(("```", "~~~")):
            fence = stripped[:3]
            index += 1
            code_lines = []
            while index < len(lines) and not lines[index].strip().startswith(fence):
                code_lines.append(lines[index])
                index += 1
            index += 1  # skip the closing fence
            for code_line in code_lines:
                widget.insert("end", code_line + "\n", ("code_block",))
            widget.insert("end", "\n")
            continue

        heading = HEADING.match(stripped)
        if heading:
            level = min(len(heading.group(1)), 3)
            widget.insert_inline(heading.group(2), (f"h{level}",))
            widget.insert("end", "\n")
            index += 1
            continue

        if RULE.match(stripped):
            widget.insert("end", "\u2500" * 60 + "\n", ("rule",))
            index += 1
            continue

        if stripped.startswith("|") and index + 1 < len(lines) \
                and TABLE_SEPARATOR.match(lines[index + 1].strip()):
            rows = []
            while index < len(lines) and lines[index].strip().startswith("|"):
                if not TABLE_SEPARATOR.match(lines[index].strip()):
                    rows.append([cell.strip() for cell in lines[index].strip().strip("|").split("|")])
                index += 1
            insert_table(widget, rows)
            continue

        if BLOCK_QUOTE.match(line):
            quote_lines = []
            while index < len(lines) and BLOCK_QUOTE.match(lines[index]):
                quote_lines.append(BLOCK_QUOTE.match(lines[index]).group(1))
                index += 1
            widget.insert_inline(" ".join(part for part in quote_lines if part.strip()), ("quote",))
            widget.insert("end", "\n")
            continue

        bullet = BULLET.match(line)
        if bullet:
            widget.insert("end", "\u2022  ", ("bullet",))
            widget.insert_inline(bullet.group(2), ("bullet",))
            widget.insert("end", "\n", ("bullet",))
            index += 1
            continue

        numbered = NUMBERED.match(line)
        if numbered:
            widget.insert("end", f"{numbered.group(2)}.  ", ("bullet",))
            widget.insert_inline(numbered.group(3), ("bullet",))
            widget.insert("end", "\n", ("bullet",))
            index += 1
            continue

        paragraph = []
        while index < len(lines) and lines[index].strip() and not BLOCK_START.match(lines[index]) \
                and not RULE.match(lines[index].strip()):
            paragraph.append(lines[index].strip())
            index += 1
        if not paragraph:
            paragraph.append(stripped)
            index += 1
        widget.insert_inline(" ".join(paragraph), ("p",))
        widget.insert("end", "\n")


def insert_table(widget: MarkdownText, rows: list[list[str]]) -> None:
    """Show a Markdown table as aligned monospaced text."""
    if not rows:
        return
    columns = max(len(row) for row in rows)
    padded = [row + [""] * (columns - len(row)) for row in rows]
    widths = [max(len(row[column]) for row in padded) for column in range(columns)]
    for row in padded:
        cells = [row[column].ljust(widths[column]) for column in range(columns)]
        widget.insert("end", "  ".join(cells).rstrip() + "\n", ("table",))
    widget.insert("end", "\n")


class LessonWindow(tk.Toplevel):
    """A separate window that shows the lesson beside the main window."""

    def __init__(self, master: tk.Misc, colors: dict, title: str, on_dock, on_copy) -> None:
        super().__init__(master)
        self.title(title)
        self.geometry("620x760")
        self.minsize(360, 300)
        self.configure(bg=colors["panel"])
        self.on_dock = on_dock
        self.protocol("WM_DELETE_WINDOW", self.dock)

        toolbar = tk.Frame(self, padx=8, pady=4, bg=colors["panel"])
        toolbar.pack(fill="x")
        self.dock_button = tk.Button(toolbar, text="Dock", command=self.dock, relief="flat", bd=0,
                                     font=("Segoe UI", 9), padx=8, pady=1, cursor="hand2",
                                     bg=colors["panel"], fg=colors["muted"],
                                     activebackground=colors["panel"])
        self.dock_button.pack(side="right")
        self.copy_button = tk.Button(toolbar, text="Copy", command=on_copy, relief="flat", bd=0,
                                     font=("Segoe UI", 9), padx=8, pady=1, cursor="hand2",
                                     bg=colors["panel"], fg=colors["muted"],
                                     activebackground=colors["panel"])
        self.copy_button.pack(side="right")

        self.view = MarkdownText(self, colors)
        scroll = tk.Scrollbar(self, orient="vertical", command=self.view.yview)
        self.view.configure(yscrollcommand=scroll.set)
        scroll.pack(side="right", fill="y")
        self.view.pack(fill="both", expand=True)

    def set_markdown(self, text: str, title: str) -> None:
        """Show a new lesson."""
        self.title(title)
        self.view.set_markdown(text)

    def apply_palette(self, colors: dict) -> None:
        """Repaint for a new theme."""
        self.configure(bg=colors["panel"])
        self.view.apply_palette(colors)
        for button in (self.dock_button, self.copy_button):
            button.configure(bg=colors["panel"], fg=colors["muted"], activebackground=colors["panel"])

    def dock(self) -> None:
        """Close this window and show the lesson in the main window again."""
        self.on_dock()
