"""Render lesson Markdown into a tkinter Text widget, and the pop-out lesson window.

Covers the Markdown the training lessons use: headings, paragraphs, bullet and
numbered lists, block quotes, horizontal rules, fenced code, simple pipe tables,
inline code, bold, italic, links and image placeholders. Fenced code blocks
tagged python or py are highlighted, and each code block is drawn as a rounded
panel. Maths in $...$ is rendered as an image with matplotlib's mathtext engine.
If mathtext can't draw an expression, it is shown as Unicode text instead.
Web links open in the default browser. Relative links show as text.
"""

from __future__ import annotations

import base64
import io
import re
import tkinter as tk
import tkinter.font as tkfont
import webbrowser

from syntax import SYNTAX_TAGS, python_spans

try:
    import matplotlib.image as mpl_image
    from matplotlib.mathtext import MathTextParser
    MATHTEXT_AVAILABLE = True
except Exception:  # matplotlib not installed: maths falls back to Unicode text
    MATHTEXT_AVAILABLE = False

BODY_FONT = ("Segoe UI", 10)
CODE_FAMILY = "Consolas"
CODE_SIZE = 11
MATH_SIZE = 10.5
MATH_DPI = 110

HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
RULE = re.compile(r"^([-*_])(\s*\1){2,}\s*$")
BLOCK_QUOTE = re.compile(r"^\s*>\s?(.*)$")
BULLET = re.compile(r"^(\s*)[-*+]\s+(.*)$")
NUMBERED = re.compile(r"^(\s*)(\d+)[.)]\s+(.*)$")
TABLE_SEPARATOR = re.compile(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?$")
# One pattern for all inline markup, so bold and italic can contain maths and code.
INLINE = re.compile(
    r"(\$[^$\n]{1,80}\$)"          # maths
    r"|(`[^`]+`)"                  # inline code
    r"|(\*\*.+?\*\*)"              # bold
    r"|(__.+?__)"                  # bold
    r"|(\*[^*\s][^*]*?\*)"         # italic
    r"|(!?\[[^\]]*\]\([^)]*\))"    # link or image
)
BLOCK_START = re.compile(r"^(#{1,6}\s|```|~~~|>|\s*[-*+]\s|\s*\d+[.)]\s|\|)")

MATH = re.compile(r"\$([^$\n]{1,80})\$")
SUPERSCRIPT = str.maketrans("0123456789+-=()n", "\u2070\u00b9\u00b2\u00b3\u2074\u2075\u2076\u2077\u2078\u2079\u207a\u207b\u207c\u207d\u207e\u207f")
SUBSCRIPT = str.maketrans("0123456789+-=()", "\u2080\u2081\u2082\u2083\u2084\u2085\u2086\u2087\u2088\u2089\u208a\u208b\u208c\u208d\u208e")
LATEX_SYMBOLS = {
    "\\times": "\u00d7", "\\cdot": "\u00b7", "\\div": "\u00f7", "\\pm": "\u00b1",
    "\\neq": "\u2260", "\\leq": "\u2264", "\\le": "\u2264", "\\geq": "\u2265", "\\ge": "\u2265",
    "\\approx": "\u2248", "\\cdots": "\u22ef", "\\ldots": "\u2026", "\\to": "\u2192",
    "\\rightarrow": "\u2192", "\\infty": "\u221e", "\\pi": "\u03c0", "\\,": " ", "\\;": " ", "\\ ": " ",
}

CODE_MARGIN = 10     # space between the rounded panel and the lesson text
CODE_PADDING_X = 20  # space between the panel edge and the code
CODE_PADDING_Y = 16  # space between the panel edge and the code
CODE_RADIUS = 8
CODE_MAX_COLUMNS = 110

_MATH_CACHE: dict[tuple[str, str, float], tk.PhotoImage | None] = {}


def latex_to_text(expression: str) -> str:
    """Unicode fallback for a LaTeX expression, used when mathtext can't draw it."""
    text = re.sub(r"\\frac\{([^{}]*)\}\{([^{}]*)\}", r"(\1)/(\2)", expression)
    text = re.sub(r"\\sqrt\{([^{}]*)\}", lambda m: "\u221a(" + m.group(1) + ")", text)
    text = re.sub(r"\\(text|mathrm)\{([^{}]*)\}", r"\2", text)
    text = re.sub(r"\\underline\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\underline", "", text)
    text = re.sub(r"\\mkern-?[0-9.]+mu", "", text)
    for key in sorted(LATEX_SYMBOLS, key=len, reverse=True):
        text = text.replace(key, LATEX_SYMBOLS[key])
    text = re.sub(r"\^\{([^{}]*)\}", lambda m: m.group(1).translate(SUPERSCRIPT), text)
    text = re.sub(r"\^(\w)", lambda m: m.group(1).translate(SUPERSCRIPT), text)
    text = re.sub(r"_\{([^{}]*)\}", lambda m: m.group(1).translate(SUBSCRIPT), text)
    text = re.sub(r"_(\w)", lambda m: m.group(1).translate(SUBSCRIPT), text)
    return text.replace("{", "").replace("}", "")


def render_math(text: str) -> str:
    """Replace every $...$ span with its Unicode fallback text (used for table widths)."""
    return MATH.sub(lambda match: latex_to_text(match.group(1)), text)


def strip_markup(text: str) -> str:
    """Plain text of a cell, without bold, italic and code markers."""
    return re.sub(r"\*\*|\*|`", "", text)


def plain_width(text: str) -> int:
    """Approximate displayed width of a table cell."""
    return len(strip_markup(render_math(text)))


_MATHTEXT_PARSER = None


def mathtext_parser() -> MathTextParser:
    """One shared mathtext parser, created on first use."""
    global _MATHTEXT_PARSER
    if _MATHTEXT_PARSER is None:
        _MATHTEXT_PARSER = MathTextParser("agg")
    return _MATHTEXT_PARSER


def math_photo(widget: tk.Misc, expression: str, colour: str, size: float) -> tk.PhotoImage | None:
    """Render a LaTeX expression to an image with mathtext, or None if that fails."""
    key = (expression, colour, size)
    if key not in _MATH_CACHE:
        photo = None
        if MATHTEXT_AVAILABLE:
            try:
                rgba, _depth = mathtext_parser().to_rgba(f"${expression}$", color=colour,
                                                         dpi=MATH_DPI, fontsize=size)
                buffer = io.BytesIO()
                mpl_image.imsave(buffer, rgba, format="png")
                encoded = base64.b64encode(buffer.getvalue()).decode("ascii")
                photo = tk.PhotoImage(master=widget, data=encoded, format="png")
            except Exception:
                photo = None
        _MATH_CACHE[key] = photo
    return _MATH_CACHE[key]


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
    widget.tag_configure("inline_code", font=(CODE_FAMILY, 10), foreground=colors["fn"])
    widget.tag_configure("table", font=(CODE_FAMILY, CODE_SIZE), background=colors["code_bg"],
                         foreground=colors["code_fg"], lmargin1=12, lmargin2=12)
    widget.tag_configure("quote", foreground=colors["muted"], font=("Segoe UI", 10, "italic"),
                         lmargin1=16, lmargin2=16)
    widget.tag_configure("bullet", lmargin1=24, lmargin2=40, spacing3=2)
    widget.tag_configure("rule", foreground=colors["rule"])
    widget.tag_configure("muted", foreground=colors["muted"], font=("Segoe UI", 10, "italic"))
    widget.tag_configure("link", foreground=colors["accent"], underline=True)
    for tag in SYNTAX_TAGS:
        widget.tag_configure(tag, foreground=colors[tag])


def round_rect(canvas: tk.Canvas, x1: float, y1: float, x2: float, y2: float,
               radius: float, fill: str) -> None:
    """A filled rectangle with rounded corners, drawn from rectangles and arcs."""
    radius = min(radius, (x2 - x1) / 2, (y2 - y1) / 2)
    canvas.create_rectangle(x1 + radius, y1, x2 - radius, y2, fill=fill, outline=fill)
    canvas.create_rectangle(x1, y1 + radius, x2, y2 - radius, fill=fill, outline=fill)
    corners = (
        (x1 + radius, y1 + radius, 90),   # top left
        (x2 - radius, y1 + radius, 0),    # top right
        (x2 - radius, y2 - radius, 270),  # bottom right
        (x1 + radius, y2 - radius, 180),  # bottom left
    )
    for centre_x, centre_y, start in corners:
        canvas.create_arc(centre_x - radius, centre_y - radius, centre_x + radius, centre_y + radius,
                          start=start, extent=90, fill=fill, outline=fill)


class MarkdownText(tk.Text):
    """A read-only Text widget that shows rendered lesson Markdown."""

    def __init__(self, master: tk.Misc, colors: dict, **options) -> None:
        super().__init__(master, wrap="word", bd=0, padx=16, pady=12, highlightthickness=0,
                         state="disabled", cursor="arrow", **options)
        self.colors = colors
        self.markdown = ""
        self.link_count = 0
        self.math_as_text = False  # set while drawing table cells, so columns stay aligned
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
        """Insert text with maths, bold, italic, code, links and image placeholders.

        Bold and italic recurse, so a formula or code span inside them keeps its formatting.
        """
        position = 0
        for match in INLINE.finditer(text):
            if match.start() > position:
                self.insert("end", text[position:match.start()], base_tags)
            token = match.group(0)
            if match.group(1):
                self.insert_math(token[1:-1], base_tags)
            elif match.group(2):
                self.insert("end", token[1:-1], base_tags + ("inline_code",))
            elif match.group(3) or match.group(4):
                self.insert_inline(token[2:-2], base_tags + ("bold",))
            elif match.group(5):
                self.insert_inline(token[1:-1], base_tags + ("italic",))
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

    def insert_math(self, expression: str, base_tags: tuple[str, ...]) -> None:
        """A formula as a rendered image, or as Unicode text when the image can't be made."""
        photo = None if self.math_as_text else math_photo(self, expression, self.colors["fg"], MATH_SIZE)
        if photo is None:
            self.insert("end", latex_to_text(expression), base_tags)
        else:
            self.image_create("end", image=photo, align="baseline")

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


def insert_code_block(widget: MarkdownText, code_lines: list[str], language: str) -> None:
    """A code block drawn as a rounded panel with a margin around it.

    The code sits in a read-only Text inside the panel, so it can be selected
    and copied. Python blocks are highlighted.
    """
    colors = widget.colors
    font = tkfont.Font(family=CODE_FAMILY, size=CODE_SIZE)
    char_width = font.measure("0")
    line_height = font.metrics("linespace")

    longest = max((len(line) for line in code_lines), default=0)
    columns = max(20, min(longest, CODE_MAX_COLUMNS))
    rows = sum(max(1, -(-len(line) // columns)) for line in (code_lines or [""]))

    box_width = columns * char_width + 2 * CODE_PADDING_X
    box_height = rows * line_height + 2 * CODE_PADDING_Y
    canvas = tk.Canvas(widget, width=box_width + 2 * CODE_MARGIN, height=box_height + 2 * CODE_MARGIN,
                       bd=0, highlightthickness=0, bg=colors["bg"])
    round_rect(canvas, CODE_MARGIN, CODE_MARGIN, CODE_MARGIN + box_width, CODE_MARGIN + box_height,
               CODE_RADIUS, colors["code_bg"])

    inset = min(round(CODE_RADIUS * 0.7), CODE_PADDING_X, CODE_PADDING_Y)  # keeps the code clear of the rounded corners
    code = tk.Text(canvas, width=columns, height=rows, wrap="char", font=font, bd=0,
                   padx=CODE_PADDING_X - inset, pady=CODE_PADDING_Y - inset, highlightthickness=0,
                   background=colors["code_bg"], foreground=colors["code_fg"], cursor="xterm")
    code.insert("1.0", "\n".join(code_lines))
    if language in ("python", "py"):
        for start, end, tag in python_spans("\n".join(code_lines)):
            code.tag_add(tag, f"{start[0]}.{start[1]}", f"{end[0]}.{end[1]}")
        for tag in SYNTAX_TAGS:
            code.tag_configure(tag, foreground=colors[tag])
    code.configure(state="disabled")

    # The panel is fixed size, so mouse-wheel events go to the lesson, not the code box.
    code.bind("<MouseWheel>", lambda event: (widget.yview_scroll(int(-event.delta / 120), "units"), "break")[1])

    canvas.create_window(CODE_MARGIN + inset, CODE_MARGIN + inset, window=code, anchor="nw",
                         width=box_width - 2 * inset, height=box_height - 2 * inset)
    canvas.bind("<MouseWheel>", lambda event: (widget.yview_scroll(int(-event.delta / 120), "units"), "break")[1])
    widget.window_create("end", window=canvas)
    widget.insert("end", "\n")


def strip_html(text: str) -> str:
    """Remove the HTML the lessons use for layout, so it doesn't show as text."""
    text = re.sub(r"<(style|script)\b.*?</\1\s*>", "", text, flags=re.IGNORECASE | re.DOTALL)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.IGNORECASE)
    text = re.sub(r"<img\b[^>]*>", "[Image]", text, flags=re.IGNORECASE)
    return text


def render_markdown(widget: MarkdownText, text: str) -> None:
    """Walk the Markdown line by line and insert formatted blocks."""
    lines = strip_html(text).replace("\r\n", "\n").split("\n")
    index = 0
    while index < len(lines):
        line = lines[index]
        stripped = line.strip()

        if not stripped:
            index += 1
            continue

        if stripped.startswith(("```", "~~~")):
            fence = stripped[:3]
            info = stripped[3:].strip()
            language = info.split()[0].lower() if info else ""
            index += 1
            code_lines = []
            while index < len(lines) and not lines[index].strip().startswith(fence):
                code_lines.append(lines[index])
                index += 1
            index += 1  # skip the closing fence
            insert_code_block(widget, code_lines, language)
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
                    cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
                    if any(cells):
                        rows.append(cells)
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
    """Show a Markdown table as aligned monospaced text, with inline formatting in cells."""
    if not rows:
        return
    columns = max(len(row) for row in rows)
    padded = [row + [""] * (columns - len(row)) for row in rows]
    widths = [max(plain_width(row[column]) for row in padded) for column in range(columns)]
    widget.math_as_text = True
    for row in padded:
        for column in range(columns):
            cell = row[column]
            widget.insert_inline(cell, ("table",))
            if column < columns - 1:
                gap = widths[column] - plain_width(cell) + 2
                widget.insert("end", " " * gap, ("table",))
        widget.insert("end", "\n", ("table",))
    widget.math_as_text = False
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
