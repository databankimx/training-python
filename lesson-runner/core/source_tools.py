"""Text helpers for step source: lint comments and the badges that describe what a step does."""

from __future__ import annotations

import re

LINT_COMMENT = re.compile(r"#\s*(pylint|nosonar)", re.IGNORECASE)

BADGE_RULES = (
    (re.compile(r"plt\.show\("), "Window",
     "Opens in a new window"),
    (re.compile(r"(?<!plt)\.show\("), "Browser",
     "Opens in browser"),
    (re.compile(r"offline\.plot\("), "Browser",
     "Opens in browser"),
    (re.compile(r"savefig\(|write_html\(|write_text\(|json\.dump\("), "Saves file",
     "Writes a file to disk, next to the script or in its data folder."),
    (re.compile(r"requests\.get\("), "Internet",
     "Calls an internet service. Needs a connection, and can fail if the rate limit is reached."),
    (re.compile(r"\binput\("), "Input",
     "Asks you to type a reply. You'll be prompted in a dialog box."),
)


BADGE_GLYPHS = {"Window": "window", "Browser": "globe", "Input": "keyboard",
                "Saves file": "disk", "Internet": "cloud"}


def strip_lint_comments(source: str) -> str:
    """Remove #pylint and #NOSONAR comments from source shown in the editor.

    A line that is only such a comment is dropped. On other lines, only the comment is cut off.
    """
    kept = []
    for line in source.split("\n"):
        if LINT_COMMENT.search(line):
            if line.lstrip().startswith("#"):
                continue
            line = re.sub(r"\s*#\s*(pylint|nosonar).*$", "", line, flags=re.IGNORECASE) #NOSONAR
        kept.append(line)
    return "\n".join(kept)


def step_badges(source: str) -> list[tuple[str, str]]:
    """
    Badges for what a step does, as (label, tooltip), each label once.
    Comment lines are ignored.
    """
    code = "\n".join(line for line in source.splitlines() if not line.lstrip().startswith("#"))
    found: dict[str, str] = {}
    for pattern, label, tip in BADGE_RULES:
        if label not in found and pattern.search(code):
            found[label] = tip
    return list(found.items())
