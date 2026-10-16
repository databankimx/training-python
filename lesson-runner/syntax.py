"""Source coloring for the source editor and lesson code blocks.

Python uses the tokenize module. C uses a small set of patterns, which covers the
C samples in the lessons: comments, strings, preprocessor lines, numbers,
keywords and function calls.

The tags follow Visual Studio's default colours (Dark+ and Light+). The palette
for each theme is defined in app.py under the same keys as the tags below.
"""

from __future__ import annotations

import bisect
import builtins
import io
import keyword
import re
import tokenize

# Tags the highlighter can produce. Each must be configured with a colour.
SYNTAX_TAGS = ("kw", "ctl", "str", "com", "num", "typ", "fn", "var")

# Keywords shown in the control-flow colour, as in Visual Studio.
CONTROL = {
    "if", "elif", "else", "for", "while", "break", "continue", "return", "yield",
    "try", "except", "finally", "raise", "with", "pass", "import", "from", "as",
    "in", "is", "not", "and", "or", "lambda", "async", "await", "match", "case",
    "assert", "del", "global", "nonlocal",
}

BUILTIN_NAMES = set(dir(builtins))
BUILTIN_TYPES = {name for name in BUILTIN_NAMES if isinstance(getattr(builtins, name), type)}

C_CONTROL = {
    "if", "else", "for", "while", "do", "switch", "case", "default", "break",
    "continue", "return", "goto",
}
C_KEYWORDS = {
    "int", "char", "float", "double", "void", "long", "short", "unsigned", "signed",
    "const", "static", "extern", "struct", "union", "enum", "typedef", "sizeof",
    "auto", "register", "volatile", "inline", "bool", "true", "false", "NULL",
}

C_TOKEN = re.compile(
    r'(?P<com>//[^\n]*|/\*.*?\*/)'
    r'|(?P<str>"(?:\\.|[^"\\\n])*"|\'(?:\\.|[^\'\\\n])*\')'
    r'|(?P<dir>^[ \t]*#[^\n]*)'
    r'|(?P<num>\b(?:0[xX][0-9a-fA-F]+|\d+(?:\.\d*)?(?:[eE][+-]?\d+)?)[uUlLfF]*\b)'
    r'|(?P<name>\b[A-Za-z_]\w*\b)',
    re.MULTILINE | re.DOTALL,
)


def python_spans(code: str) -> list[tuple[tuple[int, int], tuple[int, int], str]]:
    """Return (start, end, tag) spans for Python code. Rows are 1-based, columns 0-based."""
    spans = []
    previous = ""
    try:
        for token in tokenize.generate_tokens(io.StringIO(code).readline):
            tag = None
            if token.type == tokenize.COMMENT:
                tag = "com"
            elif token.type == tokenize.STRING:
                tag = "str"
            elif token.type == tokenize.NUMBER:
                tag = "num"
            elif token.type == tokenize.NAME:
                name = token.string
                if previous == "def":
                    tag = "fn"
                elif previous == "class":
                    tag = "typ"
                elif keyword.iskeyword(name):
                    tag = "ctl" if name in CONTROL else "kw"
                elif name == "self":
                    tag = "var"
                elif name in BUILTIN_TYPES:
                    tag = "typ"
                elif name in BUILTIN_NAMES:
                    tag = "fn"
            previous = token.string if token.type == tokenize.NAME else ""
            if tag:
                spans.append((token.start, token.end, tag))
    except (tokenize.TokenError, SyntaxError):
        pass
    return spans


def c_spans(code: str) -> list[tuple[tuple[int, int], tuple[int, int], str]]:
    """Return (start, end, tag) spans for C code. Rows are 1-based, columns 0-based."""
    line_starts = [0] + [match.end() for match in re.finditer(r"\n", code)]

    def row_col(offset: int) -> tuple[int, int]:
        row = bisect.bisect_right(line_starts, offset)
        return row, offset - line_starts[row - 1]

    spans = []
    for match in C_TOKEN.finditer(code):
        kind = match.lastgroup
        text = match.group(0)
        if kind == "name":
            if text in C_CONTROL:
                tag = "ctl"
            elif text in C_KEYWORDS:
                tag = "kw"
            elif code[match.end():].lstrip(" \t").startswith("("):
                tag = "fn"
            else:
                continue
        elif kind == "com":
            tag = "com"
        elif kind == "str":
            tag = "str"
        elif kind == "dir":
            tag = "ctl"
        else:
            tag = "num"
        spans.append((row_col(match.start()), row_col(match.end()), tag))
    return spans
