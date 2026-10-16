"""Python token colouring, shared by the source editor and lesson code blocks.

The tags follow Visual Studio's default colours (Dark+ and Light+). The palette
for each theme is defined in app.py under the same keys as the tags below.
"""

from __future__ import annotations

import builtins
import io
import keyword
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
