"""Render a lesson's Markdown to a complete HTML page for Qt WebEngine.

Markdown is parsed with markdown-it-py (CommonMark plus tables, and raw HTML
passed through, so the lesson's own <style> block applies). $...$ and $$...$$
maths is left for MathJax to typeset in the page. Code blocks are highlighted
by Prism, and the token colours follow the Visual Studio palette.

MathJax and Prism are loaded from the app's vendor folder, so the app works
offline once that folder is in place.
"""

from __future__ import annotations

import html
import re
from pathlib import Path

from markdown_it import MarkdownIt
from mdit_py_plugins.dollarmath import dollarmath_plugin

#pylint: disable=unused-argument, line-too-long

CSS = """
body { background: #1E1E1E; color: #D4D4D4; font-family: "Segoe UI", sans-serif;
       font-size: 15px; line-height: 1.5; margin: 0; padding: 16px 24px; }
h1, h2, h3 { color: #569CD6; }
h1 { font-size: 26px; } h2 { font-size: 21px; } h3 { font-size: 17px; }
p { margin: 8px 0; }
code { font-family: Consolas, monospace; font-size: 13px; color: #D7BA7D; }
h1 code, h2 code, h3 code { font-size: inherit; }
pre { background: #0A0A0A; border-radius: 8px; padding: 14px 18px; margin: 12px 10px;
      overflow-x: auto; }
pre code { color: #D4D4D4; background: none; font-size: 14px; }
table { border-collapse: collapse; margin: 12px 0; }
th, td { padding: 4px 10px; border: 1px solid #3F3F46; }
a { color: #3794FF; }
blockquote { color: #858585; border-left: 3px solid #3F3F46; margin: 8px 0;
             padding-left: 12px; }
hr { border: 0; border-top: 1px solid #3F3F46; }

/* Prism tokens, Visual Studio Dark+ colours. */
.token.comment, .token.prolog, .token.doctype, .token.cdata { color: #6A9955; }
.token.string, .token.char, .token.attr-value { color: #CE9178; }
.token.number, .token.boolean { color: #B5CEA8; }
.token.keyword { color: #569CD6; }
.token.ctl { color: #C586C0; }
.token.directive { color: #C586C0; }
.token.directive .token.string { color: #CE9178; }
.token.directive .token.keyword { color: #C586C0; }
.token.function { color: #DCDCAA; }
.token.class-name, .token.builtin { color: #4EC9B0; }
.token.variable, .token.property, .token.constant { color: #9CDCFE; }
.token.operator, .token.punctuation { color: #D4D4D4; }
"""

LIGHT_CSS = """
body { background: #FFFFFF; color: #1E1E1E; font-family: "Segoe UI", sans-serif;
       font-size: 15px; line-height: 1.5; margin: 0; padding: 16px 24px; }
h1, h2, h3 { color: #0451A5; }
h1 { font-size: 26px; } h2 { font-size: 21px; } h3 { font-size: 17px; }
p { margin: 8px 0; }
code { font-family: Consolas, monospace; font-size: 13px; color: #795E26; }
h1 code, h2 code, h3 code { font-size: inherit; }
pre { background: #F5F5F5; border-radius: 8px; padding: 14px 18px; margin: 12px 10px;
      overflow-x: auto; }
pre code { color: #1E1E1E; background: none; font-size: 14px; }
table { border-collapse: collapse; margin: 12px 0; }
th, td { padding: 4px 10px; border: 1px solid #CCCEDB; }
a { color: #0451A5; }
blockquote { color: #717171; border-left: 3px solid #CCCEDB; margin: 8px 0;
             padding-left: 12px; }
hr { border: 0; border-top: 1px solid #CCCEDB; }

/* Prism tokens, Visual Studio Light+ colours. */
.token.comment, .token.prolog, .token.doctype, .token.cdata { color: #008000; }
.token.string, .token.char, .token.attr-value { color: #A31515; }
.token.number, .token.boolean { color: #098658; }
.token.keyword { color: #0000FF; }
.token.ctl { color: #AF00DB; }
.token.directive { color: #AF00DB; }
.token.directive .token.string { color: #A31515; }
.token.directive .token.keyword { color: #AF00DB; }
.token.function { color: #795E26; }
.token.class-name, .token.builtin { color: #267F99; }
.token.variable, .token.property, .token.constant { color: #001080; }
.token.operator, .token.punctuation { color: #1E1E1E; }
"""

HEAD = """<!doctype html>
<html><head><meta charset="utf-8">
<style>__CSS__</style>
<script>
window.MathJax = {
  tex: { macros: { Larr: '\\\\leftarrow', Rarr: '\\\\rightarrow', Z: '\\\\mathbb{Z}', N: '\\\\mathbb{N}', R: '\\\\mathbb{R}', Q: '\\\\mathbb{Q}' }, inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
         displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']],
         processEscapes: true },
  svg: { fontCache: 'global' }
};
</script>
<script src="VENDOR_URL/node_modules/mathjax/es5/tex-svg.js" async></script>
<script src="VENDOR_URL/node_modules/prismjs/prism.js"></script>
<script src="VENDOR_URL/node_modules/prismjs/components/prism-python.min.js"></script>
<script src="VENDOR_URL/node_modules/prismjs/components/prism-clike.min.js"></script>
<script src="VENDOR_URL/node_modules/prismjs/components/prism-c.min.js"></script>
</head><body>
"""

TAIL = """
<script>
if (window.Prism) {
  // Control-flow keywords get their own colour, as in Visual Studio.
  var CONTROL = new Set(['if', 'else', 'for', 'while', 'do', 'return', 'break', 'continue',
    'switch', 'case', 'default', 'goto', 'elif', 'try', 'except', 'finally', 'raise', 'with',
    'pass', 'import', 'from', 'as', 'in', 'is', 'not', 'and', 'or', 'lambda', 'async', 'await',
    'yield', 'match', 'assert', 'del', 'global', 'nonlocal']);
  Prism.hooks.add('wrap', function (env) {
    if (env.type === 'keyword' && CONTROL.has(env.content)) { env.classes.push('ctl'); }
  });
  Prism.highlightAll();
}
</script>
</body></html>
"""


def make_parser() -> MarkdownIt:
    """CommonMark with tables, raw HTML and $...$ maths.

    The maths plugin wraps formulas in span tags without delimiters, so MathJax
    can't find them. These render rules write \\(...\\) and \\[...\\] instead,
    which MathJax is configured to typeset.
    """
    md = (MarkdownIt("commonmark", {"html": True, "linkify": False})
          .enable("table")
          .use(dollarmath_plugin))

    def inline_math(renderer, tokens, idx, options, env):
        return "\\(" + html.escape(tokens[idx].content) + "\\)"

    def block_math(renderer, tokens, idx, options, env):
        return "\\[" + html.escape(tokens[idx].content) + "\\]\n"

    md.add_render_rule("math_inline", inline_math)
    md.add_render_rule("math_block", block_math)
    return md


_PARSER = make_parser()

# A table header row whose cells are all empty. The lessons use these as spacers.
EMPTY_HEADER = re.compile(r"<thead>\s*<tr>(?:\s*<th[^>]*></th>)+\s*</tr>\s*</thead>")


MATH_SPAN = re.compile(r"\$\$[^$]+\$\$|\$[^$\n]+\$")


def math_symbols(markdown_text: str) -> str:
    """Swap symbols that LaTeX doesn't define for their maths equivalents, inside maths only.

    \\^ is the XOR operator in these lessons, shown as \\oplus. Code blocks are left alone.
    """
    return MATH_SPAN.sub(lambda m: m.group(0).replace("\\^", "\\oplus"), markdown_text)


def render_lesson(markdown_text: str, vendor_dir: Path, dark: bool = True) -> str:
    """Return a complete HTML page for one lesson, in the dark or light theme.

    vendor_dir is the folder holding node_modules (MathJax and Prism). It is
    given as an absolute file URL, because the page's base URL is the lesson's
    own folder, not the app's.
    """
    body = EMPTY_HEADER.sub("", _PARSER.render(math_symbols(markdown_text)))
    head = HEAD.replace("VENDOR_URL", vendor_dir.as_uri()).replace("__CSS__", CSS if dark else LIGHT_CSS)
    return head + body + TAIL
